import re
s1="Welcome to aPSL. *PSL&,pune psl"
patt1=r"PSL"
m=re.findall(patt1,s1)
print "m=",m
if m!=None:
    print "match found",m
else:
    print "match not found"



print re.findall('car','car')
print re.findall('car','scary')
print re.findall('car','carry the tarcardi')
