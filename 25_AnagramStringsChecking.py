def anagramStrings(s1,s2):

    if len(s1)!=len(s2):
     return False
    
    r1=sorted(s1)
    r2=sorted(s2)

    return r1==r2


s1="aaMdra"
s2="Madara"

ans=anagramStrings(s1,s2)
if ans:
   print("strings are anagram")
else:
   print("strings are not anagram")

