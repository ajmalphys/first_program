''''''
'''Qn 1: create a file with numbers. use python program to read from the file
add the numbers into a list, 
print the list
also find the sum of the list'''

# f=open('C:/Users/hp/PycharmProjects/first_program/8_File_Handling_Dir2/Ex_1','r')
# l=[]
# sum=0
# for i in f:
#     l.append(i)
#     sum+=int(i)
# print(l)
# print(sum)
#output
# ['101\n', '102\n', '103\n', '104\n', '105\n'] \n represents a new line
# 515

'''----------------------to change the backward slash to forward-----------------------------'''
# p=r'C:\Users\hp\PycharmProjects\first_program\8_File_Handling_Dir2\Ex_1'
# o=p.replace('\\','/')
# print(o)
'''------------------------------------------------------------------------------'''

# f=open('C:/Users/hp/PycharmProjects/first_program/8_File_Handling_Dir2/Ex_1','r')
# l=[]
# sum=0
# for i in f:
#    l.append(int(i))
# print(l) #[101, 102, 103, 104, 105]

# f=open('C:/Users/hp/PycharmProjects/first_program/8_File_Handling_Dir2/Ex_1','r')
# l=[]
# sum=0
# for i in f:
#    l.append(i.rstrip('\n'))
# print(l) #['101', '102', '103', '104', '105']
# for i in l:
#     sum+=int(i)
# print(sum) #515

'''Qn 2: copy a paragraph from somewhere
find the word count in that paragraph'''

s=r'C:\Users\hp\PycharmProjects\first_program\8_File_Handling_Dir2\r_ex_2'
p=s.replace('\\','/')
print(p)
f=open(p,'r')
# l=[]
# l2=[]
# for i in f:
#     print(i)
#     l.append(i.rstrip('\n'))
# print(l)
# for i in l:
#     for j in i:
#         l2.append(j)
# print(l2)
# d={}
# for i in l2:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)------------------------i did the letter count. do word count
# dic={}
# for i in f:
#     data=i.split()
#     for j in data:
#         if j not in dic:
#             dic[j]=1
#         else:
#             dic[j]+=1
# print(dic)


x=('key1','key2','key3')
y=0
thisdict=dict.
print(thisdict)

