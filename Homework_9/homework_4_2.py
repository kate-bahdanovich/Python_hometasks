if __name__ == '__main__':
    s_input = '''homEwork:
    
      tHis iz your homeWork, copy these Text to variable.
    
    
    
      You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
    
    
    
      it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
    
    
    
      last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

def get_number_of_whitespaces(s):
    s_temp = "".join(s.split())                             # create string without whitespaces. Subtract the length of input string and the length of temp string
    return len(s) - len(s_temp)

if __name__ == '__main__':
    print(get_number_of_whitespaces(s_input))

def set_upper_case_after_char(s,c):
    list_of_paragraph = s.split(c)                          # create a list of paragraphs
    number_of_paragraph = len(list_of_paragraph)            # preparation to the cycle through a list of paragraphs
    for i in range(0, number_of_paragraph):                 # with each paragraph...
        list_of_words = list_of_paragraph[i].split(" ")     # find the first word of the paragraph 'i', which could start with " ". Split paragraph 'i' by " "
        word = list_of_words[0]                             # preparation to the cycle through list of words
        n = len(list_of_words)
        j = 0
        while not word and j < n - 1:                       # loop while a 'real' word is not found or list is not ended
            j = j + 1                                       # iterate j
            word = list_of_words[j]                         # iterate word
        list_of_words[j] = list_of_words[j].capitalize()    # capitalise a first real word (or capitalise "" for paragraph without real words)
        list_of_paragraph[i] = " ".join(list_of_words)      # join words back to paragraph
    return c.join(list_of_paragraph)

def normilize_str(s):
    s = s.lower()                                           # convert string to the lower case words
    s = s.replace(' iz ', ' is ')                           # replace iz => is. there was no special functionality for mistakes correction, so it stays inside "normalize"
    s = set_upper_case_after_char(s, "\n")                  # capitalize first words of the paragraph
    s = set_upper_case_after_char(s, ".")                   # capitalize first words after "."
    return s

def get_new_sentence_from_last_words(s):
    list_of_sentence = s.split(".")                         # create list of sentences
    new_sentence = []                                       # define new sentence as a list (for storing last word from each sentence)
    for i in list_of_sentence:                              # loop through a list of sentences
        list_of_words = i.split(" ")                        # create a list of words for each sentence
        new_sentence.append(list_of_words[-1])              # get last word
    new_sentence_str = " ".join(new_sentence)               # create a string from list...
    new_sentence_str = new_sentence_str.capitalize()        # ... and capitalize it
    return new_sentence_str


if __name__ == '__main__':
    s_output = normilize_str(s_input)
    s_output = s_output.replace("paragraph.", "paragraph. " + get_new_sentence_from_last_words(s_output))
    print(s_output)