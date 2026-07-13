import math
from pprint import pprint

# training instances / values
vs = [
    # [1, 1, 1],
    [4, 4, 0],
    [2, 2, 1],
    [3, 1, 0],
    [2, 1, 1],
    [1, 3, 0],
    [1, 2, 1],
    [3, 3, 0]
]

# Weights
w = [0,0,0]
wws = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
# w = [1,1,1]
# wws = [
#     [1,1,1],
#     [1,1,0],
#     [1,0,1]
# ]
# w = [1,-1,-1]
# wws = [
#     [1,-1,-1],
#     [-1,1,0],
#     [-1,0,1]
# ]

# hidden output
ss = [1, 0, 0]
h = [1, 0, 0]

# learning rate
r = 1

# Sigmoid
def f(s):
    return 1/(1+math.exp(-s))

# Sigmoid derivative
def fd(s):
    return f(s)*(1-f(s))

# Dot product of two vectors
def dot(a,b):
    if len(a) != len(b):
        return 0
    return sum(i[0]*i[1] for i in zip(a,b))

# First differential
def dw(y,s,si):
    return (f(s) - y) * fd(s) * f(si)

# Second differential
def dww(y,s,si,v):
    return (f(s) - y) * fd(s) * fd(si) * v

# error
e = 0
c = 0

# training process
def train():
    global e, c;
    for vv in vs:
        v = [1, vv[0],vv[1]]
        y = vv[2]
        ww1 = wws[1]
        ww2 = wws[2]
        print("v:")
        pprint(v)
        # pprint(ww1)
        # pprint(ww2)

        h[0] = f(ss[0])
        ss[1] = dot(ww1,v)
        h[1] = f(ss[1])
        ss[2] = dot(ww2,v)
        h[2] = f(ss[2])
        s = dot(w, h)
        yp = f(s)

        e += pow(y - yp,2)/2
        c += 1

        print("h:")
        pprint(h)
        print("w:")
        pprint(w)
        print("s",s)

        # update weights to output
        # print("s, yp, y: ", s, yp, y)
        # print("w0, w1, w2: ", end=" ")
        for i in [0,1,2]:
            dwi = dw(y,s,ss[i])
            w[i] = w[i] - dwi*r
            wws[0][i] = wws[0][i] - dwi * r
        #     print(dwi, end="\t")
        # print("")
        # normalize weights to output
        # nw = w[2]
        # for i in [0,1,2]:
        #     wws[0][i] = wws[0][i]/nw
        #     w[i] = w[i]/nw

        # dw1 = dw(y,s,h[1])
        # dw2 = dw(y,s,h[2])
        # update weights to hidden
        for i in [1,2]:
            # print("ww0, ww1, ww2: ", end=" ")
            for j in [0,1,2]:
                dwwij = dww(y,s,ss[i],v[j])
                wws[i][j] = wws[i][j] - dwwij * r
        #         print(dwwij, end="\t")
        #     print("")
        # print("----------------------------------")
        # normalize weights to hidden
        # nw = wws[2][2]
        # for i in [1,2]:
        #     for j in [0,1,2]:
        #         wws[i][j] = wws[i][j]/nw

        # simplified model without w12 and w21 weights (zero)
        wws[1][2] = 0
        wws[2][1] = 0
        # pprint(w)
        # pprint(wws)
        print("y, yp, error:")
        print(y, yp, y-yp)
        print("----------------------------------")

print("it w0 w1 ww1 w2 ww2 w10 w11 ww11 w12 ww12 w20 w21 ww21 w22 ww22 e")
for i in range(1,2000):
    # training
    e = 0
    c = 0
    train()
    print(i, end=" ")
    for i in [0,1,2]:
        for j in [0,1,2]:
            print(wws[i][j], end=" ")
            if j>0:
                print(wws[i][j]/wws[i][0], end=" ")
    e2 = e/c
    print(e2)
    # print("")
