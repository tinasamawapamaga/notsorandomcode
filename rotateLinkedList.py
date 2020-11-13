# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if (head == None): 
            return head
        #create temporary node
        tail = head
        l = 1
        while (tail.next != None):
            tail = tail.next
            l+=1
            
        k%=l
        #this line will link the last element 
        #to the first one, making it a ring
        tail.next = head
        l = l - k
        for i in range(l, 0, -1): 
            head = head.next;
            tail = tail.next;
        #return ring list to singly
        #linked list
        tail.next = None
        return head;
