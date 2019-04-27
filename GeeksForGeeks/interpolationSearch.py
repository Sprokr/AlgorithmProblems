# https://www.geeksforgeeks.org/interpolation-search/
# Time complexity Best case - O(loglog n), Worst Case - O(n)

def interpolationSearchIterative(input, elemToFind):
    high = len(input) - 1
    low = 0
    while high >= low:
        mid = low + int((float((elemToFind - input[low]) * (high - low))) / (input[high] - input[low]))
        if input[mid] == elemToFind:
            return mid
        elif input[mid] > elemToFind:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def interpolationSearchRecursive(input, low, high, elemToFind):
    if high < low:
        return -1
    mid = low + int((float((elemToFind - input[low]) * (high - low))) / (input[high] - input[low]))
    if input[mid] == elemToFind:
        return mid
    elif input[mid] > elemToFind:
        return interpolationSearchRecursive(input, low, mid - 1, elemToFind)
    else:
        return interpolationSearchRecursive(input, mid + 1, high, elemToFind)

    return


# Driver Code
input = map(int, raw_input().split(" "))
elem = int(raw_input())
res = interpolationSearchIterative(input, elem)
print "Iterative approach Soln: "
if res == -1:
    print "Element is not present in the array"
else:
    print "Element is present at index - ", res

res = interpolationSearchRecursive(input, 0, len(input) - 1, elem)
print "Recursive approach Soln: "
if res == -1:
    print "Element is not present in the array"
else:
    print "Element is present at index - ", res
