
#Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.


if __name__ == '__main__':
    L=[] 
    N = int(input())

for row in range(N): 
    inputs = input().split() 
    if len(inputs)==1: 
        command =inputs[0] 
    if len(inputs)==2: 
        command = inputs[0] 
        e = int(inputs[1]) 
    if len(inputs)==3: 
        command = inputs[0] 
        i = int(inputs[1]) 
        e = int(inputs[2])
    if command=="insert":
        L.insert(i,e)
    elif command=="remove":
        L.remove(e)
    elif command=="append":
         L.append(e)
    elif command=="sort":
         L.sort()
    elif command=="pop":
         L.pop()
    elif command=="reverse":
         L.reverse()
    elif command=="print":
        print(L)
