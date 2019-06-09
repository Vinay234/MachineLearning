#1) find the mean from list or value
#2) find the median from list or value
#3) find the mode from list or value
#4) find the variance from list or value
#5) find the co-variance from list_x and  list_y
#6) find the normalization from list
#7) find the z-score or z-value or z-standard from list#

def insertion_sort_asc(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    return arr
#1
def mean(x):
    sum=0
    for i in x:
        sum+=i
    return sum/len(x)

def duplicate(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    return d
#2
def median(x):
    x=insertion_sort_asc(x)
    median=0
    n=len(x)
    if n%2==0:
        median=(x[n//2]+n[n//2-1])/2
    else:
        median=x[n//2]

    return median


def largest(arr):
    max=arr[0]


    for i in range(1,len(arr)):

        if max<arr[i]:
            max=arr[i]

    return max
def smallest(arr):
    min=arr[0]


    for i in range(1,len(arr)):

        if min>arr[i]:
            min=arr[i]

    return min
#3
def mode(x):
    dict1=duplicate(x)
    y=list(dict1.values())
    print(y)
    max= largest(y)

    for i in dict1:
        if dict1[i] == max:
            print(str(i)+" ")

#4
def variance(x):
    y=mean(x)

    sum=0
    for i in x:
        sum+=(y-i)**2
    return sum/len(x)
#5
def covariance(x,y):
    mean_x=mean(x)
    mean_y=mean(y)
    sum=0
    for i,j in x,y:
        sum+=(i-mean_x)*(j-mean_y)
    cov=sum/(len(x)-1)
    return cov
#6
def normalize(x):
    x_min=smallest(x)
    x_max=largest(x)
    um=0
    diff=x_max-x_min
    for i in range(0,len(x)):
        x[i]=(x[i]-x_min)/ diff


    return x
#7
def z_score(x):
    mean_X=mean(x)
    sum=0
    for i in x:
        sum+=i-mean_X
    std_dev=variance(x)**.5
    z=sum/std_dev
    return z


list1=[3, 7, 5, 13, 20, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29]
print("mean value is",mean(list1))
print("mode value is ");mode(list1)
print("median value is",median(list1))
print("variance is ",variance(list1))
#print("std deviation is ",covariance())
print("normalized value of the list are as follows:",normalize(list1))
print("z score is ",z_score(list1))