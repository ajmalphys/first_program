''''''
'''
files are for : storing data
analysis is done based on these files
three types of operations are there in file handling

1--read operation
2--write operation
3--append operation
--------------------------------------------------------------------------------------------------------
1--read operation
to read the file. it is represented by 'r'
---------------------------------------------------------------------------------------------------------
2--write operation
need to store the data analysed. this operation is for that.
it is represented by 'w'
while writing, if we do it to an existing file, it will replace the contents in it.
that is it doesnt appends, but rewrites. which leads to loss of data in that file. 
old data will be replaced with new data
----------------------------------------------------------------------------------------------------------
3--append operation
used to append data
we can do append to the existing files. it dont replace the previous contents
it is represented using 'a'
------------------------------------------------------------------------------------------------------------
need to create a reference first before using this operation

var_name=open(file_name/path,mode_of_operation)             ------->syntax

if one need to
write-----the mode of operation is w
read------the mode of operation is r
append----the mode of operation is a



'''