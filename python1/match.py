import re
regexp=re.compile("PSL")
s1="PSLaaaaaaaaa Welcome to peersistent...."
s2="pslaaa PSL Welcome to india"

if regexp.match(s2):
    print "Match found"
else:
    print "Match not found"
print ".................."
if regexp.search(s2):
    print "Match found"
else:
    print "Match not found"


"""
the re module provide regular
"""
