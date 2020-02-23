def remdup(l):
    lis = []
    for n in l:
        if n not in lis:
            lis.append(n)
    return lis


def sumsquare(l):
    lise = []
    e, o = 0, 0
    for i in range(0, len(l)):
        if l[i]%2 == 0:
            e = e + l[i]**2
        else:
            o = o + l[i]**2
    lise.append(o)
    lise.append(e)
    return lise


def transpose(m):
    return [list(x) for x in zip(*m)]