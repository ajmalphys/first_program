''''''
'''Symmetric_difference_update'''
# p={1,2,3}
# q={2,3,4}
# p.symmetric_difference_update(q)
# print(p) #o/p:{1,4}

#shortcut ^=

# p={1,2,3}
# q={2,3,4}
# p^=q
# print(p) #o/p:{1,4}
# print(q) #o/p : {2,3,4}
#------------------------------------------------------
'''isdisjoint()'''
# p={1,2,3}
# q={2,3,4}
# print(p.isdisjoint(q)) #False
#------------------------------------------------------
l={1,3,2}
l.discard(3)
print(l)
l.add(5)
print(l)