#!/usr/bin/python3 

################################################################
#                                                              #
# @Author     : Ajay Mathe                                     #
# @Date       : 2018-03-15 20:19:43                            #
# @Description: Python internal type conversion example        #
#                                                              #
################################################################

#a is an integer
a = 40
#b is a float
b = 2.31234

print("a = {0}".format(a))
print("b = {0}\n".format(b))


print("type of a is:{0}".format(type(a)))
print("type of b is:{0}\n".format(type(b)))

print("adding them both will internally convert int to float\n")

print("sum of a+b:{0}".format(a+b))
print("Type of the result for a+b:{0}".format(type(a+b)))