def encode(characters, encoding=[]):
    key = [None, 0]
    for i in range(len(characters)):
        if not key[0]:
            key = [characters[i], 1]
        elif key[0] == characters[i]:
            key[1] += 1
        else:
            encoding.append(key)
            key = [characters[i], 1]
    encoding.append(key)
    return encoding

while True:
    compressable_text = list(input("Enter text to be compressed! \n:"))
    print(" ".join([str(i[0])+" "+str(i[1]) for i in encode(compressable_text)]))
