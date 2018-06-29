import re
print re.sub("PSL","persistent","Welcome to PSl,PSL in pune")
print ".............."
string="if the problem is texual,use the the re module"
print "original string=",string
pattern=r"the the"
regexp=re.compile(pattern)
str=regexp.sub("the",string)
print "modiied string=",str
