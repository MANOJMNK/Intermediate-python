#meta charector (^,$)
import re
s1="PSL Welcome to psl,punePSL"
s2="pslWelcome to PSL,pune"
n=re.search("^PSL",s1)
print "n=",n
if n!=None:
    print n.group()
else:
    print "Match not found"
