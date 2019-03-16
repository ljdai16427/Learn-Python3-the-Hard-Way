from sys import argv
from os.path import exists

script, from_files, to_files = argv

print "Copy from %s to %s" % (from_files, to_files)

# We could do these two on one line too, how?

in_file = open(from_files)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_files)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_files, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

