from utils.node_helper import ListNode


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Reverse linked list
        cur1 = l1
        p1 = None
        while cur1:
            temp = cur1.next
            cur1.next = p1
            p1 = cur1
            cur1 = temp

        cur2 = l2
        p2 = None
        while cur2:
            temp = cur2.next
            cur2.next = p2
            p2 = cur2
            cur2 = temp

        num1 = 0
        while p1:
            num1 = num1 * 10 + p1.val
            p1 = p1.next

        num2 = 0
        while p2:
            num2 = num2 * 10 + p2.val
            p2 = p2.next

        num = num1 + num2
        pre = head = ListNode(0)
        for num in str(num)[::-1]:
            head.next = ListNode(int(num))
            head = head.next
        return pre.next


if __name__ == '__main__':
    s = Solution()
    l1 = head = ListNode(0)
    # 3 -> 2 -> 1 -> 0
    for i in range(4):
        head.next = ListNode(i)
        head = head.next

    l2 = head = ListNode(0)
    # 3 -> 2 -> 1 -> 0
    for i in range(4):
        head.next = ListNode(i)
        head = head.next

    res = s.addTwoNumbers(l1, l2)
    cur = res
    while cur:
        print(cur.val)
        cur = cur.next
