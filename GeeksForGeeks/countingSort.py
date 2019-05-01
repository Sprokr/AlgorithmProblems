# https://www.geeksforgeeks.org/counting-sort/
# complexity - O(n)


def countingSort(arr):
    mx = max(arr)
    mn = min(arr)
    countArr = [0]*(mx-mn+1)
    for i in range(0,len(arr)):
        countArr[arr[i]-mn] += 1
    j = 0
    for i in range(0, len(countArr)):
        while countArr[i] > 0:
            arr[j] = i+mn
            countArr[i] -= 1
            j += 1

    return




# Driver Code
print "Provide the input array :"
arr = map(int, raw_input().split(" "))
countingSort(arr)
print "Array in sorted order : "
for x in arr:
    print x,
