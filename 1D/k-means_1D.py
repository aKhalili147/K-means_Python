import numpy as np
import random 


arr = [1, 2, 3, 6, 7, 8, 13, 15, 17] # input data
k = 3 # number of clusters

def compare_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        print("error in size!")
    else:
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return True

    return False

def copy_array(arr1,arr2):
    if len(arr1) != len(arr2):
        print("error in size!")
    else:
        for i in range(len(arr1)):
            arr1[i] = arr2[i]

        

def k_means(arr_in,k):
    # pick k random centers initially
    ctrs = random.sample(arr_in,k)

    # or pick with first k points from input data
    # ctrs = [1,2,3]
    
    print("centers at the beginning: "+str(ctrs))
    ctrs2 = np.zeros(k)

    flag = True
    while flag:

        lt_cls = [[] for x in range(k)] # list of clusters

        # filling clusters with points
        for x in arr_in:
            index = min_dist(x,ctrs)
            lt_cls[index].append(x)

        # calculate new centers
        for i in range(len(lt_cls)):
            sum = 0.
            for j in lt_cls[i]:
                sum+=j
            ctrs2[i] = sum/len(lt_cls[i])

        print("centers: "+str(ctrs2))
        print("clusters "+str(lt_cls))

        # to check centers are stable or not
        if compare_arrays(ctrs,ctrs2) == False: 
            return lt_cls
        else:
            copy_array(ctrs,ctrs2)


def min_dist(x,ctrs):
    dist = abs(ctrs[0]-x)
    index = 0
    for i in range(len(ctrs)):
        if dist > (abs(ctrs[i]-x)):
            dist = abs(ctrs[i]-x)
            index = i
    
    return index

k_means(arr,k)
