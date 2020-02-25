#-------------------------------------------------------------------------------
# Name:        primnum_Generator
# Purpose:     to generate all prime number list less than the input number
#
# Author:      William Lien
#
# Created:     24/02/2020
# Copyright:
# Licence:
#-------------------------------------------------------------------------------
#DEFINE FUNCTION
def Divisor_Generator(inNum):
    testNum = inNum
    divsorList = []
    divList = []
    i = testNum
    #print allList

#ERROR CHECK
    if inNum < 2: #test maxNum
        print ("input number should be equal to or greater than two")
    else: #proceed
        #print ("proceed")

#BODY
        for j in range(1, int(i/2)+1):
            if i % j == 0:
                divList.append(j)
                divList.append(i/j)
            else:
       	        pass
        #rigional cleanup

#POSTPROCESS
    #divList = list(dict.fromkeys(divList))
    #divList.sort()

#OUTPUT
    print divList
    print

#CLEANUP
    del inNum
    del testNum
    del divList

#RUN CODE
Divisor_Generator(30000)