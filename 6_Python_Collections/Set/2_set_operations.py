''''''
'''
1--union---combines two different sets
2--intersection---retains the common elements
3--difference---retains the values in a set by ignoring the values in the other set(including the common ones) see example.
'''

# s1={1,2,3,4,5,6}
# s2={4,5,6,7,8,9}
#
'''------union()------'''
# print(s1.union(s2)) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
'''-------intersection()-------------------'''
# print(s1.intersection(s2)) #{4,5,6}
'''----------difference()-----------------'''
# print(s1.difference(s2)) #{1,2,3} those in set 1 and not in s2
# print(s2.difference(s1)) #{8, 9, 7} those in set 2 and not in s1
# l=list(s1) # let me try to convert those set to list
# print(l) #[1, 2, 3, 4, 5, 6]
# s3=set(l) #again trying to convert this to list
# print(s3) #{1, 2, 3, 4, 5, 6}
'''converting a tuple to set'''
# t=(1,2,3,4)
# s=set(t)
# print(s) #{1, 2, 3, 4}
# u=tuple(s) #converting the set to a tuple
# print(u) #(1, 2, 3, 4)

