import re
def is_isogram(string):
    string = re.sub('[^A-Za-z0-9]+', '', string.lower())
    return len(string) == len(set(string))
