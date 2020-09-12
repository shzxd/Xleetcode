def addTwoNumbers(l1, l2):
    p = 0
    # style 1
    n = ListNode(0)
    ans = n
    # style 2
    # ans = n = ListNode(0)
    while l1 or l2 or p:
        if l1:
            p += l1.val
            l1 = l1.next
        if l2:
            p += l2.val
            l2 = l2.next
        p, val = divmod(p, 10)
        # style 1
        n.next = ListNode(val)
        n = n.next
        # style 2
        # n.next = n = ListNode(val)
    return ans.next
    
