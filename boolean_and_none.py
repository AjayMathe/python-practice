#!/usr/bin/python3 

################################################################
#                                                              #
# @Author     : Ajay Mathe                                     #
# @Date       : 2019-01-05 09:17:17                            #
# @Description: Boolean and none in python.                    #
#                                                              #
#                                                              #
#                                                              #
################################################################

python_love=True #notice capital T
java_love=False #notice capital F

if python_love:
    print("that's great! welcome to python world")

if java_love:
    print("that's great! welcome to java world")

#converting booleans to int or strings
print("converting {0} to int:{1}".format(python_love,int(python_love)))
print("converting {0} to string:{1}".format(python_love,str(python_love)))


# none represents a null value
alian =None
print(alian) #prints None

if alian:
    print("true")