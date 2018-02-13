import matplotlib.pylab as plt
import numpy as np

w1 = np.array([[0.2, 0.2, 0.2], [0.4, 0.4, 0.4], [0.6, 0.6, 0.6]])
w2 = np.zeros((1, 3))
w2[0,:] = np.array([0.5, 0.5, 0.5])

b1 = np.array([0.8, 0.8, 0.8])
b2 = np.array([0.2])

w = [w1, w2]
b = [b1, b2]

x = [1.5, 2.0, 3.0]

def f(x):
    return 1 / (1 + np.exp(-x))


def simple_looped_nn_calc(n_layers, x, w, b):
    for l in range(n_layers - 1):
        if (l == 0):
            node_in = x
        else:
            node_in = h

        h = np.zeros(w[l].shape[0],)
        for i in range(w[l].shape[0]):
            f_sum = 0
            for j in range(w[l].shape[1]):
                f_sum += w[l][i][j] * node_in[j]

            f_sum += b[l][i]
            h[i] = f(f_sum)
    return h

def matrix_feed_forward_calc(n_layers, x, w, b):
    for l in range(n_layers - 1):
        if (l == 0):
            node_in = x
        else:
            node_in = h

        z = w[l].dot(node_in) + b[l]
        h = f(z)
    return h


def df(x):
    y = 4 * x**3 - 9 * x**2
    return y

def grad():
    x_old = 0
    x_new = 6
    gamma = 0.01
    precision = 0.00001

    while (abs(x_new - x_old) > precision):
        x_old = x_new
        x_new += -gamma * df(x_old)
    return x_new

def read_text_file(filename):
    fileptr = open(filename)
    for line in fileptr:
        print(line)
    fileptr.close()
    return


print("looped h = %f" % simple_looped_nn_calc(3, x, w, b))

print("matrix h = %f" % matrix_feed_forward_calc(3, x, w, b))

print("The local minimum occurs at %f" % grad())

read_text_file('D:\MachineLearning\Python\cntkex1\cntkex1\cntklstm.py')
