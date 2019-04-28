# https://www.geeksforgeeks.org/bubble-sort/
# complexity avg and worst case - O(n^2), best case - O(n)


def bubbleSort(arr):

    for i in range(0,len(arr)-1):
        didSwap = False
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                didSwap = True
        if didSwap == False:
            break

    return



# Driver Code
print "Provide the input array :"
arr = map(int, raw_input().split(" "))
bubbleSort(arr)
print "Array in sorted order : "
for x in arr:
    print x,
