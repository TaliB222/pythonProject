def Anagram(str1, str2):
    #get lengths of both string
    n1=len(str1)
    n2=len(str2)
    #if length of both strings is not the same, then
    #they cannot be anagram
    if n1!=n2:
        return False
    #sort both strings
    str1= sorted(str1)
    str2= sorted(str2)

    #compare sorted string
    for i in range(1, n1):
        if str1[i]!= str2[i]:
            return False
        else:
            return True

#
if Anagram("rat", "tar"):
    print("True")
else:
    print("False")

