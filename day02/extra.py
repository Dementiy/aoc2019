import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression


if __name__ == '__main__':
    df = pd.read_table(sys.argv[1], delimiter=' ', header=None, names=['noun', 'verb', 'output'])
    X, y = df[['noun', 'verb']], df.output
    model = LinearRegression()
    model.fit(X, y)
    print(model.coef_, model.intercept_)
    print(model.predict(np.array([[51, 21]])))

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(df.noun, df.verb, df.output)
    plt.show()
