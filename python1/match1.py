import re
s1=" PSL Welcome to PSL,pune"
s2="pslWelcome to PSL,pune"
pattern=r"PSL"
m=re.match(pattern,s1)
n=re.search(pattern,s1)
print "m=",m
print "n=",n
if m!=None:
    print "found content=",m.group()
else:
    print "Not found"
#part two
if n!=None:
    print "found content=",n.group()
else:
    print "Not found"

