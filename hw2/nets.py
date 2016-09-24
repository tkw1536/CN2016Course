def subnet(l):
    for i in range(2**l):
        b = str(bin(i))+('0'*(8-l))
        s = str(int(b, 2))
        print("\item 203.0.113.%s/%s" % (s, 24 + l))

def hosts():
    for i in range(2**7):
        c = str(bin(i))[2:]
        d = ('0'*(7 - len(c))) + c
        b = '0b1'+d
        print(int(b, 2))
