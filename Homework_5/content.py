import datetime
from input_class import InputClass


class Content:
    def __init__(self):
        self.text = ''
        self.pub_date = ''
        self.type = ''
        self.pub_body = ''

    def set_pub_date(self):
        self.pub_date = datetime.datetime.now()
        return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


class News(Content, InputClass):
    def __init__(self):
        Content.__init__(self)
        self.city = ''
        self.type = 'News'

    def create_publication_body(self):
        self.text = InputClass.read_str_input("input news text:")
        self.city = InputClass.read_str_input("input news city:")
        self.pub_date = Content.set_pub_date(self)
        self.pub_body = f"{self.text}\n{self.city}, {self.pub_date}"


class Advert(Content, InputClass):
    def __init__(self):
        Content.__init__(self)
        self.exp_date = ''
        self.num_of_days = 0
        self.type = 'Advertising'

    def create_publication_body(self):
        self.text = InputClass.read_str_input("input advertising text:")
        self.exp_date = InputClass.read_date_input("input advertising expiration date:")
        Content.set_pub_date(self)
        self.num_of_days = (self.exp_date - self.pub_date).days
        self.pub_body = f"{self.text} \nActual until: {self.exp_date.strftime('%d/%m/%Y')}, {self.num_of_days} days left"


class UserComment(Content, InputClass):
    def __init__(self):
        Content.__init__(self)
        self.user_name = ''
        self.type = 'User Comment'

    def create_publication_body(self):
        self.text = InputClass.read_str_input("input user comment text:")
        self.user_name = InputClass.read_str_input("input user name:")
        self.pub_date = Content.set_pub_date(self)
        self.pub_body = f"{self.text}'\nFrom {self.user_name}, at {self.pub_date}"
