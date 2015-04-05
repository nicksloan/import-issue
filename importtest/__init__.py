from __future__ import absolute_import
print "__init__"

def test():
    print "a is %s" % globals().get('a')

test()
