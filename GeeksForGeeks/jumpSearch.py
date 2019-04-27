# https://www.geeksforgeeks.org/jump-search/
# complexity O(Root(n))

import math

def jumpSearch(input, elemToFind):
    stepSize = int(math.sqrt(len(input)))

    currIndex = 0
    while currIndex < len(input):
        if input[currIndex] == elemToFind:
            return currIndex
        elif input[currIndex] < elemToFind:
            currIndex += stepSize
        else:
            currIndex = currIndex - stepSize + 1
            break
    limitToSearch = min(currIndex + stepSize-1, len(input))
    while currIndex < limitToSearch:
        if input[currIndex] == elemToFind:
            return currIndex
        else:
            currIndex += 1
    return -1



# Driver Code
input = map(int, raw_input().split(" "))
elem = int(raw_input())
res = jumpSearch(input, elem)
print "jumpSearch  approach Soln: "
if res == -1:
    print "Element is not present in the array"
else:
    print "Element is present at index - ", res
