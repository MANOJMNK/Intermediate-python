import re
s1=" psl Welcome to psl,pune"
s2="pslWelcome to PSL,pune"
n=re.search("PSL",s1,re.IGNORECASE)

print "regex object=",n

if n!=None:
    print "found content=",n.group()
else:
    print "Match Not found"
#part two
 
