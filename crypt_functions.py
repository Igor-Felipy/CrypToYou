def To_crypt(data, crypt, key):

    if crypt == 'chinese':
        s = ''
        for c in data: s += chr(ord(c)+30000)
        return s
    