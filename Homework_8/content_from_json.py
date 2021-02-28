import os
import json


# define class to read content from json file
class ReadContentFromJson:
    # define object constructor with default file path and tuple for content types handling
    def __init__(self, file_path="content_source.json", handling_types=()):
        # set file_path
        self.file_path = file_path
        # set handling_types
        self.handling_types = handling_types
        # it is expected that all json objects from file will be turned into publications
        self.successful_processing = "true"

    # define procedure for file reading, skipping lines with incorrect format and returning list of correct lines
    def read_content(self):
        # define empty result
        list_events = []
        # try to open default file
        try:
            with open(self.file_path, "r") as f:
                # load objects to the list
                list_from_file = json.load(f)
                # loop through the file lines
                for event in list_from_file:
                    # if this dictionary has less then 3 values (not enough for content creation)
                    if len(event) < 3:
                        print(f"line '{event}' has been skipped cause of the wrong format")
                        # mark this file as having mistakes
                        self.successful_processing = "false"
                    # there is no 'type' key in the current dictionary
                    elif event.setdefault('type', -1) == -1:
                        print(f"line '{event}' has been skipped cause of the missed 'type'")
                        # mark this file as having mistakes
                        self.successful_processing = "false"
                    # if provided content type is not handled
                    elif event['type'] not in self.handling_types:
                        print(f"line '{event}' has been skipped cause of the non-handling type of content")
                        # mark this file as having mistakes
                        self.successful_processing = "false"
                    # from current line content can be created
                    else:
                        # add list created from current file line to result
                        list_events.append(event)
        # if default or provided file could not be found
        except FileNotFoundError:
            print(f"source file '{self.file_path}' does not exists")
        # return composed list[dict]
        return list_events

    # define procedure for changing 'successful_processing' parameter from outside of the class
    def set_successful_processing(self, successful_processing='false'):
        self.successful_processing = successful_processing

    # define class destructor for handling file deleting
    def __del__(self):
        # if default or provided file exists
        if os.path.isfile(self.file_path):
            # use 'successful_processing' flag to define whether file should be deleted
            if self.successful_processing == "true":
                # delete file
                os.remove(self.file_path)
                print(f"file {self.file_path}  has been deleted")


if __name__ == '__main__':                                                      # for testing purpose
    x = ReadContentFromJson(handling_types=("News", "2"))                       # create object
    a = x.read_content()                                                        # get 'clean' content for publication as a list[list[str]]
