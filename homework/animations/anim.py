import matplotlib.pyplot as plt
import numpy as np 
from sklearn.linear_model import LinearRegression
import random

if __name__ == "__main__":
    x = []
    y = []

    reg = LinearRegression()

    for _ in range(100):
        plt.clf() #Clear figure
        x.append(random.randint(0,100))
        y.append(random.randint(0,100))
        
        xnp = np.array(x)
        xnp = xnp.reshape(-1, 1)

        ynp = np.array(y)
        ynp = ynp.reshape(-1, 1)

        reg.fit(xnp, ynp)
        plt.xlim(0,100)
        plt.ylim(0,100)
        plt.scatter(x, y, color='k')
        plt.plot(list(range(100)), reg.predict(np.array([x for x in range(100)]).reshape(-1, 1)))
        plt.pause(0.01)

    plt.show()