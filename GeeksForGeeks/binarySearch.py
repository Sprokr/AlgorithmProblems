# https://www.geeksforgeeks.org/binary-search/
# complexity O(log n)

def binarySearchIterative(input, elemToFind):
    high = len(input) - 1
    low = 0
    while high >= low:
        mid = (high + low) / 2
        if input[mid] == elemToFind:
            return mid
        elif input[mid] > elemToFind:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binarySearchRecursive(input, low, high, elemToFind):
    if high < low:
        return -1
    mid = (high + low) / 2
    if input[mid] == elemToFind:
        return mid
    elif input[mid] > elemToFind:
        return binarySearchRecursive(input, low, mid - 1, elemToFind)
    else:
        return binarySearchRecursive(input, mid + 1, high, elemToFind)

    return


# Driver Code
input = map(int, raw_input().split(" "))
elem = int(raw_input())
res = binarySearchIterative(input, elem)
print "Iterative approach Soln: "
if res == -1:
    print "Element is not present in the array"
else:
    print "Element is present at index - ", res

res = binarySearchRecursive(input, 0, len(input)-1, elem)
print "Recursive approach Soln: "
if res == -1:
    print "Element is not present in the array"
else:
    print "Element is present at index - ", res
