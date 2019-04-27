# https://www.geeksforgeeks.org/linear-search/


def linearSearch(input, elemToFind):
    for i in range(0,len(input)):
        if input[i] == elemToFind:
            return i
    return -1


# Driver Code
input = map(int, raw_input().split(" "))
elem = int(raw_input())
print linearSearch(input, elem)



