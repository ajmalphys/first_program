''''''

'''from the given external file, use it to find the following qns'''
f=open(r'E:\Datascience\customer1.txt','r')

'''Qn:1
1. Dancer prof, fname, lname, age'''

# for i in f:
#     data=i.split(',')
#     if data[4]=='Dancer':
#         print(data[1:4])
'''------output-----------'''
# ['Franklin', 'Vick', '28']
# ['Kurt', 'Cassidy', '32']
# ['Danny', 'Byrne', '51']
# ['Ronnie', 'Atkins', '67']
# ['Lawrence', 'Miles', '74']
# ['Max', 'Robinson', '32']
# ['Tracy', 'Cates', '54']
# ['Christina', 'Morris', '56']
# ['Paige', 'Henson', '61']

'''Qn:2'''
'''2 Age above 50 fname, lname, age, prof'''

# for i in f:
#     data=i.split(',')
#     if int(data[3])>50:
#         print(data[1:5])
'''----------output---------------'''
# ['Kristina', 'Chung', '55', 'Pilot']
# ['Paige', 'Chen', '74', 'Teacher']
# ['Gretchen', 'Hill', '66', 'Computer hardware engineer']
# ['Karen', 'Puckett', '74', 'Lawyer']
# ['Hazel', 'Bender', '63', 'Carpenter']
# ['Dolores', 'McLaughlin', '60', 'Writer']
# ['Beth', 'Woodard', '65', 'Musician']
# ['Jerome', 'Wallace', '52', 'Pharmacist']
# ['Neal', 'Lawrence', '72', 'Computer support specialist']
# ['Kristine', 'Dougherty', '63', 'Financial analyst']
# ['Crystal', 'Powers', '67', 'Engineering technician']
# ['Eric', 'Steele', '66', 'Doctor']
# ['Marcia', 'Walsh', '64', 'Accountant']
# ['Neal', 'Middleton', '59', 'Civil engineer']
# ['Tim', 'Watts', '58', 'Lawyer']
# ['Beth', 'Walton', '73', 'Firefighter']
# ['Donald', 'Chung', '65', 'Computer hardware engineer']
# ['Paul', 'Woods', '63', 'Doctor']
# ['Patricia', 'Mangum', '67', 'Civil engineer']
# ['Darlene', 'Barton', '54', 'Doctor']
# ['Harvey', 'Underwood', '70', 'Engineering technician']
# ['William', 'Jones', '53', 'Photographer']
# ['Frederick', 'Baker', '52', 'Writer']
# ['Jason', 'Cross', '56', 'Civil engineer']
# ['Don', 'Sharpe', '53', 'Social worker']
# ['Evan', 'Grant', '66', 'Agricultural and food scientist']
# ['Calvin', 'Diaz', '65', 'Athlete']
# ['Eugene', 'Graham', '52', 'Police officer']
# ['Vickie', 'Watkins', '55', 'Computer support specialist']
# ['Luis', 'Hinton', '69', 'Childcare worker']
# ['Allan', 'Marsh', '67', 'Athlete']
# ['Marianne', 'Branch', '53', 'Judge']
# ['Arlene', 'Case', '62', 'Musician']
# ['Calvin', 'Christensen', '54', 'Architect']
# ['Gary', 'Parks', '65', 'Pharmacist']
# ['Gladys', 'Davidson', '52', 'Recreation and fitness worker']
# ['Faye', 'Sparks', '61', 'Civil engineer']
# ['Steve', 'Graves', '73', 'Nurse']
# ['Alison', 'Scarborough', '66', 'Designer']
# ['Sherri', 'Sutton', '75', 'Social worker']
# ['Kelly', 'Bowman', '69', 'Childcare worker']
# ['Dana', 'McLean', '61', 'Artist']
# ['Jennifer', 'Christian', '54', 'Human resources assistant']
# ['Ronnie', 'Cowan', '71', 'Photographer']
# ['Gene', 'Bowling', '73', 'Recreation and fitness worker']
# ['Louise', 'Beasley', '54', 'Loan officer']
# ['Patricia', 'Abrams', '51', 'Veterinarian']
# ['Mary', 'Morse', '70', 'Automotive mechanic']
# ['Danny', 'Davidson', '70', 'Agricultural and food scientist']
# ['Alice', 'Blanchard', '73', 'Economist']
# ['Joan', 'McAllister', '73', 'Engineering technician']
# ['Danny', 'Byrne', '51', 'Dancer']
# ['Peggy', 'Schroeder', '61', 'Loan officer']
# ['Sara', 'Perkins', '67', 'Actor']
# ['Jack', 'Palmer', '52', 'Human resources assistant']
# ['Benjamin', 'Rowe', '64', 'Childcare worker']
# ['Patricia', 'Hodge', '59', 'Artist']
# ['Clifford', 'Li', '63', 'Photographer']
# ['Martin', 'Justice', '58', 'Electrician']
# ['Beth', 'Willis', '62', 'Carpenter']
# ['Jessica', 'Hester', '72', 'Civil engineer']
# ['Samantha', 'Floyd', '72', 'Childcare worker']
# ['Jimmy', 'Graves', '69', 'Nurse']
# ['Dianne', 'Norman', '68', 'Veterinarian']
# ['Sidney', 'Lane', '54', 'Statistician']
# ['Jeff', 'Kaplan', '70', 'Chemist']
# ['Sandra', 'Heller', '51', 'Photographer']
# ['Raymond', 'Jennings', '63', 'Coach']
# ['Kathy', 'Holloway', '65', 'Pharmacist']
# ['Troy', 'Jones', '74', 'Secretary']
# ['Jack', "O'Donnell", '59', 'Actor']
# ['Tamara', 'Stone', '73', 'Firefighter']
# ['Mitchell', 'McClure', '68', 'Loan officer']
# ['Franklin', 'Watson', '64', 'Coach']
# ['Leroy', 'Monroe', '51', 'Computer support specialist']
# ['Judith', 'Singer', '73', 'Actor']
# ['Kathleen', 'Lucas', '66', 'Chemist']
# ['Amy', 'Norman', '62', 'Automotive mechanic']
# ['Ronnie', 'Atkins', '67', 'Dancer']
# ['Pauline', 'Chandler', '70', 'Economist']
# ['Peggy', 'Hobbs', '69', 'Musician']
# ['Donna', 'Adkins', '72', 'Electrical engineer']
# ['Ryan', 'Conner', '51', 'Electrical engineer']
# ['Tracey', 'Waters', '73', 'Computer hardware engineer']
# ['Sarah', 'Fox', '73', 'Psychologist']
# ['Gladys', 'Hatcher', '62', 'Musician']
# ['Hazel', 'Wu', '68', 'Therapist']
# ['Vincent', 'Welch', '54', 'Psychologist']
# ['Joseph', 'Chappell', '59', 'Reporter']
# ['Eric', 'Kane', '61', 'Childcare worker']
# ['Heather', 'Butler', '67', 'Farmer']
# ['Claire', 'Pickett', '59', 'Lawyer']
# ['Michele', 'Bowman', '54', 'Computer software engineer']
# ['Clyde', 'Thornton', '70', 'Pharmacist']
# ['Timothy', 'McNeill', '70', 'Librarian']
# ['Billie', 'Moss', '65', 'Photographer']
# ['Katharine', 'Lucas', '67', 'Electrician']
# ['Lester', 'Rich', '53', 'Human resources assistant']
# ['Louis', 'Harvey', '72', 'Financial analyst']
# ['Charlene', 'Stevenson', '65', 'Carpenter']
# ['Sheryl', 'Dunn', '71', 'Civil engineer']
# ['Ben', 'West', '64', 'Electrician']
# ['Sarah', 'Barr', '52', 'Therapist']
# ['Dana', 'Cain', '63', 'Human resources assistant']
# ['Rebecca', 'Heath', '74', 'Environmental scientist']
# ['Glen', 'Olsen', '63', 'Childcare worker']
# ['Don', 'Pittman', '70', 'Designer']
# ['Gregory', 'Weiner', '58', 'Accountant']
# ['Randy', 'Petersen', '71', 'Actor']
# ['Edna', 'Coleman', '58', 'Veterinarian']
# ['Faye', 'Norman', '64', 'Pilot']
# ['Marvin', 'Parrott', '67', 'Doctor']
# ['Alex', 'Henry', '67', 'Police officer']
# ['Karl', 'McLean', '69', 'Photographer']
# ['Melinda', 'Weeks', '59', 'Computer software engineer']
# ['Robert', 'Puckett', '56', 'Physicist']
# ['Edna', 'Hoyle', '74', 'Electrical engineer']
# ['Clifford', 'Garrett', '72', 'Veterinarian']
# ['Penny', 'Neal', '59', 'Veterinarian']
# ['Glenda', 'Baker', '52', 'Economist']
# ['Arthur', 'Goldman', '58', 'Childcare worker']
# ['Wesley', 'Shaffer', '58', 'Farmer']
# ['Jeremy', 'House', '61', 'Pilot']
# ['Wesley', 'Moser', '64', 'Doctor']
# ['Lucy', 'Dickinson', '72', 'Loan officer']
# ['Susan', 'Abbott', '65', 'Actor']
# ['Monica', 'Dodson', '58', 'africa\n']
# ['Justin', 'Spencer', '67', 'Economist']
# ['Margaret', 'Burgess', '74', 'Social worker']
# ['Philip', 'Liu', '59', 'Nurse']
# ['Miriam', 'Blackburn', '52', 'Athlete']
# ['Christopher', 'McKay', '67', 'Judge']
# ['Stacy', 'Frazier', '69', 'Designer']
# ['Brian', 'Braswell', '64', 'Chemist']
# ['Juan', 'Steele', '57', 'Nurse']
# ['Leroy', 'Donovan', '74', 'Photographer']
# ['Alice', 'Nance', '59', 'Pilot']
# ['Adam', 'Washington', '54', 'Electrical engineer']
# ['Angela', 'McMahon', '66', 'Secretary']
# ['Lawrence', 'Miles', '74', 'Dancer']
# ['Valerie', 'Jennings', '59', 'Loan officer']
# ['Meredith', 'Bowles', '62', 'Accountant']
# ['Jan', 'Brown', '58', 'Secretary']
# ['Allen', 'Craven', '64', 'Therapist']
# ['Ian', 'Nichols', '57', 'Electrician']
# ['Donna', 'Lehman', '71', 'Social worker']
# ['Nancy', 'Sullivan', '70', 'Electrical engineer']
# ['Lloyd', 'Mack', '67', 'Recreation and fitness worker']
# ['Wendy', 'Cherry', '70', 'Loan officer']
# ['Lucille', 'Richmond', '70', 'Photographer']
# ['Virginia', 'York', '67', 'Politician']
# ['Marc', 'Harrington', '57', 'Physicist']
# ['Geoffrey', 'Reed', '53', 'Reporter']
# ['Todd', 'Wilkerson', '55', 'Librarian']
# ['Erin', 'Finch', '54', 'Police officer']
# ['Melinda', 'Starr', '57', 'Statistician']
# ['Julie', 'Holland', '61', 'Architect']
# ['Karen', 'Clements', '74', 'Farmer']
# ['Raymond', 'Hawley', '66', 'Recreation and fitness worker']
# ['Julie', 'Skinner', '56', 'Electrical engineer']
# ['Luis', 'Turner', '69', 'Computer software engineer']
# ['Brent', 'Byrne', '62', 'Judge']
# ['Sharon', 'Mayer', '70', 'Statistician']
# ['Annie', 'Haynes', '51', 'Social worker']
# ['Ruth', 'Harmon', '75', 'Artist']
# ['Michelle', 'Matthews', '67', 'Computer software engineer']
# ['Jane', 'Barefoot', '53', 'Accountant']
# ['Lee', 'Pope', '55', 'Statistician']
# ['Keith', 'Schwartz', '65', 'Childcare worker']
# ['Jim', 'Singleton', '55', 'Accountant']
# ['Steven', 'Ballard', '62', 'Pilot']
# ['Pauline', 'Spivey', '55', 'Computer hardware engineer']
# ['Marc', 'Denton', '71', 'Musician']
# ['Claude', 'Berger', '51', 'Electrical engineer']
# ['Catherine', 'Garcia', '69', 'Athlete']
# ['Lewis', 'Currin', '73', 'Farmer']
# ['Ernest', 'Stanton', '51', 'Lawyer']
# ['Vivian', 'Carey', '64', 'Statistician']
# ['Kay', 'Hess', '56', 'Childcare worker']
# ['Vicki', 'Mills', '56', 'Computer support specialist']
# ['Alvin', 'McDonald', '73', 'Musician']
# ['Jacob', 'Moore', '64', 'Environmental scientist']
# ['Holly', 'Fox', '74', 'Physicist']
# ['Audrey', 'Lanier', '54', 'Human resources assistant']
# ['Joseph', 'Underwood', '57', 'Reporter']
# ['Nicholas', 'Vaughn', '66', 'Carpenter']
# ['Ben', 'Banks', '60', 'Accountant']
# ['Harriet', 'Rubin', '71', 'Real estate agent']
# ['Barry', 'Maynard', '53', 'Pharmacist']
# ['Jerome', 'Hill', '66', 'Computer hardware engineer']
# ['Jason', 'Livingston', '67', 'Civil engineer']
# ['Norman', 'Lam', '63', 'Teacher']
# ['Tim', 'Starr', '59', 'Photographer']
# ['Eddie', 'Barbour', '61', 'Athlete']
# ['Arnold', 'Burke', '70', 'Reporter']
# ['Peter', 'Rosenberg', '60', 'Politician']
# ['Jean', 'Garrett', '73', 'Doctor']
# ['Tracy', 'Cates', '54', 'Dancer']
# ['Holly', 'McIntosh', '73', 'Computer software engineer']
# ['Emma', 'Olson', '74', 'Pilot']
# ['Molly', 'Cox', '55', 'Social worker']
# ['Carlos', 'Erickson', '63', 'Statistician']
# ['Betsy', 'Chang', '54', 'Designer']
# ['Eileen', 'Goldberg', '57', 'Therapist']
# ['Randall', 'Hinson', '51', 'Judge']
# ['Kelly', 'Weiss', '72', 'Librarian']
# ['Leo', 'Lassiter', '65', 'Pilot']
# ['Clarence', 'Massey', '74', 'Politician']
# ['Jordan', 'Dunlap', '59', 'Agricultural and food scientist']
# ['Jordan', 'Horowitz', '58', 'Actor']
# ['Dawn', 'Lutz', '66', 'Therapist']
# ['Jessica', 'Teague', '72', 'Firefighter']
# ['Regina', 'Ellington', '52', 'Social worker']
# ['Joyce', 'Jennings', '61', 'Social worker']
# ['Toni', 'Lynn', '67', 'Civil engineer']
# ['Betty', 'Albright', '64', 'Engineering technician']
# ['Tommy', 'Burnette', '72', 'Doctor']
# ['Alan', "O'Neal", '59', 'Pilot']
# ['Christina', 'Morris', '56', 'Dancer']
# ['Marcus', 'Harvey', '62', 'Computer support specialist']
# ['Carrie', 'Watson', '52', 'Musician']
# ['Paige', 'Henson', '61', 'Dancer']
# ['Jay', 'Wang', '64', 'Carpenter']
# ['Sue', 'Ellis', '59', 'Environmental scientist']
# ['Nelson', 'Pierce', '69', 'Actor']
# ['Nicholas', 'Godfrey', '69', 'Environmental scientist']
# ['Matthew', 'Stanton', '51', 'Secretary']
# ['Thomas', 'Fuller', '51', 'Childcare worker']
# ['Benjamin', 'Simmons', '70', 'Veterinarian']
# ['Kristine', 'Schultz', '66', 'Architect']
# ['Jordan', 'Knight', '65', 'Electrician']
# ['Kim', 'Hensley', '64', 'Photographer']
# ['Deborah', 'French', '56', 'Accountant']
# ['Gretchen', 'Francis', '60', 'Politician']
# ['Wayne', 'Weiner', '70', 'Actor']

'''Qn:3'''
'''3 Age range 25 to 40 (including 25 and 40) fname, lname, age, prof'''

# for i in f:
#     data=i.split(',')
#     age=int(data[3])
#     if age<=40 and age>=25:
#         print(data[1:5])
'''------output----------------'''
# ['Sherri', 'Melton', '34', 'Firefighter']
# ['Malcolm', 'Wagner', '39', 'Artist']
# ['Sandy', 'Raynor', '26', 'Writer']
# ['Alex', 'May', '39', 'Environmental scientist']
# ['Franklin', 'Vick', '28', 'Dancer']
# ['Marian', 'Solomon', '27', 'Lawyer']
# ['Wayne', 'Connolly', '40', 'Real estate agent']
# ['Jerome', 'Johnston', '38', 'Childcare worker']
# ['Shelley', 'Weeks', '25', 'Reporter']
# ['Priscilla', 'Wilkerson', '35', 'Agricultural and food scientist']
# ['Elsie', 'Barton', '27', 'Childcare worker']
# ['Erica', 'Hall', '33', 'Police officer']
# ['Douglas', 'Ross', '27', 'Secretary']
# ['Louis', 'Rosenthal', '31', 'Economist']
# ['Gretchen', 'Holmes', '39', 'Childcare worker']
# ['Glenda', 'Morgan', '37', 'Real estate agent']
# ['Scott', 'Hoyle', '40', 'Doctor']
# ['Jessica', 'Rich', '37', 'Actor']
# ['Melinda', 'Proctor', '27', 'Teacher']
# ['Kyle', 'Watts', '39', 'Engineering technician']
# ['Samantha', 'Hardin', '27', 'Doctor']
# ['Stacy', 'Eason', '31', 'Musician']
# ['Mike', 'Whitehead', '26', 'Politician']
# ['Lynne', 'Rose', '36', 'Loan officer']
# ['Ethel', 'Rodgers', '30', 'Librarian']
# ['Stacy', 'Olsen', '25', 'Veterinarian']
# ['Brett', 'Lamb', '39', 'Engineering technician']
# ['Brandon', 'James', '29', 'Musician']
# ['Keith', 'Chandler', '25', 'Coach']
# ['Joann', 'Stout', '32', 'Real estate agent']
# ['Scott', 'Golden', '27', 'Teacher']
# ['Jennifer', 'Tilley', '35', 'Agricultural and food scientist']
# ['Shawn', 'Boykin', '34', 'Photographer']
# ['Vincent', 'Sumner', '31', 'Lawyer']
# ['Kurt', 'Cassidy', '32', 'Dancer']
# ['Charlene', 'Heath', '26', 'Electrician']
# ['Leslie', 'Griffin', '37', 'Photographer']
# ['Martha', 'Robertson', '37', 'Agricultural and food scientist']
# ['Roberta', 'Zhang', '38', 'Statistician']
# ['Joanne', 'Bowling', '35', 'Musician']
# ['Vincent', 'Fischer', '33', 'Statistician']
# ['Rhonda', 'Chan', '34', 'Pharmacist']
# ['Tamara', 'Hunt', '25', 'Psychologist']
# ['Mary', 'Byrd', '34', 'Environmental scientist']
# ['Katie', 'May', '28', 'Recreation and fitness worker']
# ['Natalie', 'Locklear', '37', 'Politician']
# ['Neal', 'Glover', '40', 'Real estate agent']
# ['Martin', 'Vick', '31', 'Physicist']
# ['Beth', 'McKenna', '40', 'Veterinarian']
# ['Glen', 'Abbott', '29', 'Loan officer']
# ['Alice', 'Hall', '33', 'Recreation and fitness worker']
# ['Bruce', 'Farrell', '35', 'Librarian']
# ['Martha', 'Monroe', '31', 'Judge']
# ['Robert', 'Reid', '39', 'Carpenter']
# ['Stephen', 'Finch', '30', 'Coach']
# ['Doris', 'Kinney', '36', 'Athlete']
# ['Ben', 'Whitaker', '35', 'Computer support specialist']
# ['Mark', 'Becker', '39', 'Computer support specialist']
# ['Louis', 'Rollins', '35', 'Economist']
# ['Janet', 'Love', '39', 'Politician']
# ['Constance', 'Black', '36', 'Firefighter']
# ['Jerome', 'Joyce', '40', 'Artist']
# ['Kim', 'Matthews', '38', 'Architect']
# ['Alison', 'MacDonald', '26', 'Childcare worker']
# ['Terry', 'Barton', '27', 'Recreation and fitness worker']
# ['Ken', 'Kennedy', '35', 'Automotive mechanic']
# ['Sandra', 'Middleton', '28', 'Librarian']
# ['Johnny', 'Carlton', '28', 'Librarian']
# ['Lauren', 'Schultz', '33', 'Electrician']
# ['Glenda', 'Boswell', '28', 'Civil engineer']
# ['Geraldine', 'Davis', '36', 'Accountant']
# ['Sidney', 'Terrell', '32', 'Statistician']
# ['Kathy', 'Burch', '28', 'Pilot']
# ['Alexander', 'Gray', '35', 'Reporter']
# ['Laura', 'Eason', '31', 'Loan officer']
# ['Bill', 'Heath', '35', 'Actor']
# ['Florence', 'Carver', '34', 'Electrical engineer']
# ['Claire', 'Shelton', '34', 'Environmental scientist']
# ['Christy', 'Lyons', '31', 'Physicist']
# ['Nancy', 'Hobbs', '40', 'Environmental scientist']
# ['Miriam', 'Wong', '27', 'Childcare worker']
# ['Joanna', 'Middleton', '37', 'Firefighter']
# ['Janice', 'Reid', '40', 'Therapist']
# ['Tommy', 'Barrett', '38', 'Engineering technician']
# ['Lillian', 'Bolton', '32', 'Photographer']
# ['Lester', 'Cash', '30', 'Firefighter']
# ['Jacob', 'Pittman', '34', 'Economist']
# ['Jill', 'Kent', '27', 'Electrical engineer']
# ['Colleen', 'Winters', '36', 'Designer']
# ['Bradley', 'Beatty', '36', 'Human resources assistant']
# ['Glenda', 'Douglas', '28', 'Loan officer']
# ['Mary', 'Cochran', '25', 'Computer support specialist']
# ['Sue', 'Reilly', '33', 'Physicist']
# ['Rita', 'Yates', '34', 'Librarian']
# ['Wallace', 'Kaplan', '35', 'Secretary']
# ['Kimberly', 'Gross', '38', 'Designer']
# ['Jon', 'Richmond', '37', 'Agricultural and food scientist']
# ['Kenneth', 'Pickett', '28', 'Police officer']
# ['Kerry', 'Huff', '38', 'Writer']
# ['Lynne', 'Mangum', '37', 'Chemist']
# ['Rose', 'McCall', '29', 'Farmer']
# ['Frances', 'Wagner', '28', 'Veterinarian']
# ['Diana', 'Crane', '26', 'Lawyer']
# ['Marian', 'Crane', '37', 'Automotive mechanic']
# ['Sheryl', 'Diaz', '30', 'Pharmacist']
# ['Malcolm', 'Chan', '27', 'Environmental scientist']
# ['Max', 'Robinson', '32', 'Dancer']
# ['Christina', 'Harris', '39', 'Doctor']
# ['Evelyn', 'Parsons', '37', 'Human resources assistant']
# ['Dorothy', 'Sherrill', '28', 'Agricultural and food scientist']
# ['Theresa', 'Oakley', '35', 'Nurse']
# ['Glen', 'Thompson', '40', 'Coach']
# ['Ellen', 'Creech', '36', 'Human resources assistant']
# ['Dianne', 'Dillon', '34', 'Recreation and fitness worker']
# ['Kent', 'Roy', '31', 'Electrical engineer']
# ['Melanie', 'Ritchie', '36', 'Financial analyst']
# ['Gene', 'Pearce', '30', 'Architect']
# ['Neal', "O'Connor", '26', 'Therapist']
# ['Bill', 'Klein', '26', 'Teacher']
# ['Rhonda', 'Goldman', '38', 'Computer support specialist']
# ['Glenda', 'Humphrey', '32', 'Carpenter']
# ['Jacob', 'Singleton', '33', 'Veterinarian']
# ['Stephen', 'Melton', '33', 'Athlete']
# ['Jerry', 'Alston', '31', 'Lawyer']
# ['Dean', 'Lutz', '26', 'Pilot']
# ['Veronica', 'Callahan', '31', 'Veterinarian']
# ['Kelly', 'Conway', '36', 'Designer']
# ['Nina', 'Savage', '35', 'Politician']
# ['Brenda', 'Barbour', '36', 'Architect']
# ['Vincent', 'Woodward', '34', 'Electrical engineer']
# ['Hannah', 'Langston', '25', 'Pilot']
# ['Alice', 'Eaton', '32', 'Chemist']
# ['Elisabeth', 'Lowe', '34', 'Farmer']
# ['Guy', 'Klein', '34', 'Designer']
# ['Terry', 'Garcia', '30', 'Automotive mechanic']
# ['Floyd', 'Schroeder', '37', 'Farmer']
# ['Marsha', 'Gold', '36', 'Athlete']
# ['Peter', 'Hughes', '38', 'Computer software engineer']
# ['Bernard', 'Pate', '34', 'Doctor']
# ['Harold', 'Burnett', '40', 'Musician']
# ['Cheryl', 'Horn', '40', 'Veterinarian']

'''Qn:4'''
'''4 india work, fname, lname, age, prof'''
# for i in f:
#     s=i.strip('\n') # i is a string. strip returns a new string without any \n. so we need to store it into a new variable
#     data=s.split(',')
#     if data[-1]=='india':
#         print(data[1:5])
'''---------output----------------'''
# ['Kristina', 'Chung', '55', 'Pilot']
# ['Hazel', 'Bender', '63', 'Carpenter']
# ['Malcolm', 'Wagner', '39', 'Artist']
# ['Dolores', 'McLaughlin', '60', 'Writer']
# ['Francis', 'McNamara', '47', 'Therapist']
# ['Sandy', 'Raynor', '26', 'Writer']
# ['Marion', 'Moon', '41', 'Carpenter']
# ['Beth', 'Woodard', '65', 'Musician']
# ['Julia', 'Desai', '49', 'Musician']
# ['Jerome', 'Wallace', '52', 'Pharmacist']
# ['Neal', 'Lawrence', '72', 'Computer support specialist']
# ['Jean', 'Griffin', '45', 'Childcare worker']
# ['Kristine', 'Dougherty', '63', 'Financial analyst']
# ['Crystal', 'Powers', '67', 'Engineering technician']
# ['Alex', 'May', '39', 'Environmental scientist']
# ['Eric', 'Steele', '66', 'Doctor']
# ['Wesley', 'Teague', '42', 'Carpenter']
# ['Franklin', 'Vick', '28', 'Dancer']
# ['Claire', 'Gallagher', '42', 'Musician']
# ['Marian', 'Solomon', '27', 'Lawyer']
# ['Marcia', 'Walsh', '64', 'Accountant']

'''Qn:5'''
'''5 india work and age above 50 ---fname, lname, age'''

# for i in f:
#     s=i.rstrip('\n')
#     data=s.split(',')
#     if data[-1]=='india':
#        if int(data[3])>50:
#            print(data[1:4])
'''-------output----------'''
# ['Kristina', 'Chung', '55']
# ['Hazel', 'Bender', '63']
# ['Dolores', 'McLaughlin', '60']
# ['Beth', 'Woodard', '65']
# ['Jerome', 'Wallace', '52']
# ['Neal', 'Lawrence', '72']
# ['Kristine', 'Dougherty', '63']
# ['Crystal', 'Powers', '67']
# ['Eric', 'Steele', '66']
# ['Marcia', 'Walsh', '64']

'''Qn:6'''
'''6 india work and prof Dancer fname, lname, age'''
# for i in f:
#     s=i.strip('\n')
#     data=s.split(',')
#     if data[-1]=='india' and data[4]=='Dancer':
#         print(data[1:4])
'''-------output-------------'''
# ['Franklin', 'Vick', '28']

'''Qn:7'''
'''7 Pilot prof fname, lname, age'''

# for i in f:
#     data=i.split(',')
#     if data[4]=='Pilot':
#         print(data[1:4])
'''----output------------'''
# ['Kristina', 'Chung', '55']
# ['Elsie', 'Hamilton', '43']
# ['Faye', 'Norman', '64']
# ['Kathy', 'Burch', '28']
# ['Jeremy', 'House', '61']
# ['Alice', 'Nance', '59']
# ['Geraldine', 'Jensen', '50']
# ['Steven', 'Ballard', '62']
# ['Emma', 'Olson', '74']
# ['Leo', 'Lassiter', '65']
# ['Alan', "O'Neal", '59']
# ['Dean', 'Lutz', '26']
# ['Hannah', 'Langston', '25']


'''Qn:8'''
'''8 Pilot prof and age above 40 fname, lname, age'''
# for i in f:
#     data=i.split(',')
#     if data[4]=='Pilot' and int(data[3])>40:
#         print(data[1:4])
'''--------output------------'''
# ['Kristina', 'Chung', '55']
# ['Elsie', 'Hamilton', '43']
# ['Faye', 'Norman', '64']
# ['Jeremy', 'House', '61']
# ['Alice', 'Nance', '59']
# ['Geraldine', 'Jensen', '50']
# ['Steven', 'Ballard', '62']
# ['Emma', 'Olson', '74']
# ['Leo', 'Lassiter', '65']
# ['Alan', "O'Neal", '59']

'''Qn:9'''
'''9 us work fname, lname, age'''

# for i in f:
#     s=i.rstrip('\n')
#     data=s.split(',')
#     if data[-1]=='us':
#         print(data[1:4])

'''-------output---------'''
# ['Sherri', 'Melton', '34']
# ['Calvin', 'Diaz', '65']
# ['Eugene', 'Graham', '52']
# ['Vickie', 'Watkins', '55']
# ['Luis', 'Hinton', '69']
# ['Allan', 'Marsh', '67']
# ['Melanie', 'Hewitt', '47']
# ['Marianne', 'Branch', '53']
# ['Natalie', 'Walton', '24']
# ['Caroline', "O'Brien", '44']
# ['Arlene', 'Case', '62']
# ['Kyle', 'Watts', '39']
# ['Calvin', 'Christensen', '54']
# ['Gary', 'Parks', '65']
# ['Samantha', 'Hardin', '27']
# ['Sara', 'Lucas', '44']
# ['Stacy', 'Eason', '31']
# ['Gladys', 'Davidson', '52']
# ['Mike', 'Whitehead', '26']
# ['Lynne', 'Rose', '36']
# ['Faye', 'Sparks', '61']
# ['Diana', 'Moore', '44']
# ['Leon', 'Pearson', '24']
# ['Ethel', 'Rodgers', '30']
# ['Steve', 'Graves', '73']
# ['Alison', 'Scarborough', '66']
# ['Sherri', 'Sutton', '75']
# ['Patsy', 'Sinclair', '48']
# ['Kelly', 'Bowman', '69']
# ['Stacy', 'Olsen', '25']
# ['Curtis', 'Love', '45']
# ['Dana', 'McLean', '61']
# ['Jennifer', 'Christian', '54']
# ['Brett', 'Lamb', '39']
# ['Brandon', 'James', '29']
# ['Keith', 'Chandler', '25']
# ['Joann', 'Stout', '32']
# ['Ronnie', 'Cowan', '71']
# ['Scott', 'Golden', '27']
# ['Gene', 'Bowling', '73']
# ['Louise', 'Beasley', '54']
# ['Geoffrey', 'Clapp', '41']
# ['Patricia', 'Abrams', '51']
# ['Jennifer', 'Tilley', '35']
# ['Mary', 'Morse', '70']
# ['Shawn', 'Boykin', '34']
# ['Vincent', 'Sumner', '31']
# ['Kurt', 'Cassidy', '32']
# ['Danny', 'Davidson', '70']
# ['Charlene', 'Heath', '26']
# ['Alice', 'Blanchard', '73']
# ['Joan', 'McAllister', '73']
# ['Betty', 'McKenzie', '45']
# ['Danny', 'Byrne', '51']
# ['Peggy', 'Schroeder', '61']
# ['Leslie', 'Griffin', '37']
# ['Marshall', 'Gross', '42']
# ['Sara', 'Perkins', '67']
# ['Martha', 'Robertson', '37']
# ['Jack', 'Palmer', '52']
# ['Gayle', 'Brady', '45']
# ['Benjamin', 'Rowe', '64']
# ['Roberta', 'Zhang', '38']
# ['Patricia', 'Hodge', '59']
# ['Clifford', 'Li', '63']
# ['Joanne', 'Bowling', '35']
# ['Martin', 'Justice', '58']
# ['Toni', 'Glass', '46']
# ['Beth', 'Willis', '62']
# ['Jessica', 'Hester', '72']
# ['Samantha', 'Floyd', '72']
# ['Jimmy', 'Graves', '69']
# ['Vincent', 'Fischer', '33']
# ['Dianne', 'Norman', '68']
# ['Rhonda', 'Chan', '34']
# ['Tamara', 'Hunt', '25']
# ['Mary', 'Byrd', '34']
# ['Sidney', 'Lane', '54']

'''Qn:10'''
'''10 uk work and age above 50 fname, lname, age'''

# for i in f:
#     s=i.rstrip('\n')
#     data=s.split(',')
#     if data[-1]=='uk' and int(data[3])>50:
#         print(data[1:4])
'------output-------------'
# ['Paige', 'Chen', '74']
# ['Neal', 'Middleton', '59']
# ['Tim', 'Watts', '58']
# ['Beth', 'Walton', '73']
# ['Donald', 'Chung', '65']
# ['Paul', 'Woods', '63']
# ['Patricia', 'Mangum', '67']
# ['Darlene', 'Barton', '54']
# ['Harvey', 'Underwood', '70']
# ['William', 'Jones', '53']
# ['Frederick', 'Baker', '52']
# ['Jason', 'Cross', '56']
# ['Don', 'Sharpe', '53']
# ['Evan', 'Grant', '66']

'''Qn:11'''
'''Each profession count'''
# d={}
# for i in f:
#     data=i.split(',')
#     if data[4] not in d:
#         d[data[4]]=1
#     else:
#         d[data[4]]+=1
# print(d)
'''------output-----------'''
# '''{'Pilot': 13, 'Teacher': 5, 'Firefighter': 9, 'Computer hardware engineer': 7,
# 'Lawyer': 10, 'Veterinarian': 13, 'Carpenter': 10, 'Artist': 8, 'Writer': 5,
# 'Therapist': 8, 'Musician': 15, 'Pharmacist': 8, 'Computer support specialist': 12,
# 'Childcare worker': 17, 'Financial analyst': 4, 'Engineering technician': 9,
# 'Environmental scientist': 10, 'Doctor': 13, 'Dancer': 9, 'Accountant': 9,
# 'Economist': 10, 'Real estate agent': 6, 'Human resources assistant': 10,
# 'Civil engineer': 11, 'Reporter': 8, 'Agricultural and food scientist': 9,
# 'Police officer': 7, 'Secretary': 8, 'Physicist': 8, 'Computer software engineer': 7,
# 'Photographer': 15, 'Social worker': 10, 'Actor': 12, 'Athlete': 9, 'Judge': 6,
# Recreation and fitness worker': 9, 'Architect': 8, 'Loan officer': 14,
# 'Politician': 11, 'Librarian': 8, 'Nurse': 9, 'Designer': 9, 'Coach': 9,
#  'Automotive mechanic': 6, 'Electrician': 8, 'Statistician': 11, 'Psychologist': 5,
#   'Chemist': 6, 'Electrical engineer': 11, 'Farmer': 8, 'africa\n': 1}'''


'''Qn:12'''
'''Each Location count'''
# d={}
# for i in f:
#     s=i.strip('\n')
#     data=s.split(',')
#     if data[-1] not in d:
#         d[data[-1]]=1
#     else:
#         d[data[-1]]+=1
# print(d)
'''--------output----------'''
# {'india': 21, 'uk': 37, 'us': 78, 'china': 56,
# 'africa': 90, 'australia': 104, 'ireland': 77}

'''Qn:13'''
'''Each Age group count'''
# d={}
# for i in f:
#     data=i.split(',')
#     if data[3] not in d:
#         d[data[3]]=1
#     else:
#         d[data[3]]+=1
# print(d)
'''--------output---------'''
#{'55': 7, '74': 12, '34': 13, '66': 11, '42': 8, '43': 9,
# '63': 9, '39': 9, '60': 4, '47': 5, '26': 8, '41': 6, '65': 11,
# '49': 4, '52': 10, '72': 10, '45': 10, '67': 16, '28': 10,
# '27': 10, '64': 13, '40': 10, '50': 9, '59': 14, '24': 4,
# '58': 9, '38': 8, '25': 6, '35': 12, '73': 13, '33': 7,
# '44': 9, '31': 10, '54': 12, '70': 15, '53': 7, '21': 6,
# '56': 7, '22': 5, '37': 11, '69': 10, '62': 8, '36': 11,
# '61': 9, '30': 6, '75': 2, '48': 5, '29': 3, '32': 7,
# '71': 6, '51': 11, '46': 3, '68': 3, '23': 4, '57': 6}





