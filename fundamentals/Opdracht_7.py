import keyword
print(keyword.kwlist)


def contains_keyword(*string_values):
    for words in string_values:
        words = str(words)
        if keyword.iskeyword(words):
            print("True")
            break
    else:
        print("False")


contains_keyword("hello", "goodbye")
contains_keyword("def", "haha", "lol", "chickens are evil", 42)
contains_keyword("four", "for", "if")
contains_keyword("blabla", "doggo", "crab", "anchor")
contains_keyword("grizzly", "ignore", "return", "False")