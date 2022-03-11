def is_isogram(string):
    test = ''.join(filter(str.isalnum, string.lower()))
    return len(test) == len(set(test))