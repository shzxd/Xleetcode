# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # search题, 数据结构满足查找为O(1)即可，选用set数据结构并不是为了所谓“去重”
        # 而是这里仅需要查找node即可，不需要存储key-value，所以用dict多此一举。
        # 直接使用array的话，会因为查找费时
        # time complexity: O(n)
        # space complexity: O(n)
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

    # def hasCycle(self, head: ListNode) -> bool:
    #     # two pointer, 避开查找，直接判断是否相等
    #     # time complexity: O(n)
    #     # space complexity: O(1)
    #     i = head
    #     if i is None:
    #         return False
    #     j = i.next
    #     while i != j:
    #         if j is None or j.next is None:
    #             return False
    #         i = i.next
    #         j = j.next.next
    #     return True
