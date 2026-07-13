
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

# centroids
cs = [
    [4,0.5],
    [2.5,1.5],
    [2.5,2.75]
]

# new iris_centroids
# the 1st and 2nd elements of each row are sum values
# the 3rd element of each row is the count
cs2 = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# distance function
def dist(v1, v2):
    return math.sqrt( ((v1[0]-v2[0])/6)**2 + ((v1[1]-v2[1])/3)**2 )

# assign instances to their closest centroid
# @param it the iteration number
def assign(it):
    global v, cs, cs2;
    cs2 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    for v in vs:
        dmin = 1000000000
        vc = [0,0]
        i = 0
        for c in cs:
            d = dist(c,v)
            if d <= dmin:
                dmin = d
                vc = c
                ci = i
            i += 1
        # sum and count (so that we can compute new centroids at the end)
        cs2[ci][0] += v[0]
        cs2[ci][1] += v[1]
        cs2[ci][2] += 1
        save(it, ci, v, vc)
        # f.write("{0} {1}\n".format(vc[0],vc[1]))
        # f.write("{0} {1}\n".format(v[0],v[1]))
        # f.write("{0} {1}\n".format(v[0],v[1]))
        # f.write("{0} {1}\n".format(vc[0],vc[1]))
    i = 0

    fc = open("org_kmeans/{0}_c.dat".format(it), "w")
    fc.write("pl pw\n")
    for c2 in cs2:
        f = open("org_kmeans/{0}_c{1}.dat".format(it,i), "w")
        f.write("pl pw\n")
        # current centroid
        f.write("{0} {1}\n".format(cs[i][0], cs[i][1]))
        if c2[2]>0:
            cs[i][0] = c2[0]*1.0/c2[2]
            cs[i][1] = c2[1]*1.0/c2[2]
        # updated centroid
        f.write("{0} {1}\n".format(cs[i][0], cs[i][1]))
        fc.write("{0} {1}\n".format(cs[i][0], cs[i][1]))
        i += 1
        f.close()
    fc.close()

# prepare output data file header
def header(it, ci):
    f = open("org_kmeans/{0}_{1}.dat".format(it, ci), "w")
    f.write("pl pw\n")
    f.close()

def header_all(it):
    for ci in [0,1,2]:
        header(it, ci)

# save data to output file
def save(it, ci, v, vc):
    f = open("org_kmeans/{0}_{1}.dat".format(it, ci), "a")
    # f.write("{0} {1}\n".format(v[0],v[1]))
    f.write("{0} {1}\n".format(vc[0],vc[1]))
    f.write("{0} {1}\n".format(v[0],v[1]))
    f.write("{0} {1}\n".format(v[0],v[1]))
    f.write("{0} {1}\n".format(vc[0],vc[1]))
    f.close()



# run the first iteration
for it in [1,2,3,4,5]:
    header_all(it)
    assign(it)
