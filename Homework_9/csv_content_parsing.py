import csv
from string import punctuation
from decimal import Decimal
import os.path


# new class to work with csv files
class ContentParsingToCsv:
    # constructor for initialization required fields
    def __init__(self, file_words_path="words.csv", file_letters_path="letters.csv"):
        # dictionary to store words statistics
        self.words = {}
        # dictionary to store letters statistics
        self.letters = {}
        self.letters_number = 0
        self.file_words_path = file_words_path
        self.file_letters_path = file_letters_path
        # read existing words statistics from word's file
        self.__read_csv_words()
        # read existing words statistics from letter's file
        self.__read_csv_letters()

    # define procedure for words statistics initializing
    def __read_csv_words(self):
        # if specified file_path exist...
        if os.path.isfile(self.file_words_path):
            # ...open it for reading
            with open(self.file_words_path, 'r') as f:
                # create object to work with the csv file
                csv_content = csv.reader(f, delimiter='-')
                # read each line from a file to a dictionary
                for row in csv_content:
                    self.words[row[0]] = int(row[1])

    # define procedure for words statistics initializing
    def __read_csv_letters(self):
        # if specified file_path exist...
        if os.path.isfile(self.file_words_path):
            # ...open it for reading
            with open(self.file_letters_path, 'r') as f:
                # create object to work with the csv file
                reader = csv.DictReader(f)
                # read each line from a file to a dictionary
                for row in reader:
                    self.letters[row['letter']] = [int(row['count_all']),
                                                   int(row['count_uppercase']),
                                                   Decimal(row['percentage'])]
                    # calculate letters number for letters statistics
                    self.letters_number = self.letters_number + int(row['count_all'])

    # define function to write word's statistics to specified csv file
    def write_csv_words(self, source_str):
        # parse new string and add it to a word's statistics
        self.__parse_words(source_str)
        # open specified file to write word's statistics
        with open(self.file_words_path, 'w', newline='') as f:
            # created object to work with csv file
            writer = csv.writer(f, delimiter='-')
            # for each pair {word:count} from obtained self.words dictionary
            for word in self.words.keys():
                # write {word:count} from dictionary to a file
                writer.writerow([word, self.words[word]])

    # define function to write letter's statistics to specified csv file
    def write_csv_letters(self, source_str):
        # parse new string and add it to a letter's statistics
        self.__parse_letters(source_str)
        # open specified file to write word's statistics
        with open(self.file_letters_path, 'w', newline='') as f:
            # define field's names for csv file
            fieldnames = ['letter', 'count_all', 'count_uppercase', 'percentage']
            # created object to work with csv file
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            # write header to a file
            writer.writeheader()
            # for each pair {letter:[count,count_upper,percentage]} from obtained self.letters dictionary
            for letter in self.letters.keys():
                # write {letter:[count,count_upper,percentage]} to a file
                writer.writerow({'letter': letter,
                                 'count_all': self.letters[letter][0],
                                 'count_uppercase': self.letters[letter][1],
                                 'percentage': self.letters[letter][2]})

    # define procedure to parse new string to the words dictionary
    def __parse_words(self, source_str):
        # remove punctuation chars from a string
        for p_char in punctuation:
            source_str = source_str.replace(p_char, ' ')
        # for each word from new string
        for i in source_str.split():
            # if current word is a number...
            if i.isnumeric():
                # ...skip it
                continue
            # convert current word to lower case variant
            word = i.lower()
            # if such 'word' does not exist in the resulted dictionary => create element - word: count = 1
            if self.words.setdefault(word, -1) == -1:
                self.words[word] = 1
            else:  # such word value exists in the resulted dictionary...
                # increase count for this word by 1
                self.words[word] = self.words[word] + 1

    # define procedure to parse new string to the letters dictionary
    def __parse_letters(self, source_str):
        # drop numeric 'letters' from new string
        for n_char in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            source_str = source_str.replace(n_char, '')
        # drop punctuation chars from new string
        for p_char in punctuation:
            source_str = source_str.replace(p_char, '')
        # remove whitespaces from source string
        source_str = "".join(source_str.split())
        # calculate new number of the letters
        self.letters_number = self.letters_number + len(source_str)
        # convert chars from a string to a list and loop trhough all chars
        for i in list(source_str):
            # lower case current letter
            letter = i.lower()
            # set upper_flag (1 or 0) for current letter
            if i.isupper():
                upper_flag = 1
            else:
                upper_flag = 0
            # if such letter does not exist in the resulted dictionary => create element - letter:[count,count_upper,percent]
            if self.letters.setdefault(letter, -1) == -1:
                self.letters[letter] = [1, upper_flag, 0]
            else:  # such letter value exists in the resulted dictionary...
                # add 1 to letters  count
                self.letters[letter][0] = self.letters[letter][0] + 1
                # add 1 to upper_count for Upper letters
                self.letters[letter][1] = self.letters[letter][1] + upper_flag
        # recalculate percentage for all letters from self.letters
        for letter in self.letters.keys():
            self.letters[letter][2] = round(self.letters[letter][0] / self.letters_number * 100, 2)


# for testing purposes
if __name__ == '__main__':
    t = ContentParsingToCsv(file_words_path='test.csv')
    t.write_csv_words("""Privet.
    priiveT.1234.""")
