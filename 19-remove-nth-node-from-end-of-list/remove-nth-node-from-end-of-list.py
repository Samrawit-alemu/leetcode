# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            # prev = curr
            curr = curr.next
        
        L = len(arr)
        to_be_removed = L - n

        curr = head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        index = 0
        while curr:
            if index == to_be_removed:
                prev.next = curr.next
                break
            index += 1
            prev = curr
            curr = curr.next

        return dummy.next
