#merge sort

#ascending_oroder
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        Left = arr[:mid]
        Right = arr[mid:]

        merge_sort(Left)
        merge_sort(Right)

        i = j = k = 0
        # initial indices value of arrays to be sorted and a new array
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1

        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1
        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1


arr=[3,9,2,5,90,3,2]
n=len(arr)
merge_sort(arr)
for i in arr:
    print(i)