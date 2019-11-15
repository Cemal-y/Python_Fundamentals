from itertools import groupby

recipients = ["b44 44 4rt   ", "W0u uuT3R", "   4l3x", "K 3 n4n", "54R4h"]


def manipulate_names(string1):
    string1 = string1.replace("4", "a")
    string1 = string1.replace("0", "o")
    string1 = string1.replace("3", "e")
    string1 = string1.replace("5", "s")
    string1 = string1.replace(' ', '')
    string1 = string1.lower()
    string1 = string1.capitalize()
    return string1


def remove_consecutive_duplicates(string1):
    result_str = []
    for (key, group) in groupby(string1):
        result_str.append(key)

    return ''.join(result_str)


for name in recipients:
    temp_name = name
    temp_name = manipulate_names(temp_name)
    temp_name = remove_consecutive_duplicates(temp_name)
    recipients[recipients.index(name)] = temp_name

print(recipients)
