# https://www.geeksforgeeks.org/exponential-search/
# complexity O(log n)

def eponentialSearch(input, elemToFind):
    i = 0
    while i < len(input):
        if input[i] == elemToFind:
            return i
        elif input[i] > elemToFind:
            break
        else:
            if i == 0:
                i = min(1, len(input))
            else:
                i = min(i*2, len(input))
    high = i
    low = i/2

    while high >= low:
        mid = (high + low) / 2
        if input[mid] == elemToFind:
            return mid
        elif input[mid] > elemToFind:
            high = mid - 1
        else:
            low = mid + 1
    return -1



# Driver Code
input = map(int, raw_input().split(" "))
elem = int(raw_input())
res = eponentialSearch(input, elem)
print "ExponentialSearch approach Soln: "
if res == -1:
    print "Element is not present in the array"
else:
    print "Element is present at index - ", res
