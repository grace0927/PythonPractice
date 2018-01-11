m = [9, 15, 24]

def modify(k):
    k.append(39)
    print("k =", k)

def replace(g):
    g = [17, 28, 45]
    print("g =", g)

def replace_contents(g):
    g[0] = 17
    g[1] = 28
    g[2] = 45

modify(m)
replace(m)
replace_contents(m)
