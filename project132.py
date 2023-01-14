import csv
import matplotlib.pyplot as plt
import seaborn as sns
mass = []
radius = []
gravitydata = []

rows = []
def calgravity(x,y):
    return  6.67*(x/y^2)

with open("data.csv","r")as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        row.append(row)


massdata = rows[3]

Radius = rows[6]

massdatakg = massdata* 1.989e+30
raduismeters = Radius*6.957e+8

for i in massdata[0]:
    calgravity(massdata[i],Radius[i])

X = []

for index, massdata in enumerate(massdata):
    temp_list = [
        radius[index],
        massdata
    ]
    X.append(temp_list)
    
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++',random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,7))



