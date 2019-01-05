#!/usr/bin/python3 

################################################################
#                                                              #
# @Author     : Ajay Mathe                                     #
# @Date       : 2018-03-15 20:43:54                            #
# @Description: Strings in python and default string functions #
#                                                              #
################################################################

Today = "thursday"

print("string is: {0}\n".format(Today))

#each character in a string can be accessed by specifying the index
print("get first char in the string(sting[0]): {0}".format(Today[0]))
#0 represents the first character in a string, we can slice the string to any number of characters
print("sliced the string to get 1st 3 chars(sting[0:3]):{0}".format(Today[0:3]))
#-1 represents the last character in a string
print("second character from backwards(sting[-2]):{0}".format(Today[-2]))
print("\n")

print("Length of the string {0} is {1}".format(Today,len(Today))+" len(string)")
print("capitalize with string.capitalize() function:{0}".format(Today.capitalize()))
print("Replace 'u' with 'a' in {1} using string.replace() function :{0}".format(Today.replace('u','a'),Today))

#check for specific types
print("string.isnumeric(): {0}".format(Today.isnumeric()))
print("string.isalpha(): {0}\n".format(Today.isalpha()))

#split the string with split function
student_names = "ajay,babu,mathe"
print("split function example : "+student_names)

#use sting.split function
print(student_names.split(","))


