def encode(words):
    """ convert the list to a string """
    count = []
    for word in words:
        count.append(len(word))
    s = '@@@'.join(words)
    return s, count


def decode(s, count):
    """ convert the string to a list"""
    words = []
    z = 0
    j = 0
    for i in range(len(count)):
        if i != 0:
            j += 3
        word = ""

        for _ in range(count[z]):
            word += s[j]
            j += 1
        else:
            z += 1
            words.append(word)
    print(words)


x, y = encode(["ibra", "siu", "@@@meow"])
print(x)
print(y)
decode(x, y)

