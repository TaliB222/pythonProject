# iteration on string
#this function count the freq of the letters in a message
def char_freq(message):

    count=1

    freq={}
    if len(message)==0:
        return
    else:
        for letter in message[0:len(message)+1]:
            if letter not in freq.keys():
             freq[letter]=count
            else:

               freq[letter]=freq[letter]+1

        print(freq)
char_freq("cjdsllll")


#""
#"aba"
 #^

 #result:
 #a,2
 #b,1



