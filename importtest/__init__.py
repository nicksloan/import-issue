print("__init__")

def test():
    print("a is {}".format(globals().get('a')))

test()
