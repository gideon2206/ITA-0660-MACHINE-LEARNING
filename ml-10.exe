data = [2,4,10,12,3,20,30,11,25]

mean1 = 4
mean2 = 20

for k in range(3):

    cluster1 = []
    cluster2 = []

    for x in data:
        if abs(x-mean1) < abs(x-mean2):
            cluster1.append(x)
        else:
            cluster2.append(x)

    mean1 = sum(cluster1)/len(cluster1)
    mean2 = sum(cluster2)/len(cluster2)

print("Cluster 1:", cluster1)
print("Mean 1:", mean1)

print("\nCluster 2:", cluster2)
print("Mean 2:", mean2)
