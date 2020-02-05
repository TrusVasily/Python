import sys
from scipy.cluster.hierarchy import dendrogram, average
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

from sklearn.model_selection import train_test_split

sys.setrecursionlimit(10000)

tmp = pd.read_json(r"data.json")

data = tmp[['age', 'countGroups']]
df = pd.DataFrame(data)
df = df[df['age'] != 0]

df.values.tolist()

print(df)


def get_clusters_average():
    x = np.array(df)
    print(len(x))
    linkage_array = average(x)
    print(linkage_array)
    print(len(linkage_array))
    dendrogram(linkage_array)
    ax = plt.gca()
    bounds = ax.get_xbound()
    ax.plot(bounds, [2500, 2500], '--', c='k')
    ax.plot(bounds, [850, 850], '--', c='k')
    ax.text(bounds[1], 2500, ' два кластера', va='center', fontdict={'size': 5})
    ax.text(bounds[1], 850, ' три кластера', va='center', fontdict={'size': 5})
    plt.xlabel("Индекс наблюдения")
    plt.ylabel("Кластерное расстояние")
    plt.xlim(2567, 3000)
    plt.ylim(0, 10)
    plt.show()


def get_linear_regression():
    x = np.array(df['age'])
    y = np.array(df['countGroups'])
    inp = np.array(x).reshape(-1, 1)
    out = np.array(y).reshape(-1, 1)
    x_train, x_test, y_train, y_test = train_test_split(inp, out, test_size=0.33, random_state=0)
    model = linear_model.LinearRegression().fit(x_train, y_train)
    y_pred = model.predict(x_test)

    plt.scatter(x_train, y_train, edgecolor='k')
    plt.scatter(inp, out, edgecolor='k')
    plt.plot(x_train, model.predict(x_train))
    plt.scatter(x_test, y_pred, edgecolor='k')
    plt.show()


def get_correlation():
    x = np.array(data['age']).reshape(-1, 1)
    y = np.array(data['countGroups']).reshape(-1, 1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

    coff = linear_model.LinearRegression()

    coff.fit(x_train, y_train)
    print(coff.score(x_test, y_test))


if __name__ == '__main__':
    get_clusters_average()
    # get_linear_regression()
    # get_correlation()

