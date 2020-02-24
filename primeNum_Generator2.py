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
def primnum_Generator(maxNum):
    testNum = maxNum + 1
    allList = range(2, testNum)
    primeList = []
    comList = []
    i = 2
    #print allList

#ERROR CHECK
    if maxNum < 2: #test maxNum
        print ("input number should be equal to or greater than two")
    else: #proceed
        #print ("proceed")
        pass

#BODY
        for i in allList:
    	   for j in range(2, int(i/2)+1):
                if i % j == 0:
    			 comList.append(i)
                else:
            	   j + 1

#POSTPROCESS
    comList = list(dict.fromkeys(comList))
    #primeList = allList.remove(comList)
    primeList = list(set(allList) - set(comList))
    primeList.sort()
#OUTPUT
    print primeList
    #print comList

#CLEANUP
    del testNum
    del maxNum
    del allList
    del primeList
    del comList



#RUN CODE
primnum_Generator(-9)