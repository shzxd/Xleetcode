# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # iteration, 维护三个节点，一个指向前节点，一个指向现节点，一个指向后节点
        # 保存后节点，断开现节点链结到前节点，更新前节点为现节点，更新现节点为后节点
        # 直到现节点为None时，原链表翻转完毕，此刻的前节点即为新链表的头结点
        # time complexity: O(n)
        # space complexity: O(1)
        prev = None
        curr = head
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        return prev

    # def reverseList(self, head: ListNode) -> ListNode:
    #     # recursion, 如果当前节点是tail或输入是None则原样返回即可。
    #     # 否则翻转一条链表只需将当前节点next的链表翻转，然后将当前节点指向None(作为tail）即可。
    #     # time complexity: O(n)
    #     # space complexity: O(n)
    #     if head is None or head.next is None:
    #         return head
    #     reversedlist = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return reversedlist
