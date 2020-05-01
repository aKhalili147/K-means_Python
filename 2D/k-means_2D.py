import matplotlib.pyplot as plt
import numpy as np
import random
import csv 
import math

points = []
# csv to multi_dimensional list
with open("iris.csv",'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # point = []
        # point.append(float(row[0])) # x coordinate
        # point.append(float(row[1])) # y coordinate
        points.append([float(row[2]),float(row[3])])


def compare_centers(centers1, centers2):
    if len(centers1) != len(centers2):
        print("error in size!")
    else:
        for i in range(len(centers1)):
            for j in range(len(centers1[i])):
                if centers1[i][j] != centers2[i][j]:
                    return True

    return False

def copy_array(centers1,centers2):
    if len(centers1) != len(centers2):
        print("error in size!")
    else:
        for i in range(len(centers1)):
            centers1[i] = centers2[i]

        

def k_means(arr_in,k):
    # pick k random centers initially
    ctrs = random.sample(arr_in,k)
    # print("centers at the beginning: "+str(ctrs))
    
    ctrs2 = random.sample(arr_in,k)

    while True:

        lt_cls = [[] for x in range(k)] # list of clusters

        # filling clusters with points
        for x in arr_in:
            index = min_dist(x,ctrs)
            lt_cls[index].append(x)

        # calculate new centers
        for i in range(len(lt_cls)):
            sum_x, sum_y = 0.,0.
            for point in lt_cls[i]:
                sum_x+=point[0]
                sum_y+=point[1]
            ctrs2[i][0], ctrs2[i][1] = sum_x/len(lt_cls[i]), sum_y/len(lt_cls[i])

        # print("centers: "+str(ctrs2))
        # print("clusters "+str(lt_cls))

        # to check centers are stable or not
        if compare_centers(ctrs,ctrs2) == False: 
            return lt_cls
        else:
            copy_array(ctrs,ctrs2)


def min_dist(x,ctrs):
    dist = math.sqrt(math.pow(ctrs[0][0]-x[0],2)+math.pow(ctrs[0][1]-x[1],2))
    index = 0
    for i in range(len(ctrs)):
        if dist > math.sqrt(math.pow(ctrs[i][0]-x[0],2)+math.pow(ctrs[i][1]-x[1],2)):
            dist = math.sqrt(math.pow(ctrs[i][0]-x[0],2)+math.pow(ctrs[i][1]-x[1],2))
            index = i
    
    return index


clusters = k_means(points,k=3)

colormap = ['r','g','b']
cnt = 0
for cluster in clusters:
    X,Y = [],[]
    for point in cluster:
        X.append(point[0])
        Y.append(point[1])

    plt.scatter(X,Y,c=colormap[cnt])
    cnt+=1

plt.title('K-means clustering Irish dataset')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.show()