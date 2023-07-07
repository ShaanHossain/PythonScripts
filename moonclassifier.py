import sklearn
from sklearn.linear_model import LogisticRegression
import numpy as np




X = [
    [1, 2],
    [2, 4],
    [3, 6],
    [4, 8]
]

y = [1, 4, 9, 16]

clr = LogisticRegression() 
clr.fit(X, y)
print(clr.predict([1, 2]))