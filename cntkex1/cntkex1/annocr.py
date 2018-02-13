from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


X_scale = StandardScaler()

digits = load_digits()
print(digits.data.shape)
print(digits.data[0,:])

X = X_scale.fit_transform(digits.data)
print(X[0,:])

y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4)


import matplotlib.pyplot as plt
plt.gray()
plt.matshow(digits.images[1])
plt.show()

