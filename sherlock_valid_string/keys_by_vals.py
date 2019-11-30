def find_key(d,val):
    keys = []
    for key, val_  in d.items():
        if val_ == val :
            keys.append(key)

    return keys
