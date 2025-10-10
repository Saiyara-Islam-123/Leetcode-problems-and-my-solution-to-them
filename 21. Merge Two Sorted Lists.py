class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(l):
  if len(l) == 0:
    return None
  head = ListNode(l.pop(0))
  curr = head
  while len(l) > 0:
    curr.next = ListNode(l.pop(0))
    curr = curr.next

  return head

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        curr_1 = list1
        curr_2 = list2
        if curr_1 == None and curr_2 == None:
            return None
        elif curr_1 == None and curr_2 != None:
            return curr_2
        elif curr_1 != None and curr_2 == None:
            return curr_1

        if curr_1.val < curr_2.val:
            merged_head = ListNode(curr_1.val)
            curr_1 = curr_1.next
        else:
            merged_head = ListNode(curr_2.val)
            curr_2 = curr_2.next

        m = merged_head

        while curr_1 is not None and curr_2 is not None:
            if curr_1.val < curr_2.val:
                m.next = ListNode(curr_1.val)
                curr_1 = curr_1.next

            else:
                m.next = ListNode(curr_2.val)
                curr_2 = curr_2.next

            m = m.next

################################################################################################3

        if curr_1 == None and curr_2 == None: #equal length
            return merged_head
        elif curr_1 == None and curr_2 != None: #list 2 is longer
            while curr_2 != None:
                m.next = ListNode(curr_2.val)
                m = m.next
                curr_2 = curr_2.next

            return merged_head
        elif curr_1 != None and curr_2 == None: #list 1 is longer
            while curr_1 != None:
                m.next = ListNode(curr_1.val)
                m = m.next
                curr_1 = curr_1.next
            return merged_head

if __name__ == '__main__':
    l1 = create_linked_list([1,2,4])
    l2 = create_linked_list([1,3,9])
    sol = Solution()
    merged = sol.mergeTwoLists(l1, l2)
