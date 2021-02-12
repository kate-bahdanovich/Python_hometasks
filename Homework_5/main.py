import content
from input_class import InputClass
from output_to_file import WriteContentToTxt

def main ():
    user_input = InputClass
    ans = user_input.choose_event()
    while ans != "4":
        if ans == "1":
            publ = content.News()
        elif ans == "2":
            publ = content.Advert()
        elif ans == "3":
            publ = content.UserComment()
        publ.create_publication_body()
        file_pub = WriteContentToTxt(publ)
        file_pub.write_content()
        ans = user_input.choose_event()

main()