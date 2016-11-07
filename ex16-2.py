from sys import argv

script, filename = argv

print "Your filename is %r." % filename

insides = open(filename)
outside =  insides.read()

print """
Contents of  your file is:
%r
""" % outside

insides.close()
