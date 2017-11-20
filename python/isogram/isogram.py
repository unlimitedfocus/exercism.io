import re
def is_isogram(string):
    string = re.sub('[^A-Za-z0-9]+', '', string.lower())
    size = len(string)
    if 2 > size:
        return True
    else:
        return size == len(set(string))
