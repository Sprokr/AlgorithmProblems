# https://www.geeksforgeeks.org/merge-sort/
# complexity - O(nlogn)


def merge(arr, l, m, r):
    i = l
    j = m+1
    tmpArr = []
    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            tmpArr.append(arr[i])
            i += 1
        else:
            tmpArr.append(arr[j])
            j += 1
    while i <= m:
        tmpArr.append(arr[i])
        i += 1
    while j <= r:
        tmpArr.append(arr[j])
        j += 1
    j = l
    for i in range(0, len(tmpArr)):
        arr[j] = tmpArr[i]
        j += 1
    return

def mergeSort(arr, l, r):
    if r > l:
        m = (l+r)/2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr,l,m,r)
    return




# Driver Code
print "Provide the input array :"
arr = map(int, raw_input().split(" "))
mergeSort(arr,0,len(arr)-1)
print "Array in sorted order : "
for x in arr:
    print x,

