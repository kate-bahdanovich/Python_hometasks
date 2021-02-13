import content
from input_class import InputClass

user_input = InputClass                 # create object to read user choice
ans = user_input.choose_event()         # ask for first input
while ans != "4":                       # loop until user has not choose 4
    if ans == "1":
        publ = content.News()           # if choice = 1 => create News content
    elif ans == "2":
        publ = content.Advert()         # if choice = 2 => create Adv content
    elif ans == "3":
        publ = content.UserComment()    # if choice = 3 => create User Comment content
    publ.create_publication_body()      # use method to  create publication body
    publ.write_content()                # and  write it to a file
    ans = user_input.choose_event()     # ask user for new choice
