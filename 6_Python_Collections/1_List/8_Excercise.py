''''''

'''1. Shopping Cart 🛒------------------------------------------------------------------------------------------

Task:
Start with an empty cart.
Keep asking the user to add items until they type "done".
Finally, display all the added items.

Sample Input:

Enter item: apple  
Enter item: milk  
Enter item: chips  
Enter item: done

Expected Output:

Items in your cart: ['apple', 'milk', 'chips']'''

# cart=[]
# status=False
# while status==False:
#     item=input('Enter item : ')
#     if item=='done':
#         status=True
#     else:
#         cart.append(item)
# print('Items in your cart : ',cart)

'''
2. Favorite Movies 🎬---------------------------------------------------------------------------------------
Task:
Given list = ["Inception", "Titanic", "Avatar", "Interstellar", "Joker"]
Add one new movie.-----------1
Remove one movie you no longer like.----2
Insert a new movie in between.---------3
Show final list.-----------4
Sample Execution:----------------5
Original List: ['Inception', 'Titanic', 'Avatar', 'Interstellar', 'Joker']
After adding: ['Inception', 'Titanic', 'Avatar', 'Interstellar', 'Joker', 'Oppenheimer']
After removing 'Titanic': ['Inception', 'Avatar', 'Interstellar', 'Joker', 'Oppenheimer']
After inserting 'Shutter Island' at position 2: ['Inception', 'Avatar', 'Shutter Island', 'Interstellar', 'Joker', 'Oppenheimer']

Expected Output:
Updated Movie List: ['Inception', 'Avatar', 'Shutter Island', 'Interstellar', 'Joker', 'Oppenheimer']
---
'''
# list = ["Inception", "Titanic", "Avatar", "Interstellar", "Joker"]
# #adding a new movie
# list.append('oppenheimer')
#
# #removing a movie that i dont like
# list.remove('Titanic')
#
# #insert 'shutter island' at position 2
# list.insert(1,'Shutter Island')
#
# print('Updated movie list : ',list)

'''
3. Student Marks 📘--------------------------------------------------------------------------------

Given:
marks = [45, 78, 56, 89, 90]

Steps:
1. Sort in ascending order.
2. Display highest and lowest.
3. Remove lowest and show updated list.

Expected Output:

Sorted Marks: [45, 56, 78, 89, 90]
Highest: 90
Lowest: 45
After removing lowest: [56, 78, 89, 90]
'''
# marks=[45,78,56,89,90]
# #sort in ascending order
# print(marks)
# marks.sort() #need to explicitly mention this in a line, cannot be included inside a print statement, it doesnt work then.
# print('Ascending order : ', marks)
# #Display highest and lowest
# print('Highest entry : ',max(marks))
# print('Lowest entry : ', min(marks))
# #remove lowest and show updated list
# marks.remove(min(marks))
# print('List except the lowest value : ', marks)
'''
4. Grocery List 🥦--------------------------------------------------------------------------------------------

Given:
-----groceries = ["milk", "bread", "eggs"]----------
Steps:
1---Add 3 more items: "butter", "rice", "tea".
2---Remove one bought item "bread".
3---Show final list.
--Expected Output:--
Final Grocery List: ['milk', 'eggs', 'butter', 'rice', 'tea']
'''
# gro=['milk','bread','eggs']
# add=['butter','rice','tea']
# gro.extend(add)
# print(gro)
# gro.remove('bread')
# print('removing bread: ',gro)

'''
5. Friend List 👯----------------------------------------------------------------------------------------------

Task:
Keep adding names until "stop" is typed.
Then check how many times a given name appears and show its position(s).

Sample Input:

Enter name: Rahul  
Enter name: Neha  
Enter name: Rahul  
Enter name: Arya  
Enter name: stop  
Enter name to search: Rahul

Expected Output:

Rahul appears 2 times at positions [0, 2]
'''
# lst=[]
# while True:
#     n=input('Enter name: ')
#     if n!='stop':
#         lst.append(n)
#     else:
#         break
# print(lst)
# s=input('Enter the name to search : ')
# count=0 # to count the repetitions
# p=[] #list to store index values
# l=len(lst)
# for i in range(l):
#     if s==lst[i]:
#         count+=1
#         p.append(i)
#     else:
#         continue
# print(f'{s} appears {count} times at positions {p}')

'''
6. Music Playlist 🎧--------------------------------------------------------------------------------------------

Given:
playlist = ["song1", "song2", "song3"]
Steps:
1--Add "intro_song" at the top.
2--Remove "song2".
3--Add "outro_song" at the end.
Expected Output:

Final Playlist: ['intro_song', 'song1', 'song3', 'outro_song']
'''

# playlist=['song1','song2','song3']
# playlist.insert(0,'intro_song')
# playlist.remove('song2')
# playlist.append('outro_song')
# print(playlist)

'''
7. Restaurant Orders 🍔-----------------------------------------------------------------------------------------

Task:
1---Take orders continuously.
2---When chef completes one, remove it.
3---When all done, print message.

Sample Execution:

1--Orders received: ['Burger', 'Pasta', 'Pizza']
2--Chef completed: Burger
3--Chef completed: Pasta
4--Chef completed: Pizza
5--All orders served!

Expected Output:

All orders served!
'''
# lst=[] #list to take order
# while True:
#     o=input('Enter the item : ')
#     if o!='stop':
#         lst.append(o)
#     else:
#         break
# print(f'Orders recieved : {lst}')
# l=len(lst)
# while l>0:
#     for i in lst:
#         c=input(f'Whether {i} is finished? (y/n) : ')
#         if c=='y':
#             lst.remove(i)
#             print(f'Items remining to finish : {lst}')
#             l-=1
#             print('Chef completed : ',i)
#         else:
#             continue
# print('All orders served')

'''
8. Numbers List 🔢------------------------------------------------------------------------------------------

Given:
numbers = [10, 20, 30, 40, 50]

Steps:
1--Find sum, largest, smallest.
2--Empty the list.

---Expected Output:---
Total: 150
Largest: 50
Smallest: 10
After clearing: []
'''

# n=[10,20,30,40,50]
# print(f'sum of {n} is : {sum(n)}')
# print(f'largest entry in {n} is : {max(n)}')
# print(f'Smallest entry in {n} is : {min(n)}')
# n.clear()
# print(f'Emptying the list {n}')

'''
9. Attendance Sheet 👩‍🏫------------------------------------------------------------------------------------------

Given:
students = ["Anu", "Rahul", "Meera", "Arya", "Jithin"]

Input:

Absent students: ["Rahul", "Arya"]

Expected Output:

Present Students: ['Anu', 'Meera', 'Jithin']
'''

# students = ["Anu", "Rahul", "Meera", "Arya", "Jithin"]
# while True:
#     n=input('Enter the name of absent student : ')
#     if n!='stop':
#         students.remove(n)
#     else:
#         break
# print(f'Present students: {students}')

'''
10. Product Inventory 🏪 -----------------------------------------------------------------------------------------

Given:
products = ["pen", "pencil", "eraser", "notebook"]

****** Case 1 – Product exists: *******

1--Enter product to search: pencil
2--Output: 'pencil' found at position 1

****** Case 2 – Product not found: *****

1--Enter product to search: marker
2--Output: Product not found. Added to list.
Updated Product List: ['pen', 'pencil', 'eraser', 'notebook', 'marker']
'''

# p=["pen", "pencil", "eraser", "notebook"]
# while True:
#     n=input('press Enter to start & type stop to terminate : ')
#     if n!='stop':
#         s=input('Enter an item to search : ')
#         if s in p:
#             print(f'{s} found at position {p.index(s)} ')
#         else:
#             p.append(s)
#             print('Product not found, Added to the list')
#             print(f'Updated product list : {p}')
#     else:
#         break


