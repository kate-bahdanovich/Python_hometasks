import content
from input_class import InputClass
from homework_6 import ReadContentFromTxt
from csv_content_parsing import ContentParsingToCsv

hint_for_console_input = "choose event to input: 1 - for news, 2 - for advertising, 3 - for comment, 0 - to close the program =>"
user_input = InputClass                                                                     # create object to read user choice
source_of_input = user_input.read_correct_char(("0", "1"), "choose source of import: 0 for file, 1 for console: ")

if source_of_input == "0":                                                                  # new part of 'main' code for handling input from file
    source_file = ReadContentFromTxt(handling_types=("1", "2", "3"))                        # create object to read file input
    list_of_draft_publications = source_file.read_content()                                 # read file content, clean data, normalize 'text' field, return list to a variable
    for draft_publication in list_of_draft_publications:                                    # loop through a list of data suitable for publication creating
        if draft_publication[0] == "1":
            publ = content.News(draft_publication)                                          # if choice = 1 => create News content from 'draft_publication'
        elif draft_publication[0] == "2":
            publ = content.Advert(draft_publication)                                        # if choice = 2 => create Adv content from 'draft_publication'
            if publ.mistakes_flag == 1:                                                     # if we find an incorrect date while 'publ' is created
                source_file.set_successful_processing()                                     # set flag 'file successful processing' to false (default value for procedure)
                continue                                                                    # skip this publication
        elif draft_publication[0] == "3":
            publ = content.UserComment(draft_publication)                                   # if choice = 3 => create UserComment content from 'draft_publication'
        publ.create_publication_body()                                                      # form publication body for each content type
        publ.write_content()                                                                # write publication to a file
        # add data to letter-csv and words-csv files
        csv_data = ContentParsingToCsv()
        # write words to csv for words
        csv_data.write_csv_words(publ.pretty_cont)
        # write letters statistics to the csv for letters
        csv_data.write_csv_letters(publ.pretty_cont)
    del source_file                                                                         # call destructor for file deleting

elif source_of_input == "1":                                                                # user has chose input from console
    publication_type = user_input.read_correct_char(("0", "1", "2", "3"),
                                                    hint_for_console_input)                 # ask for first input
    while publication_type != "0":                                                          # loop until user has chose 0 and  write it to a file
         if publication_type == "1":
             publ = content.News()                                                          # if choice = 1 => create News content
         elif publication_type == "2":
             publ = content.Advert()                                                        # if choice = 2 => create Adv content
         elif publication_type == "3":
             publ = content.UserComment()                                                   # if choice = 3 => create User Comment content
         publ.create_publication_body()                                                     # use method to  create publication body
         publ.write_content()
         # add data to the letter-csv and words-csv files
         csv_data = ContentParsingToCsv()
         # write words to csv for words
         csv_data.write_csv_words(publ.pretty_cont)
         # write letters statistics to the csv for letters
         csv_data.write_csv_letters(publ.pretty_cont)
         publication_type = user_input.read_correct_char(("0", "1", "2", "3"),              # ask user for new choice again
                                                          hint_for_console_input)
