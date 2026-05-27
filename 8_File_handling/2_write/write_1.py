# f=open('sample','w')
# f.write('bigdata\n')
# f.write('ds\n')
# f.write('java')

f1=open('fruits','r')#reading a file
#create a reference for writing
f2=open('basket','w')
#read the contents from fruits
for i in f1:
    f2.write(i) #creates a file called 'basket' in the same directory

#a new file is created here, if we give the filename of an existing file, it overwrites it
#giving a new name creates a new file

