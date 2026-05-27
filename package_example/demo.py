

#print(add(1,2))
''''''
'''this doesnt uses the package_example defined in the 'operation' module
we need to import that function to here

operation module is the package package_example

import package_name.module_name
'''
# import package_example.module_eg
# data=package_example.module_eg.add(1, 2)
# print(data)
# data2=package_example.module_eg.sub(2,1)
# print(data2)
# data3=package_example.module_eg.div(10,5)
# print(data3)
# data4=package_example.module_eg.mul(2,5)
# print(data4)

''' using (.) to access has a limitation
this is normal import
each time we access the modules, we need to explicitly mention the package and module name
to overcome this repetition
we use 'from' import

from packagename.modulename import *  (* means all)

'''
# from package_example.module_eg import *
# a=add(2,3)
# print(a)
# b=sub(4,3)
# print(b)
# c=mul(4,2)
# print(c)
# d=div(3,2)
# print(d)