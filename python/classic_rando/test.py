import sys
print(sys.version)


mergeTwoLists = lambda l1, l2, dummy=ListNode(): (lambda f, dummy: (f(f, dummy, l1, l2), dummy.next)[1])(lambda rec, node, l1, l2: node if not l1 and not l2 else (rec(rec, node.__setattr__('next', l1 if not l2 or (l1 and l1.val < l2.val) else l2) or node.next, l1.next if not l2 or (l1 and l1.val < l2.val) else l1, l2 if not l2 or (l1 and l1.val < l2.val) else l2.next)), dummy)
