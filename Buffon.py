import numpy as np
import matplotlib.pyplot as plt

def MethBM() :
    s = 0
    while s == 0 or s >= 1 :
        x = np.random.uniform(-1.0, 1.0)
        y = np.random.uniform(-1.0, 1.0)
        s = np.sqrt(x**2 + y**2)
    q = np.sqrt((-2*np.log(s**2))/s**2)
    return x*q, y*q

def Buffon(n, L, d, a) :
    if a >= l :
        raise "Necessaire : a < l"
    k = 0
    for i in range(0, n) :
        # On genere le point du centre
        x = np.random.uniform(-(d-a), d-a)
        y = np.random.uniform(-(d-a), d-a)
        # On genere son orientation
        xp, yp = MethBM()
        phi = np.tan(yp/xp)
        # On trouve sa position selon les fentes
        m = np.floor(x/L)
        # On recupere sa position r
        r = np.min([x - m*L, (m+1)*L - x])
        # On verifie sa position
        #ay = a*np.sin(phi)/2
        ax= a*np.cos(phi)/2
        if r == 0 :
            k += 1
        elif x + ax < (m + 1)*L and x - ax > m*L :
            pass
        else :
            k += 1
            
    return 2*n*a/(l*k), k, (k/n)*100

l = 3
a = 2
d = 9
n = 10000
pi = []
g, h, j = [], 0, 0
for j in range(0, 100) :
    f, h, j = Buffon(n, l, d, a)
    g.append(f)
    print(f, h, j)

print()
print(np.mean(g), np.mean(g)*100/np.pi)