def add_tag(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)


print(add_tag(input("tag"), input("word")))
