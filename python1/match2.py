import re
input1="xyxy:xyz:xxz:xxxz"
m=re.search("xy*z",input1)   #match is xyyyyyyz
n=re.search("xy+z",input1)    #3 match is  xyyyyyyz no match-xz
k=re.search("xy?z",input1)    #match xz
l=re.search("(xy)+z",input1)   #match is xyxyxyz
#p=re.search("^\d+$")    #multi digit number only
q=re.split(":",input1)    #split function returns a list ['xyxy', 'xyz', 'xxz', 'xxxz']

print "l=",l
if l!=None:
    print "match content=",l.group()   #pune
else:
    print "Match not found"
print "...................."
print "q=",q
if q!=None:
    print "match content=",q   #pune
    print len(q)    #4
else:
    print "Match not found"
print "...................."

pattern=r'\d'
s3="str1:str2*str3?ster4"
list3=re.split(pattern,s3)
print list3
print "....................."

 
s3="str1:str2;str3---str4,str5"
list4=re.split('[:;,]|---',s3)
print list4
print "....................."
