def deosPatternMatch(pattern, string):
    matches = dict() #Define a dictionary for indexing pattern to words
    string = string.lower() #toLower for upper case letters
    return findMatches(pattern,string,matches)

#Helper method that gets substring of string
def getRemainingString(string,fromIndex,toIndex):
    str = ""
    for i in range(fromIndex,toIndex):
        str += string[i]
    return str

def findMatches(pattern, string, matches):
    
    if not string and not pattern: 
        return True
    keyPattern = pattern[0] #Get pattern for using as a key in dictionary
    if keyPattern not in matches: #if pattern is not dictionary add it to dictionary
        for i in range(len(string),0,-1):  
            match = getRemainingString(string,0,i)
            matches[keyPattern] = match      
            if findMatches(pattern[1:], string[len(match):], matches): #Look remaining string recursively
                return True
            else:
                matches.pop(keyPattern)  # Remove word which is indexed by keyPattern from dictionary   
    else:
        value = matches.get(keyPattern)
        otherPartOfString = string[len(value):]
        if value in string[0:len(value)]:# Check whether the string starting with value
            return findMatches(pattern[1:], otherPartOfString, matches) #Look remaining string recursively
        else:
            return False 
    return False

print(deosPatternMatch("abcdab", "Tobeornottobe"))
print(deosPatternMatch("abba", "gototogo"))
print(deosPatternMatch("abab", "xxxyyxxxzz"))