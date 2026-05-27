''''''
'''Find the prime numbers in given range of numbers (say 11 to 50)'''
# l=int(input('Enter the lower limit : '))
# u=int(input('Enter the upper limit : '))
# for i in range(l,u+1):
#     count=0
#     for j in range(2,i+1):
#         if i%j==0:
#             count+=1
#         else:
#             continue
#     if count==1:
#         print(i,end=' ')


'''Find the count of prime numbers in a given range'''

# l=int(input('Enter the lower limit : '))
# u=int(input('Enter the upper limit : '))
# count_1=0
# for i in range(l,u+1):
#     count = 0
#     for j in range(2,i+1):
#         if i%j==0:
#             count+=1
#         else:
#             continue
#     if count==1:
#         count_1+=1
# print('The number of prime nos in the given range are : ',count_1)



'''find the sum of prime numbers in a given range'''

# l=int(input('Enter the lower limit : '))
# u=int(input('Enter the upper limit : '))
# sum=0
# for i in range(l,u+1):
#     count=0
#     for j in range(2,i+1):
#         if i%j==0:
#             count+=1
#         else:
#             continue
#     if count==1:
#         sum+=i
# print(f'Sum of prime nos in the range {l} to {u} is {sum}')


'''Print first N prime numbers'''
# n=int(input('Enter the limit : '))  #this pgm doesnt prints the first N nos, instead till the given limit
# if n==1:
#     print('Invalid input')
# else:
#     for i in range(2,n+1):
#         count=0
#         for j in range(2,i+1):
#             if i%j==0:
#                 count+=1
#             else:
#                 continue
#         if count==1:
#             print(i,end=' ')

# n=int(input('Enter the required number of terms : '))
# total_count=0
# i=2
# while total_count<n:
#     count=0
#     j=2
#     while j<=i:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count==1:
#         print(i,end=' ')
#         total_count += 1
#     i+=1


'''
    *
   ***
  *****
 *******
*********
'''

# for i in range(6):
#     for j in range(6-i):
#         print(' ',end='')
#     for k in range((2*i)-1):
#         print('*',end='')
#     print()

'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
#
# for i in range(6):
#     for j in range(5-i):
#         print(' ',end='')
#     for j in range(2*i-1):
#         print('*',end='')
#     print()
# for i in range(4,0,-1):
#     for j in range(5-i):
#         print('',end=' ')
#     for k in range(2*i-1):
#         print('*',end='')
#     print()


'''fibonacci'''
# n=12
# a=0
# b=1
# print(a,b,end=' ')
# for i in range(3,n+1):
#     c=a+b
#     print(c,end=' ')
#     a=b
#     b=c

'''prime nos'''
'''program to check whether the given number is prime or not'''
# n=int(input('Enter a number : '))
# count=0
# for i in range(2,n+1):
#     if n%i==0:
#         count+=1
#     else:
#         continue
# if count==1:
#     print('its a prime number')
# else:
#     print('Not a prime number')


'''
     *
    * *
   * * *
  * * * *
 * * * * * 

'''

# for i in range(1,6):
#     for j in range(5-i):
#         print(' ',end='')
#     for j in range(2*i-1):
#         print('*',end='')
#     print()
# for k in range(1,5):
#     for l in range(k):
#         print(' ',end='')
#     for m in range(2*(5-k)-1):
#         print('*',end='')
#     print()

'''
    *
   ***
  *****
 *******
*********
'''