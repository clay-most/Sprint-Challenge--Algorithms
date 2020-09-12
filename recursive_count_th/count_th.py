'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    wordlen = len(word)
    searchlen = len("th")
    #base if the string we are checking is shorter than the substring we are looking for quit
    if  (wordlen < searchlen):
        return 0
    # if the input from index 0 untill index 2 is the substring we are checking for restart the function minus the two letters we already looked at
    # and increase the count
    if word[0:searchlen] == "th":
        return count_th(word[searchlen-1:])+1
    
    # else restart the code without increasing the count
    return count_th(word[searchlen-1:])