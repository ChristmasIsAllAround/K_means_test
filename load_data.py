import numpy as np

dimesion = 2
num_centers = 4
subNumber = 400
mean = [4]*dimesion
means = np.random.multivariate_normal(mean, np.identity(dimesion), (num_centers)) *6


def randData():
    x = np.concatenate([np.random.multivariate_normal(mean, np.identity(dimesion), (subNumber)) for mean in means], axis=0)
    x = x.tolist()
    return x


def EuDis(x, y):
    return np.sqrt(sum([(x[i] - y[i]) ** 2 for i in range(len(x))]))


def labelEqual(x, y):
    sub = [abs(x[i] - y[i]) for i in range(len(x))]
    if sum(sub) == 0:
        return True
    else:
        return False