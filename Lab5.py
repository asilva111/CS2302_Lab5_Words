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







#H = HashTableC(7)
#print("Initial table size: ", len(H.item))
#ReadAndStoreInH(H)
#print("Final table size: ", len(H.item))
#print("Load Factor: ", H.LoadFactor(H))
#
#
#
#
#
#print("Similarity [bear,bear] =  ",         CompareC(H,'bear','bear'))
#print("Similarity [barley,shrimp] = ",      CompareC(H,'barley','shrimp')) 
#print("Similarity [barley,oat] =  ",        CompareC(H,'barley','oat'))
#print("Similarity [federer,baseball] = ",   CompareC(H,'federer','baseball')) 
#print("Similarity [federer,tennis] =  ",    CompareC(H,'federer','tennis'))
#print("Similarity [harvard,stanford] = ",   CompareC(H,'harvard','stanford')) 
#print("Similarity [harvard,utep] =  ",      CompareC(H,'harvard','utep'))
#print("Similarity [harvard,ant] =  ",       CompareC(H,'harvard','white'))
#print("Similarity [raven,crow] =  ",        CompareC(H,'raven','crow'))
#print("Similarity [raven,whale] =  ",       CompareC(H,'raven','whale'))
#print("Similarity [spain,france] =  ",      CompareC(H,'spain','france'))
#print("Similarity [spain,mexico] =  ",      CompareC(H,'spain','mexico'))
#print("Similarity [mexico,france] =  ",     CompareC(H,'mexico','france'))
#print("Similarity [mexico,guatemala] = ",   CompareC(H,'mexico','guatemala')) 
#print("Similarity [computer,platypus] = ",  CompareC(H,'computer','platypus')) 



def ReadAndStoreB(B):
    with open("test.txt" , 'r', encoding="utf8") as f:
        for line in f:
            
            line = line.strip('\n')
            splitLine = line.split(' ')
            npArray = np.zeros(50)
            
            for i in range(1,50):
               npArray[i-1] = splitLine[i] #i-0 to start at 0 in the np array and at 1 in the line.

            tempList = [splitLine[0], npArray]
           
            Insert(B,tempList)




B = None
ReadAndStoreB(B)
InOrderD(B,' ' )





























































