
import math
from pprint import pprint

# training instances / values
vs = [
    [1.4, 0.2, 0],
    [1.6, 0.4, 0],
    [1.3, 0.3, 0],
    [1.7, 0.2, 0],
    [1.7, 0.5, 0],
    [4.7, 1.4, 1],
    [4.5, 1.5, 1],
    [4.9, 1.5, 1],
    [4.0, 1.3, 1],
    [4.6, 1.5, 1],
    [6.0, 2.5, 2],
    [5.9, 2.1, 2],
    [5.8, 2.2, 2],
    [6.1, 2.3, 2],
    [5.4, 2.3, 2]
]

# pcvs
# a row for each instance v
# a column for each cluster c
pcvs = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# parameter values
# each row is a cluster
# 1st column is mean (mu)
# 2nd column is deviation (delta)
ps = [
    [1.0,0.25],
    [1.6,0.25],
    [2.8,0.25]
]

# prioir probability for each cluster
pcs = [1.0/3.0, 1.0/3.0, 1.0/3.0]

# normal density function
def f(u, d, v):
    # print(u, d, v)
    # \frac{1}{\sqrt{2\pi\delta_c}} e^{-\frac{(v-\mu_c)^2}{2\delta_c^2}}
    return 1/(math.sqrt(2*math.pi*d**2)) * math.exp(-(v-u)**2/(2*d**2))

# probability of cluster c membership given data v
def pvc(v, c):
    p = ps[c]
    u = p[0]
    d = p[1]
    return f(u,d,v)

# the overall probability of data v
# as the weighted sum of its association with the clusters
def pv(v):
    sum = 0
    for c in [0,1,2]:
        pc = pcs[c]
        w = pc * pvc(v,c)
        sum += w
        # print("\t pc {0} * pvc {1}) => w {2}".format(pc, pvc(v,c), w))
    # print("\t pv sum: {0}".format(sum))
    return sum

# probability of data v given c cluster
def pcv(c, v):
    pc = pcs[c]
    # print("\t pc {0}: {1}".format(c, pc))
    # print("\t pvc({0},{1}): {2}".format(v, c, pvc(v, c)))
    return pvc(v,c) * pc / pv(v)

# expectation computing for each instance
def expect(i):
    v = vs[i][1]    # only on second value for petal width
    for c in [0,1,2]:
        # print("pcv({0},{1}): {2}".format(c, v, pcv(c, v)))
        pcvs[i][c] = pcv(c, v)

# compute expectation for all data instances
def expect_all():
    for i in range(0,15):
        expect(i)

# compute the new mean
# based on all data instances vs (global)
# and cluster index c
def mean(c):
    global vs
    n_sum = 0
    d_sum = 0
    for i in range(0,15):
        v = vs[i][1]
        pcv = pcvs[i][c]
        nw = v * pcv
        dw = pcv
        n_sum += nw
        d_sum += dw
    return n_sum / d_sum

# compute the new deviation
def dev(c, u):
    global vs
    n_sum = 0
    d_sum = 0
    for i in range(0,15):
        v = vs[i][1]
        pcv = pcvs[i][c]
        nw = ((v - u)**2) * pcv
        dw = pcv
        n_sum += nw
        d_sum += dw
    return math.sqrt(n_sum / d_sum)


# execute the program
def iterate():
    expect_all()
    print("P(c|v) values: ")
    pprint(pcvs)
    # update parameters
    for c in [0,1,2]:
        u = mean(c)
        d = dev(c,u)
        ps[c][0] = u
        ps[c][1] = d
    print("Updated parameters: ")
    pprint(ps)

for i in [1,2,3,4,5]:
    print("Iteration {0}".format(i))
    print("=================================================")
    iterate()
    print("=================================================")
    print()
