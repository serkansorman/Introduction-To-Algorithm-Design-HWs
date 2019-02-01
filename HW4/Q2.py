dict = {"it","me","was","he","as","test","the","best","soft","of","time","times"}

def isReconstituted(string):
    numOfWord = [-1] * (len(string)+1)
    numOfWord[0] = 0; #Empty string can be reconstituted
    for i in range (len(string)):
        if numOfWord[i] != -1:
            for j in range(i+1,len(string)+1):
                if string[i:j] in dict: #Check sub string is in dictionary
                    numOfWord[j] = numOfWord[i]+1
    
    #Return number of word in string, if string can be reconstituted.Otherwise return -1 
    return numOfWord[len(numOfWord)-1] is not -1


print(isReconstituted("itwasthebestoftimes"))