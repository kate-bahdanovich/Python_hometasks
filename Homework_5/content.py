import datetime
from input_class import InputClass

class Content:
    def __init__(self):                                                     # define common fields for all types of content
        self.text = ''
        self.pub_date = ''
        self.type = ''
        self.pub_body = ''

    def set_pub_date(self):                                                 # define function for publication date setting
        self.pub_date = datetime.datetime.now()                             # generate current date-time...
        return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")        # return it as a string

    def __format_type(self, symb='-', pretty_len=40):                       # define function for type formatting into --- Type --- view
        type_len = len(self.type)                                           # get length of the string containing object type
        num_of_symb = int((pretty_len - 2 - type_len) / 2)                  # calculate proper number of repeated symbols
        return f"{symb * num_of_symb} {self.type} {symb * num_of_symb}\n"   # return "--------- Type ---------"

    def __pretty_content(self):                                             # define function that forms content for a file
        self.pretty_cont = self.__format_type()                             # add as a 1st string pretty_Type
        self.pretty_cont = self.pretty_cont + self.pub_body + "\n"          # add pub_body specified for each content type
        self.pretty_cont = self.pretty_cont + "\n\n"                        # add empty lines after publication main text

    def write_content(self, name="feed.txt"):                               # define function which write content to the select file
        self.__pretty_content()                                             # format content for file writing
        f = open(name, "a")                                                 # open file for writing
        f.write(self.pretty_cont)                                           # write publication to a file
        f.close()                                                           # close


class News(Content, InputClass):                                            # define news content type
    def __init__(self):
        Content.__init__(self)
        self.city = ''
        self.type = 'News'

    def create_publication_body(self):                                      # form publication body
        self.text = InputClass.read_str_input("input news text:")           # input text
        self.city = InputClass.read_str_input("input news city:")           # input city
        self.pub_date = Content.set_pub_date(self)                          # set publication date
        self.pub_body = f"{self.text}\n{self.city}, {self.pub_date}"        # form news body


class Advert(Content, InputClass):                                          # define private advert type
    def __init__(self):
        Content.__init__(self)
        self.exp_date = ''
        self.num_of_days = 0
        self.type = 'Advertising'

    def create_publication_body(self):                                      # form publication body
        self.text = InputClass.read_str_input("input advertising text:")    # input text
        self.exp_date = InputClass.read_date_input("input advertising expiration date:")    # input date
        Content.set_pub_date(self)                                          # set publication date
        self.num_of_days = (self.exp_date - self.pub_date).days             # calculate number of days
        self.pub_body = f"{self.text} \nActual until: {self.exp_date.strftime('%d/%m/%Y')}, {self.num_of_days} days left"       # form advertising body


class UserComment(Content, InputClass):                                     # define user comment type
    def __init__(self):
        Content.__init__(self)
        self.user_name = ''
        self.type = 'User Comment'

    def create_publication_body(self):                                      # form publication body
        self.text = InputClass.read_str_input("input user comment text:")   # input text
        self.user_name = InputClass.read_str_input("input user name:")      # input user name
        self.pub_date = Content.set_pub_date(self)                          # set publication date
        self.pub_body = f"{self.text}'\nFrom {self.user_name}, at {self.pub_date}"  # for publication body
