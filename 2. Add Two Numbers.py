# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        r = (l1.val + l2.val)%10
        carry = (l1.val + l2.val)//10
        result = ListNode(r)
        l1 = l1.next
        l2 = l2.next
        current = result
        while l1 is not None and l2 is not None:
            r = (l1.val + l2.val+carry) % 10
            carry = (l1.val + l2.val+carry) // 10
            new = ListNode(r)
            current.next = new
            current = new
            l1 = l1.next
            l2 = l2.next

        if l1 is None and l2 is not None:

                while l2 is not None:
                    new = ListNode((l2.val + carry)%10)
                    current.next = new
                    carry =  (l2.val + carry)//10
                    current = new
                    l2 = l2.next

        elif l2 is None and l1 is not None:

                while l1 is not None:
                    new = ListNode((l1.val + carry) % 10)
                    current.next = new
                    carry = (l1.val + carry) // 10
                    current = new
                    l1 = l1.next


        if l1 is None and l2 is None and carry > 0:
            new = ListNode(carry)
            current.next = new

        return result

if __name__ == '__main__':


    l1 = ListNode(9)
    l2 = ListNode(1)
    l3 = ListNode(6)
    l4 = ListNode(0)
    l1.next = l2
    l2.next = l3

    print(Solution().addTwoNumbers(l1, l4).val)

    
