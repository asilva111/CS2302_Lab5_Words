# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:17:32 2019

@author: andre
"""
import numpy as np
from hash_table_chain_strings import *
from bst import *
import math
import time

def StringToDec(word):
    value = 0
    for i in range(len(word)):
        value += ord(word[i]) * (26**i) #Add up all the ascii values of each character + 26^index - for a unique value
    return value

def ReadAndStoreInH(H):
    with open("glove.6B.50d.txt" , 'r', encoding="utf8") as f:
        for line in f:
            line = line.strip('\n')
            splitLine = line.split(' ')
            npArray = np.zeros(50)
            
            for i in range(1,50):
               npArray[i-1] = splitLine[i] #i-0 to start at 0 in the np array and at 1 in the line.

            InsertC(H, splitLine[0], npArray) #Insert to H the previous the string and the array

            if H.num_size >= len(H.item):
                H.item = EnlargeC(H).item


def DotProductC(H,w0,w1): #takes H and words
    product = 0
    
    for i in range(50):
        product += FindC(H,w0)[2][i] * FindC(H,w1)[2][i]
    
    return product

def MagnitudeC(H,word):
    magnitude = 0
    SumOfEmbeddings = 0
    
    for i in range(50):
        SumOfEmbeddings += FindC(H,word)[2][i] ** 2
    
    magnitude = math.sqrt(SumOfEmbeddings)
    
    return magnitude

def CompareC(H,word0,word1):
    similarity = DotProductC(H,word0,word1) / (MagnitudeC(H,word0) * MagnitudeC(H,word1))    
    return similarity



def ReadAndStoreB(B):
    with open("glove.6B.50d.txt" , 'r', encoding="utf8") as f:
        for line in f:
            
            line = line.strip('\n')
            splitLine = line.split(' ')
            npArray = np.zeros(50)
            
            for i in range(1,50):
               npArray[i-1] = splitLine[i] #i-0 to start at 0 in the np array and at 1 in the line.

            tempList = [splitLine[0], npArray]

            print("Inserting..")
            
            B = InsertB(B,tempList, StringToDec(tempList[0]))
        
        return B

def DotProductB(B,s0,s1): #takes B and words
    product = 0
    
    w0 = StringToDec(s0)
    w1 = StringToDec(s1)
    
    for i in range(50):
        product += FindB(B,s0,w0).item[1][i] * FindB(B,s1,w1).item[1][i]
    
    return product

def MagnitudeB(B,word):
    wordVal = StringToDec(word)
    magnitude = 0
    SumOfEmbeddings = 0
    
    for i in range(50):
        SumOfEmbeddings += FindB(B,word,wordVal).item[1][i] ** 2
    
    magnitude = math.sqrt(SumOfEmbeddings)
    
    return magnitude

def CompareB(B,word0,word1):
    similarity = DotProductB(B,word0,word1) / (MagnitudeB(B,word0) * MagnitudeB(B,word1))
    
    return similarity



B = None
start = time.time()
B = ReadAndStoreB(B)
end = time.time()

print("BST build time: ", end - start)


print(CompareB(B,'the','and'))







#H = HashTableC(113)
#print("Initial table size: ", len(H.item))
#ReadAndStoreInH(H)
#print("Final table size: ", len(H.item))
#print("Load Factor: ", LoadFactor(H))
#print("Percentage of empty buckets: ", PercentageOfEmpty(H))
#
#print("Comparing word values)")
#start = time.time()
#
#with open("test.txt" , 'r', encoding="utf8") as f:
#        for line in f:
#            line = line.strip('\n')
#            splitLine = line.split(' ')
#            print("Similarity [", splitLine[0], ", ",splitLine[1], "] =", CompareC(H, splitLine[0],splitLine[1]))
#
#print("Running time for hash table query processing: ", end - start)






















































