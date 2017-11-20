import re
import string
from IPython import embed

def is_pangram(sentence):
    char_strings = string.ascii_lowercase
    sentence_strings = ''.join(sorted(set(re.sub('[^a-z]+', '', sentence.lower()))))

    if char_strings == sentence_strings:
        return True
    else:
        return False
