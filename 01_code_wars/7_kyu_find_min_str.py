# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    q = min(len(i) for i in s.split())
    
    return q

find_short("fdgfdg dfgdf   123fg g ")