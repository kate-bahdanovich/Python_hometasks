from homework_4_2 import normilize_str
import os


class ReadContentFromTxt:                                                                  # define class to read content(any type) from file
    def __init__(self, file_path="content_source.txt", handling_types=()):                 # define object constructor with default file path and tuple for content types handling
        self.file_path = file_path                                                         # set file_path
        self.handling_types = handling_types                                               # set handling_types
        self.successful_processing = "true"                                                # it is expected that all lines from file will be turned into publications

    def read_content(self):                                                                # define procedure for file reading, skipping lines with incorrect format and returning list of correct lines
        f = open(self.file_path, "r")                                                      # open file (by default 'content_source.txt')
        list_events = []                                                                   # define empty result
        for i in f:                                                                        # loop through the file lines
            event_properties = (i.rstrip()).split("|")                                     # create list of the file line 'values'
            if len(event_properties) < 3:                                                  # if this list has less then 3 values (not enough for content creation)
                print(f"line '{i.rstrip()}' has been skipped cause of the wrong format")
                self.successful_processing = "false"                                       # mark this object as having mistakes
            elif event_properties[0] not in self.handling_types:                           # if provided content type is not handled
                print(f"line '{i.rstrip()}' has been skipped cause of the non-handling type of content")
                self.successful_processing = "false"                                       # mark this object as having mistakes
            else:                                                                          # from current file line content can be created
                event_properties[1] = normilize_str(event_properties[1])                   # normalize 'text' value
                list_events.append(event_properties)                                       # add list created from current file line to result
        return list_events                                                                 # return composed list[list[str]]

    def set_successful_processing(self, successful_processing='false'):                    # define procedure for changing 'successful_processing' parameter from outside of the class
        self.successful_processing = successful_processing

    def __del__(self):                                                                     # define class destructor for handling file deleting
        if self.successful_processing == "true":                                           # use 'successful_processing' flag to define whether file should be deleted
            os.remove(self.file_path)                                                      # delete file
            print(f"file {self.file_path}  has been deleted")


if __name__ == '__main__':                                                      # for testing purpose
    x = ReadContentFromTxt(handling_types=("1", "2"))                           # create object
    a = x.read_content()                                                        # get 'clean' content for publication as a list[list[str]]
    print(a)                                                                    # print if
    del x                                                                       # test file deletion if publication have been created from all strings
