import re
s1="PSL Welcome pune to psl,punePSL."
s2="98785_YslWelcome to 4765 PSL+pune"
s3="5"
s4="\n"
n=re.search("psl|pune",s1) #|is alternative PSL,whichever found first is a match
m=re.search("^5$",s3)    #"5"-----match found "5gjfhhhfddd" -NOT a match
k=re.search("^.$",s4)
p=re.search("[*+?]",s2)
q=re.search("[a-zA-Z]",s2)
r=re.search("[0-9]$",s2)
s=re.search("[^A-Z]",s2)
t=re.search("[^0-9]",s2)     #negation
u=re.search("^\D",s2)      #\d digit match    \D digit not match
v=re.search("[^a-zA-Z0-9_]",s2)     #[a-zA-Z0-9_]  -->\w alpha numeric word charector   [^a-zA-Z0-9_]   -->\W non alpha numeric word charector
                                            #[\n\t\r]  --> \s a white space    or [\n\t\r]  ---> \S 
                                             #"^[a-zA-Z]\d$"





if n!=None:
    print n.group()   #pune
else:
    print "Match not found"
print "...................."
if m!=None:
    print m.group()   #pune
else:
    print "Match not found"
print "....................."
if k!=None:
    print k.group()   #pune
else:
    print "Match not found"

print "....................."
if p!=None:
    print "match content=",p.group()   #pune
else:
    print "Match not found"
print "....................."
if q!=None:
    print "match content=",q.group()   #pune
else:
    print "Match not found"

print "....................."
if r!=None:
    print "match content=",r.group()   #pune
else:
    print "Match not found"
print "....................."
if s!=None:
    print "match content=",s.group()   #pune
else:
    print "Match not found"

print "....................."
if t!=None:
    print "match content=",t.group()   #pune
else:
    print "Match not found"

print "....................."
if u!=None:
    print "match content=",u.group()   #pune
else:
    print "Match not found"
print "....................."
if v!=None:
    print "match content=",v.group()   #pune
else:
    print "Match not found"


"""
charector class group
a|B|c|d     ---->"[abcd]"
[a-z]     match any 1 capital alphabet bet a to z
[A-Z]      match any 1 capital alphabet bet A TO Z
[a-zA-Z]
[A-Z|a-z]
"""
