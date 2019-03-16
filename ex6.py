x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

l = 10
k = "There are %d types of people."
print k % l

# a difference between %r and %s

print "I said: %r." % x
print "I said: %s." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of...."
e = "a string with a right sde."

print w + e
print(w + e)
