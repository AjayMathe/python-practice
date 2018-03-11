#!usr/bin/python3

#####################################################################
#                                                                   #
# Name        - Ajay Mathe                                          #
# Date        - 10-Mar-2018                                         #
# Usuage      - hello_ur_name.py ajay                               #
# Description - Say hello to the username passed as command line    #                                                    #
#               argument                                            #
#                                                                   #
#####################################################################

import sys

#check if the user passed an argument
if len(sys.argv) > 1:
    #argv[0] refers to the file name along with the fully qualified path
    #argv[1] refers to command line argument passed to the script
    print ("Hello {0}".format(sys.argv[1]))
else:
    print ("Script expects a value at the run time! \nUsage - hello_ur_name.py ajay")


