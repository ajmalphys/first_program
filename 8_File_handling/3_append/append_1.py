''''''
#we need to read an existing file
#then we should add some content to it
#then check whether the data is appended or over written

#let me create a file in E>datascience folder

f1=open(r'E:\Datascience\filehandling_append\append_1.txt','r')
print(f1.read()) #prints the content in the reference file

#now let me try to append
#t append, im opening the same file itself

f2=open(r'E:\Datascience\filehandling_append\append_1.txt','a')
f2.write('this is the appended content')
print(f1.read())
#everytime i run the script, the content is getting appended.