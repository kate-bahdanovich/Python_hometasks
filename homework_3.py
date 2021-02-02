s_input = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

s_temp = "".join(s_input.split())                               # create string without whitespaces. Subtract the length of input string and the length of temp string
print("The number of the whitespaces is:", len(s_input) - len(s_temp))

s_input = s_input.lower()                                       # convert string to the lower case words
s_input = s_input.replace(' iz ', ' is ')                       # replace iz => is. Such replacement will not work in the common cases ((
list_of_paragraph = s_input.splitlines()                        # create a list of paragraphs
number_of_paragraph = len(list_of_paragraph)                    # preparation to the cycle through a list of paragraphs
for i in range(0, number_of_paragraph):                         # with each paragraph...
    list_of_words = list_of_paragraph[i].split(" ")             # find the first word of the paragraph 'i', which could start with " ". Split paragraph 'i' by " "
    word = list_of_words[0]                                     # preparation to the cycle through list of words
    n = len(list_of_words)
    j = 0
    while not word and j < n-1:                                 # loop while a 'real' word is not found or list is not ended
        j = j + 1                                               # iterate j
        word = list_of_words[j]                                 # iterate word
    list_of_words[j] = list_of_words[j].capitalize()            # capitalise a first real word (or capitalise "" for paragraph without real words)
    # there is another way: to delete all spaces at the begining of the each paragraph. But that will not save text format.
    list_of_paragraph[i] = " ".join(list_of_words)              # join words back to paragraph
s_output = "\n".join(list_of_paragraph)                         # join paragraphs back to new output string
# one more split + join iteration to fix Upper case after sentence end. Will work only with "." at the sentence end.
list_of_sentence = s_output.split(".")                          # create a list of sentences
new_sentence = []                                               # define new sentence as a list (for storing last word from each sentence)
number_of_sentence = len(list_of_sentence)                      # preparation to the cycle through a list of sentences
for i in range(0, number_of_sentence):                          # with each sentence...
    list_of_words = list_of_sentence[i].split(" ")              # find the first word of the sentence 'i', which could start with "  " or "\n\n". Split paragraph 'i' by " "
    word = list_of_words[0]                                     # preparation to the cycle through list of words
    n = len(list_of_words)
    j = 0
    while not word and j < n-1:                                 # loop while a 'real' word is not found or list is not ended
        j = j + 1                                               # iterate j
        word = list_of_words[j]                                 # iterate word
    list_of_words[j] = list_of_words[j].capitalize()            # capitalise a first real word
    new_sentence.append(list_of_words[-1])                      # add last word of each sentence to a list
    list_of_sentence[i] = " ".join(list_of_words)               # join words back to the sentence
new_sentence_str = " ".join(new_sentence)                       # create a string from list...
new_sentence_str = new_sentence_str.capitalize()                # ... and capitalize it
s_output = ".".join(list_of_sentence)                           # join sentences back to new string
# add a new sentence.
s_output = s_output.replace("paragraph.", "paragraph. " + new_sentence_str)
print(s_output)
