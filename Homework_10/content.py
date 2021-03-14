import datetime
from input_class import InputClass
from homework_4_2 import normilize_str
from content_output_to_DB import ContentToDB


class Content:
    def __init__(self):                                                     # define common fields for all types of content
        self.text = ''
        self.pub_date = ''
        self.type = ''
        self.pub_body = ''
        self.input_type = 'console'
        self.insert_query = ''
        self.mistakes_flag = 0

    def set_pub_date(self):                                                 # define function for publication date setting
        self.pub_date = datetime.datetime.now().replace(microsecond=0)                             # generate current date-time...
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
        if self.mistakes_flag == 0:
            self.__pretty_content()                                         # format content for file writing
            f = open(name, "a")                                             # open file for writing
            f.write(self.pretty_cont)                                       # write publication to a file
            f.close()                                                       # close
            self.write_content_to_db()

    def write_content_to_db(self):
        db = ContentToDB()
        db.insert_content(self.insert_query)
        del db

class News(Content):                                                        # define news content type
    def __init__(self, values_source=None):                                 # by default object will be created from console input
        Content.__init__(self)                                              # define fields from parent class
        if not values_source:                                               # create object from console(default)
            self.__set_values_from_console()                                # get object field's values from console
        elif type(values_source) is dict:                                   # create file from dictionary
            try:                                                            # if source dictionary has all required fields
                self.city = values_source["city"]                           # set city
                self.text = normilize_str(values_source["text"])            # set normalized text
            except KeyError:                                                # if some field name is missed
                self.mistakes_flag = 1                                      # set flag for mistakes from object creation
                print(f"a News publication can not be created from dict {values_source}")
            self.input_type = 'file_json'
        else:                                                               # else - create object from file using list of values 'values_source'
            self.city = values_source[2]                                    # set city
            self.text = normilize_str(values_source[1])                     # set text
            self.input_type = 'file_txt'                                    # set input_type
        self.type = 'News'                                                  # common field for all types of fields setting

    def __set_values_from_console(self):                                    # define procedure for setting fields values from console
        user_input = InputClass()                                           # use object of InputClass
        self.text = user_input.read_str_input("input news text:")           # input text
        self.text = normilize_str(self.text)
        self.city = user_input.read_str_input("input news city:")           # input city

    def create_publication_body(self):                                      # form publication body (common fields for all content types)
        if self.mistakes_flag == 0:
            Content.set_pub_date(self)                      # set publication date
            self.pub_body = f"{self.text}\n{self.city}, {self.pub_date}"    # form news body
            # define query string for inserting News data to DB
            self.insert_query = f"INSERT INTO News VALUES ('{self.text}','{self.city}','{self.pub_date}')"


class Advert(Content):                                                      # define private advert type
    def __init__(self, values_source=None):                                 # by default object will be created from console input
        Content.__init__(self)                                              # define fields from parent class
        if not values_source:                                               # create object from console(default)
            self.__set_values_from_console()                                # get object field's values from console (date input is corrected via console dialog)
        elif type(values_source) is dict:                                   # create file from dictionary
            try:                                                            # if source dictionary has all required fields
                self.exp_date = datetime.datetime.strptime(values_source["exp_date"], "%Y-%m-%d")
                self.text = normilize_str(values_source["text"])            # set normalized text
            except KeyError:                                                # if some field name is missed
                self.mistakes_flag = 1                                      # set flag for mistakes from object creation
                print(f"an Advert publication can not be created from dict {values_source}")
            except ValueError:                                              # handle incorrect date
                print(f"{values_source} date value is not using format 'YYYY-MM-DD' or provided date is not correct")
                self.mistakes_flag = 1                                      # set flag for mistakes from object creation
            self.num_of_days = 0                                            # set num_of_days
            self.input_type = 'file_json'
        else:                                                               # else - create object from file using list of values 'values_source'
            try:                                                            # check whether date provided from file is correct and try to set 'exp_date' from this value
                self.exp_date = datetime.datetime.strptime(values_source[2], "%Y-%m-%d")
            except ValueError:                                              # handle incorrect date
                print(f"{values_source} date value is not using format 'YYYY-MM-DD' or provided date is not correct")
                self.mistakes_flag = 1                                      # set flag for mistakes from object creation
            self.text = normilize_str(values_source[1])                     # set text
            self.num_of_days = 0                                            # set num_of_days
            self.input_type = 'file_txt'                                    # set input_type
        self.type = 'Advertising'                                           # common field for all types of fields setting

    def __set_values_from_console(self):                                    # define procedure for setting fields values from console
        user_input = InputClass()                                           # use object of InputClass
        self.text = user_input.read_str_input("input advertising text:")    # input text
        self.text = normilize_str(self.text)
        self.exp_date = user_input.read_date_input("input advertising expiration date:")    # input date (date input is corrected via console dialog)

    def create_publication_body(self):                                      # form publication body
        Content.set_pub_date(self)                                          # set publication date
        if self.mistakes_flag == 0:                                         # we can handle incorrect dates by skipping such values. If dates are correct
            self.num_of_days = (self.exp_date - self.pub_date).days         # calculate number of days
            self.pub_body = f"{self.text} \nActual until: {self.exp_date.strftime('%Y-%m-%d')}," \
                            f" {self.num_of_days} days left"                # form advertising body with date and number_of_days
            # define query string for inserting Advert data to DB
            self.insert_query = f"INSERT INTO Advert VALUES ('{self.text}','{self.exp_date}','{self.pub_date}')"
        else:                                                               # if provided date is not correct
            self.pub_body = f"{self.text} \nActual until: provided date is not a correct date "                                 # form advertising body without date and number of days
            # define query string for inserting advert without date data to DB
            self.insert_query = f"INSERT INTO Advert VALUES ('{self.text}',NULL,'{self.pub_date}')"


class UserComment(Content):                                                 # define user comment type
    def __init__(self, values_source=None):                                 # by default object will be created from console input
        Content.__init__(self)                                              # define fields from parent class
        if not values_source:                                               # create object from console(default)
            self.__set_values_from_console()                                # get object field's values from console
        elif type(values_source) is dict:                                   # create object from dictionary
            try:                                                            # if source dictionary has all required fields
                self.user_name = values_source["user_name"]                 # set user_name
                self.text = normilize_str(values_source["text"])            # set normalized text
            except KeyError:
                self.mistakes_flag = 1
                print(f"a UserComment publication can not be created from dict {values_source}")
            self.input_type = 'file_json'
        else:                                                               # else - create object from file using list of values 'values_source'
            self.user_name = values_source[2]                               # set user_name value
            self.text = values_source[1]                                    # set text value
            self.input_type = 'file_text'                                   # set input_type
        self.type = 'User Comment'                                          # common field for all types of fields setting

    def __set_values_from_console(self):                                    # define procedure for setting fields values from console
        user_input = InputClass()                                           # use object of InputClass
        self.text = user_input.read_str_input("input user comment text:")   # input text
        self.text = normilize_str(self.text)                                # normalize field "text"
        self.user_name = user_input.read_str_input("input user name:")      # input city

    def create_publication_body(self):                                      # form publication body
        if self.mistakes_flag == 0:
            Content.set_pub_date(self)
            self.pub_body = f"{self.text}\nFrom {self.user_name}, at {self.pub_date}"  # for publication body
            # define query string for inserting user comment data to DB
            self.insert_query = f"INSERT INTO UserComment VALUES ('{self.text}','{self.user_name}','{self.pub_date}')"
