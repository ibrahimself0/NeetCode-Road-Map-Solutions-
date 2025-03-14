def encode(words):
    """ convert the list to a string """
    count = [0]
    for word in words:
        count.append(len(word))
    s = '@@@'.join(words)
    return s, count


def decode(s, count):
    """ convert the string to a list"""
    words = []
    for i in range(len(count)-1):
        if i == 0:
            words.append(s[0: count[i + 1]])
        else:
            words.append(s[count[i]+3: count[i + 1] + i*3])
    print(words)


x, y = encode(["ibra", "siuu@@@"])
print(x)
print(y)
decode(x, y)