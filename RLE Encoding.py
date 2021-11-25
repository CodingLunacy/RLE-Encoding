# Python 3.8.3
def encode(characters: str, encoding:"previous-encoding"=[]) -> str:
    """Intakes a string, and compresses using RLE encoding returning a list.
    
    Parameters
    ----------
    characters: str
        The string which you wish to compress
    encoding: list
        Previous encoding of the function
        
    Returns
    -------
    list:
        A 2D list, which includes [character, occurences]
        for each compressed character
        
    """
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

if __name__ == "__main__":
    while True:
        compressable_text = list(input("Enter text to be compressed! \n:"))
        print(" ".join([str(i[0])+" "+str(i[1]) for i in encode(compressable_text)]))
