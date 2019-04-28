# https://www.geeksforgeeks.org/selection-sort/
# complexity O(n^2)


def selectionSort(arr):
    i = 0
    for i in range(0,len(arr)):
        minIndex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        tmp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = tmp
    return



# Driver Code
print "Provide the input array :"
arr = map(int, raw_input().split(" "))
selectionSort(arr)
print "Array in sorted order : "
for x in arr:
    print x,
