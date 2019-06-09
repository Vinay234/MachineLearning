# insertion sort
# start with element at i= and place that element in sorted sequence from  to n-1

#sorting ascending a number
def insertion_sort_asc(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp

def bubble_sort(arr):
    for i in range(0,len(arr)):
        for j in range(1,len(arr)):
            if arr[j-1]>arr[j]:
                temp=arr[j]
                arr[j-1],arr[j]=temp,arr[j-1]


def selection_sort_desc(arr):
    #finds by repeatedly finding the minimum part
    for i in range(len(arr)):
        max_index=i
        for j in range(i+1,len(arr)):

            if arr[j]>arr[max_index]:
                max_index=j
        arr[i],arr[max_index]=arr[max_index],arr[i]




print(insertion_sort_asc([3, 9, 2, 5, 90, 3, 2]))
arr=[3, 9, 2, 5, 90, 3, 2]
insertion_sort_asc(arr)

print(arr)
arr=[3, 9, 2, 5, 90, 3, 2]
bubble_sort(arr)
print(arr)
arr=[3, 9, 2, 5, 90, 3, 2]
selection_sort_desc(arr)
print(arr)