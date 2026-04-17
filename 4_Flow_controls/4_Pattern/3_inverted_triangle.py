''''''
'''
12345
1234
123
12
1
'''

# for i in range(6,1,-1): #-1 kodthillenkil program run aavilla
#     for j in range(1,i):
#         print(j,end=' ')
#     print()

'''
11111
2222
333
44
5
'''
# k=1
# for i in range(6,1,-1):
#     for j in range(1,i):
#         print(k,end=' ')
#     print()
#     k+=1

# for i in range(1,6):
#     for j in range(6-i):
#         print(i,end=' ')
#     print()

# for i in range(1,6):
#     for j in range(i,6):
#         print(i,end=' ')
#     print()
'''
55555
4444
333
22
1
'''
# for i in range(5,0,-1):
#     for j in range(i):
#         print(i,end=' ')
#     print()

# k=5
# for i in range(6,1,-1):
#     for j in range (i-1):
#         print(k,end=' ')
#     print()
#     k-=1

'''
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
'''

for i in range(6,1,-1): #6-5-4-3-2-1-0
    for j in range(i):
        print(j,end=' ')
    print()

'''
# 0 
# 0 1
# 0 2 4
# 0 3 6 9
'''
k=0
for i in range(1,5):
    for j in range(i):
        print(j*k,end=' ')
    k+=1
    print()

'''
# 1 
# 2  3 
# 4  5  6 
# 7  8  9  10
# 11 12 13 14 15
'''
k=1
for i in range(6):
    for j in range(i):
        print(k,end=' ')
        k+=1
    print()

'''
# 1 2 3 4 5 
# 2 2 3 4 5 
# 3 3 3 4 5 
# 4 4 4 4 5 
# 5 5 5 5 5
'''

for i in range(1,6):
    for j in range(i):
        print(i,end=' ')
    for k in range(5-i):
        print(k+i+1,end=' ')

    print()

'''
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1
# 5 4 3 2 1
'''
for i in range(1,6):
    k=i
    for j in range(i):
        print(k,end=' ')
        k-=1
    print()
