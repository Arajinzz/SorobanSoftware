def swap(x, y):
    return y, x


def genKey(x):

        X = x.split("-")

        X[0], X[1] = swap(X[0], X[1])
        X[0], X[len(X)-1] = swap(X[0], X[len(X)-1])

        key = ''

        for s in X:
                for c in s:
                        key += str(c)
                        c = ord(c)
                        c = ((c % 2)*10 + (c))
                        c = hex(c)
                        c = c.replace("0x","")
                        key += c

        return key


info = open("key", "r")
info = info.readlines()
info = info[2]
info = info.replace("\n","")
key = genKey(info)

print(key)