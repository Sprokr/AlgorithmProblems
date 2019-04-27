# https://www.geeksforgeeks.org/linear-search/
# complexity O(n)

def linearSearch(input, elemToFind):
    for i in range(0,len(input)):
        if input[i] == elemToFind:
            return i
    return -1


# Driver Code
input = map(int, raw_input().split(" "))
elem = int(raw_input())
res = linearSearch(input, elem)
if res == -1:
    print "Element is not present in the array"
else:
    print "Element is present at index - ", res





