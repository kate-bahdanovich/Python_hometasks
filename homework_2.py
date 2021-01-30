# 1. create a list of random number of dictionaries (from 2 to 10)
import random                                           # import "random" module to get access to the random object (or whatever it is)
n = random.randint(2, 10)                               # define a variable to store a number of the dictionaries
s = []                                                  # create a list of char a-z to avoid repeated keys for one dictionary
for i in range(97, 123):                                # from random integer ascii code ...
    s.append(chr(i))                                    # add char from code to the list s
a = []                                                  # define a variable to store the list of the dictionaries
for i in range(0, n):
    m = random.randint(1, 10)                           # generate random length for a dictionary
    keys = random.sample(s, m)                          # generate list of unique keys from s (size = m)
    dictionary = {}                                     # define dictionary of
    for j in range(0, m):                               # create a dictionary of random length m ...
        dictionary[keys[j]] = random.randint(0, 100)    # .. that gets keys from "keys" list and values from 0 to 100
    print(i+1, " created dictionary: ", dictionary)     # print each dictionary
    a.append(dictionary)                                # add dictionary to the list

# 2. get previously generated list of dicts and create one common dict:
res_list = {}                                           # define a variable to store a temporary auxiliary dictionary
for dictionary in a:                                    # loop through a list of dictionaries
    for key in dictionary.keys():                       # loop through each dictionary list of keys
        if res_list.setdefault(key, -1) == -1:          # if such key does not exist in the resulted dictionary => create element - key:[value,dictionary_index,count = 1]
            res_list[key] = [dictionary[key], a.index(dictionary), 1]
        else:                                           # such key value exists in the resulted dictionary...
            dic_element = res_list.pop(key)             # ... then we need to delete it.... and create a new one - key:[MAX(value1,value2),INDEX(max_value),count+1]
            if dic_element[0] < dictionary[key]:        # if existed_element < new_element ...
                # then assign values from new_element and ++ count:
                res_list[key] = [dictionary[key], a.index(dictionary), dic_element[2] + 1]
            else:
                # then assign values from existed_element and ++ count:
                res_list[key] = [dic_element[0], dic_element[1], dic_element[2] + 1]
# print("temporary dictionary with unique keys,max values,indices of the dictionary with max value,count of the key duplicates:")
# print(res_list)

# convert temporary dictionary into correct form
result = {}                                             # define a variable to store the resulted dictionary
for key in res_list.keys():                             # loop through auxiliary dictionary
    if res_list[key][2] > 1:                            # if count for current key > 1 (means that key was contained at 2+ source dictionaries
        new_key = key+"_"+str(res_list[key][1]+1)       # create a new key from the old key and a source dictionary index
        result[new_key] = res_list[key][0]              # add new_key:value to the resulted dictionary
    else:                                               # else....
        result[key] = res_list[key][0]                  # ... keep key unchanged and add key:value to the resulted dictionary
print("resulted dictionary looks like this:")
print(result)
