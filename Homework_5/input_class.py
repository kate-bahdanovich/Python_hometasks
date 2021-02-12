import datetime


class InputClass:
    @staticmethod
    def choose_event():
        ans = input("choose event to input: 1 - for news, 2 - for advertising, 3 - for comment, 4 - to close the program =>")
        while ans not in ("1", "2", "3", "4"):
            ans = input("type correct input event: 1 - for news, 2 - for advertising, 3 - for comment, 4 - to close the program =>")
        else:
            return ans

    @staticmethod
    def read_str_input(hint):
        print(hint)
        return input()

    @staticmethod
    def read_date_input(hint):
        print(hint)
        while 1:
            try:
                date = datetime.datetime.strptime(input("Enter date in format 'YYYY-MM-DD' :"), "%Y-%m-%d")
                break
            except ValueError:
                print("something went wrong, please enter correct date value 'YYYY-MM-DD'")
        return date
