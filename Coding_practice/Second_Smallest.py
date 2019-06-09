
#second smallest and duplicate removal

def second_smallest(arr):
    min=arr[0]

    second_min=min
    for i in range(1,len(arr)):

        if min>arr[i]:
            second_min=min
            min=arr[i]

        elif second_min>arr[i] and arr[i]!=min:
            second_min=arr[i]
    print(second_min)




arr = [3, 9, 2, 5, 90, 3,24, 2]
second_smallest(arr)






def second_largest(arr):
    max=arr[0]

    second_max=max
    for i in range(1,len(arr)):

        if max<arr[i]:
            second_max=max
            max=arr[i]

        elif second_max<arr[i] and arr[i]!=max:
            second_min=arr[i]
    print(second_max)
    print("max element is ",max)



arr = [3, 9,12, 5, 90, 3, 92]
second_largest(arr)


def duplicate(arr):
        d = {}
        for i in arr:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        return d



        array=d.keys()
        print(array)


arr=[1, 9, 2, 3, 4, 6, 8, 1, 2, 3, 6]
duplicate(arr)
arr=[5,4,6,1,1,1,2,1,2,3]
duplicate(arr)



def reverse_list(list3):
    n=len(list3)-1
    list2=[]
    while n >= 0:
        list2.append(list3[n])
        n-=1
    print(list2)

list1 =["b" ,"a","c","d"]
list3=["a" ,"a","r","d" ]
print(reverse_list(list3))



def remove_duplicates(list1):

    dict1={}
    for i in range(len(list1)):
        dict1[list1[i]]=+1


    print(dict1.keys())
    return dict1.keys()



abc=["b" ,"a","c","d","a","c","k"]
remove_duplicates(abc)
d=["a" ,"a","r","d","r"]
remove_duplicates(d)





