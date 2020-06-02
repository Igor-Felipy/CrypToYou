def To_crypt(data, crypt, key):
    data = data
    crypt = crypt
    key = key

    if crypt == 'chinese':
        s = ''
        for c in data: s += chr(ord(c)+30000)
        return s
    