import datetime


class InputClass:

    @staticmethod
    def read_str_input(hint):                           # define procedure for string type reading
        print(hint)
        return input()

    @staticmethod
    def read_date_input(hint):                          # define procedure for date type reading
        print(hint)
        while 1:
            try:
                date = datetime.datetime.strptime(input("Enter date in format 'YYYY-MM-DD' :"), "%Y-%m-%d")
                break
            except ValueError:
                print("something went wrong, please enter correct date value 'YYYY-MM-DD'")
        return date                                     # return only correct date input

    @staticmethod
    def read_correct_char(tuple_of_chars, hint):        # define procedure for source type reading
        while 1:
            ans = input(hint)                           # save input into ans variable
            if ans in tuple_of_chars:
                return ans                              # return only correct source of input and stop cycle
