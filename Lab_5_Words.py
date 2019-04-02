# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:04:41 2019

@author: andre
"""
import numpy as np
from hash_table_chaining import *
from bst import *
import math


#print("\nPlease select a data structure: Binary Search Tree or Chained Hash Table")
#choice = input("\nB/H\n").lower() 

#file = open("glove.6B.50d.txt", 'r')#DONT FORGET TO CLOSE

def StringToDec(word):
    value = 0
    for i in range(len(word)):
        value += ord(word[i]) * (26**i) #Add up all the ascii values of each character + 26^index - for a unique value
    return value

def ReadAndStoreInH(H):
    with open("test.txt" , 'r', encoding="utf8") as f:
        for line in f:
            line = line.strip('\n')
            splitLine = line.split(' ')
            npArray = np.zeros(50)
            
            for i in range(1,50):
               npArray[i-1] = splitLine[i]
              
            tempList = [StringToDec(splitLine[0]), npArray]

            InsertC(H,tempList)

    

#def CompareWithHash(word1,word2):
#    e0 = H[][]
            
def DotProductC(H,valueofW0,valueofW1): #takes decimal value of strings
    
    product = 0

    for i in range(len(FindC(H,valueofW0))):
        product += FindC(H,valueofW0)[i] * FindC(H,valueofW1)[i]
#        print("add ", FindC(H,valueofW0)[i], " and ", FindC(H,valueofW1)[i]  )
    
    return product

def MagnitudeC(H,valueOfW):  #takes decimal value of strings
#    valueOfW = StringToDec(word)
    magnitude = 0
    SumOfEmbeddings = 0
    
    for i in range(len(FindC(H,valueOfW))-1):
        SumOfEmbeddings += FindC(H,valueOfW)[i] ** 2
    
    magnitude = math.sqrt(SumOfEmbeddings)
    
    return magnitude


        
def CompareC(H,word0,word1):
    
    decValOfW0 = StringToDec(word0)
#    print(decValOfW0)
    decValOfW1 = StringToDec(word1)
#    print(decValOfW1)
    
#    
    similarity = DotProductC(H,decValOfW0,decValOfW1) / (MagnitudeC(H,decValOfW0) * MagnitudeC(H,decValOfW1))
    
    return similarity


#print("Strings:")
#print(StringToDec('the'))
#print("Len of H.item ", len(H.item))
#print(StringToDec('the')% len(H.item))
#print(H.item[3][0][0]) #prints word value in hash table
#print(H.item[3][0][1]) #prints array 
#print(H.item[0][0][1][-1]) #prints individual numbers of array
#print(len(H.item[0][0][1]))
#print(StringToDec('and'))
#print(MagnitudeC('and'))

print(CompareC(H,"and","and"))

#decValOfW0 = StringToDec("and")
#print(decValOfW0)
#
#decValOfW1 = StringToDec("the")
#print(decValOfW1)

#print(FindC(H,decValOfW0))
#
#print(FindC(H,decValOfW1))


H = HashTableC(3)

ReadAndStoreInH(H)
#print(H.item)
#print(H.item)
#DotProduct(H,'the','and')
#print(FindC(H,StringToDec('the')))
#print(DotProduct(H,"the","and"))



#print(len(H.item))
#print(LoadFactor(H))

