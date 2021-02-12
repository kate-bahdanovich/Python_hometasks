import content


class WriteContentToTxt:
    def __init__(self, cont):
        self.type = cont.type
        self.text = cont.pub_body
        self.pub_date = cont.pub_date

    def __format_type(self,symb='-', pretty_len=40):
        type_len = len(self.type)
        num_of_symb = int((pretty_len - 2 - type_len) / 2)
        return f"{symb * num_of_symb} {self.type} {symb * num_of_symb}\n"

    def __pretty_content(self):
        self.pretty_cont = self.__format_type()
        self.pretty_cont = self.pretty_cont + self.text + "\n"
        self.pretty_cont = self.pretty_cont + "\n\n"

    def write_content(self, name="feed.txt"):
        self.__pretty_content()
        f = open(name, "a")
        f.write(self.pretty_cont)
        f.close()



# news = content.UserComment()
# news.create_publication_body()
# print(news.pub_body)
#
# text = WriteToTxt(news)
# text.write_content()

