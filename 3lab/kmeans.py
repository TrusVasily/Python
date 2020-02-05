from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

tmp = pd.read_json(r"data.json")

data = tmp[['photo', 'age']]
df = pd.DataFrame(data)
df = df[df['age'] != 0]

kmeans = KMeans(n_clusters=3)
kmeans.fit(df)
plt.scatter(df['age'], df['photo'], cmap='rainbow', c=kmeans.labels_, alpha=0.7, edgecolor='k')
plt.xlim(10, 130)
plt.ylim(0, 43000)
plt.xlabel("Age")
plt.ylabel("Count Photos")
plt.show()

kmeans = KMeans(n_clusters=5)
kmeans.fit(df)
plt.scatter(df['age'], df['photo'], cmap='rainbow', c=kmeans.labels_, alpha=0.7, edgecolor='k')
plt.xlim(10, 130)
plt.ylim(0, 43000)
plt.xlabel("Age")
plt.ylabel("Count Photos")
plt.show()

kmeans = KMeans(n_clusters=7)
kmeans.fit(df)
plt.scatter(df['age'], df['photo'], cmap='rainbow', c=kmeans.labels_, alpha=0.7, edgecolor='k')
plt.xlim(10, 130)
plt.ylim(0, 43000)
plt.xlabel("Age")
plt.ylabel("Count Photos")
plt.show()


data = tmp[['countVideo', 'age']]
df = pd.DataFrame(data)
df = df[df['age'] != 0]

kmeans = KMeans(n_clusters=3)
kmeans.fit(df)
plt.scatter(df['age'], df['countVideo'], cmap='rainbow', c=kmeans.labels_, alpha=0.7, edgecolor='k')
plt.xlim(10, 120)
plt.ylim(0, 10000)
plt.xlabel("Age")
plt.ylabel("Count Videos")
plt.show()

kmeans = KMeans(n_clusters=5)
kmeans.fit(df)
plt.scatter(df['age'], df['countVideo'], cmap='rainbow', c=kmeans.labels_, alpha=0.7, edgecolor='k')
plt.xlim(10, 120)
plt.ylim(0, 10000)
plt.xlabel("Age")
plt.ylabel("Count Videos")
plt.show()

kmeans = KMeans(n_clusters=7)
kmeans.fit(df)
plt.scatter(df['age'], df['countVideo'], cmap='rainbow', c=kmeans.labels_, alpha=0.7, edgecolor='k')
plt.xlim(10, 120)
plt.ylim(0, 10000)
plt.xlabel("Age")
plt.ylabel("Count Videos")
plt.show()


data = tmp[['countNotes', 'age']]
df = pd.DataFrame(data)
df = df[df['age'] != 0]

kmeans = KMeans(n_clusters=3)
kmeans.fit(df)
plt.scatter(df['age'], df['countNotes'], cmap='rainbow', c=kmeans.labels_, alpha=0.7, edgecolor='k')
plt.xlim(10, 120)
plt.ylim(0, 10)
plt.xlabel("Age")
plt.ylabel("Count Notes")
plt.show()

kmeans = KMeans(n_clusters=5)
kmeans.fit(df)
plt.scatter(df['age'], df['countNotes'], cmap='rainbow', c=kmeans.labels_, alpha=0.7, edgecolor='k')
plt.xlim(10, 120)
plt.ylim(0, 10)
plt.xlabel("Age")
plt.ylabel("Count Notes")
plt.show()

kmeans = KMeans(n_clusters=7)
kmeans.fit(df)
plt.scatter(df['age'], df['countNotes'], cmap='rainbow', c=kmeans.labels_, alpha=0.7, edgecolor='k')
plt.xlim(10, 120)
plt.ylim(0, 10)
plt.xlabel("Age")
plt.ylabel("Count Notes")
plt.show()

data = tmp[['countGroups', 'age']]
df = pd.DataFrame(data)
df = df[df['age'] != 0]

kmeans = KMeans(n_clusters=3)
kmeans.fit(df)
plt.scatter(df['age'], df['countGroups'], cmap='rainbow', c=kmeans.labels_, alpha=0.7, edgecolor='k')
plt.xlim(10, 120)
plt.ylim(0, 5500)
plt.xlabel("Age")
plt.ylabel("Count Groups")
plt.show()

kmeans = KMeans(n_clusters=5)
kmeans.fit(df)
plt.scatter(df['age'], df['countGroups'], cmap='rainbow', c=kmeans.labels_, alpha=0.7, edgecolor='k')
plt.xlim(10, 120)
plt.ylim(0, 5500)
plt.xlabel("Age")
plt.ylabel("Count Groups")
plt.show()

kmeans = KMeans(n_clusters=7)
kmeans.fit(df)
plt.scatter(df['age'], df['countGroups'], cmap='rainbow', c=kmeans.labels_, alpha=0.7, edgecolor='k')
plt.xlim(10, 120)
plt.ylim(0, 5500)
plt.xlabel("Age")
plt.ylabel("Count Groups")
plt.show()