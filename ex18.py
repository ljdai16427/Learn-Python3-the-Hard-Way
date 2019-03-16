# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2, arg3= args
    print("arg1: %r, arg2: %s" % (arg1, arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print("arg1: %r" % arg1)

# this one takes no arguments
def print_none():
    print("I got nothin.")

print_two("Zed", "Shaw", "Ljdai")
print_two_again("Zid", "Shiw")
print_one("First!")
print_none()
