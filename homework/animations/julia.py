import matplotlib.pyplot as plt 
import numpy as np
import time

def julia():
    for i in range(10):
        plt.clf()
        add = i / 10
        N = 100
        x = np.arange(-2, 2 + (4/N), 4/N)
        y = np.arange(-2, 2 + (4/N), 4/N)

        it = 20
        
        mag = list()

        start = time.time()
        for b in y:
            mag.append(list())
            for a in x:
                cy = -0.2321 + add
                cx = -0.835 + add
                zx = a
                zy = b
                n = 0
                while n < it:
                    nx = (zx**2) - (zy**2) + cx
                    ny = (2 * zy * zx) + cy
                    if (nx**2) + (ny**2) > 2:
                        mag[-1].append(0)
                        break

                    zy = ny 
                    zx = nx 
                    n+=1

                if n == it:
                    mag[-1].append(it)
        end = time.time()
        print(end - start)
        plt.imshow(mag, extent=[-2, 1, -1, 1])
        plt.pause(0.01)
    plt.show()
    

if __name__ == "__main__":
    julia()