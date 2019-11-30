def find_key(d,val):
    keys = []
    for key, val_  in d.items():
        if val_ == val :
            keys.append(key)
    return keys[0]

def isValid(s):

    char_count = {}
    occurence_count = {}
    #Counting chars 
    for char in s :
        char_count[char] = s.count(char)
    for occur in char_count.values():
        occurence_count[occur] = list(char_count.values()).count(occur)

    
    print(char_count)
    print(occurence_count)

    if len(occurence_count) == 1 :
        print(1)
        return 'YES'
    if len(occurence_count) > 2 :
        print(2)
        return 'NO'
    if len(occurence_count) == 2 :
        if find_key(occurence_count, min(occurence_count.values())) - 1 == find_key(occurence_count, max(occurence_count.values())) :
            print(3)
            return 'YES'
        if find_key(occurence_count, max(occurence_count.values())) + 1 == find_key(occurence_count, min(occurence_count.values())) :
            print(4)
            return 'YES'
        if (find_key(occurence_count, min(occurence_count.values()))) == 1 and (min(occurence_count.values) == 1):
            print(5)
            return 'YES'
    return 'NO'