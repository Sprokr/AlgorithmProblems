# https://www.geeksforgeeks.org/insertion-sort/
# complexity - O(n^2)


def insertionSort(arr):

    for i in range(0,len(arr)):

        for j in range(0, i):
            if arr[j] > arr[i]:
                tmpLast = arr[i]
                tmpPrev = arr[j]
                for k in range(j+1, i+1):
                    tmp = arr[k]
                    arr[k] = tmpPrev
                    tmpPrev = tmp

                arr[j] = tmpLast
                break

    return



# Driver Code
print "Provide the input array :"
arr = map(int, raw_input().split(" "))
insertionSort(arr)
print "Array in sorted order : "
for x in arr:
    print x,
