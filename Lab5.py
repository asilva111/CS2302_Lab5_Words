# -*- coding: utf-8 -*-
'''
Created on Wed Mar 25th 20:55:43 2019
CS 2302 - Andres Silva
> Teacher: Olac Fuentes
> TAs: Anindita Nath  & Maliheh Zargaran
> Lab #5
> The purpose of this lab is compare Hashtables vs BSTs in data handling and accessing.
> LAST MODIFIED: APRIL 3rd, 2019
'''
import numpy as np
from hash_table_chain_strings import *
from bst import *
import math
import time

def StringToDec(word): #This method gives a unique decimal value to a string
    value = 0
    
    for i in range(len(word)):
        value += ord(word[i]) * (26**i) #Add up all the ascii values of each character + 26^index - for a unique value
    
    return value

"""
Hash Table Methods ############################################################
"""
def ReadAndStoreInH(H): #Reads text file with data and stores in dynamic hashtable.
    with open("glove.6B.50d.txt" , 'r', encoding="utf8") as f: #Read from file,
        for line in f: #For each line,
            line = line.strip('\n') #Remove next line character
            splitLine = line.split(' ') #Split line into an array
            npArray = np.zeros(50) #Initialize numpy array
            
            for i in range(1,50): #Insert every element of line into np array
               npArray[i-1] = splitLine[i] #i-0 to start at 0 in the np array and at 1 in the line.

            InsertC(H, splitLine[0], npArray) #Insert to H the previous the string and the array,

            if H.num_size > len(H.item): #If more items in hash table than slots, there is a bucket.
                newHash =  EnlargeC(H) #Make bigger hashtable with same elements.
                H.item = newHash.item #Point H to new table.
                H.num_size = newHash.num_size #Update H's number of items

def DotProductC(H,w0,w1): #Return the dot product of two strings.
    product = 0
    
    for i in range(50):
        product += FindC(H,w0)[2][i] * FindC(H,w1)[2][i] #FindC returns a bucket with the npArray at position 2, we access that array at i for each individual element.
    
    return product

def MagnitudeC(H,word): #Return Magnitude of the embeddings of a word.
    magnitude = 0
    SumOfEmbeddings = 0
    
    for i in range(50):
        SumOfEmbeddings += FindC(H,word)[2][i] ** 2
    
    magnitude = math.sqrt(SumOfEmbeddings)
    
    return magnitude

def CompareC(H,word0,word1): #Returns similarity of two words by computing the distance between two vectors.
    similarity = DotProductC(H,word0,word1) / (MagnitudeC(H,word0) * MagnitudeC(H,word1))    
    
    return similarity


"""
BST Methods ###################################################################
"""
def ReadAndStoreB(B): #Reads big data from text file and stores it in binary search tree.
    with open("glove.6B.50d.txt" , 'r', encoding="utf8") as f:#Read file.
        for line in f: #For every line in file:
        
            line = line.strip('\n') #Remove next line character.
            splitLine = line.split(' ') #Split line into an array.
            npArray = np.zeros(50) #Initialize numpy array.
            
            for i in range(1,50):  #Store all numerical data of line into np array.
               npArray[i-1] = splitLine[i] #i-0 to start at 0 in the np array and at 1 in the line.

            tempList = [splitLine[0], npArray] #Create list with string and npArray.

            B = InsertB(B,tempList, StringToDec(tempList[0])) #Insert list in BST using numerical value of string.
        
        return B

def DotProductB(B,s0,s1): #Returns dot product of two strings in a BST.
    product = 0
    
    w0 = StringToDec(s0) #Get numerical value of words
    w1 = StringToDec(s1)
    
    for i in range(50): #FindB returns a list with the npArray at the first index.
        product += FindB(B,s0,w0).item[1][i] * FindB(B,s1,w1).item[1][i] #Multiply and add all of the products of the same entries in the npArrays.
    
    return product

def MagnitudeB(B,word): #Returns the magnitude of the embeddings of a string.
    wordVal = StringToDec(word)
    magnitude = 0
    SumOfEmbeddings = 0
    
    for i in range(50):
        SumOfEmbeddings += FindB(B,word,wordVal).item[1][i] ** 2
    
    magnitude = math.sqrt(SumOfEmbeddings)
    
    return magnitude

def CompareB(B,word0,word1): #Returns the similarity of two strings in a BST.
    similarity = DotProductB(B,word0,word1) / (MagnitudeB(B,word0) * MagnitudeB(B,word1))
    
    return similarity


"""
Printing and comparing methods
"""

def OptionHash(): #Used when Hashtable is selected as a data structure.
    H = HashTableC(113)    
    print("\nInitial table size: ", len(H.item))
    print("\nBuilding Hashtable...")
    
    start = time.time()
    ReadAndStoreInH(H)
    end = time.time()
    
    print("\nBuild time of hashtable: ", end - start)
    print("\nFinal table size: ", len(H.item))
    print("Load Factor: ", LoadFactor(H))
    print("Percentage of empty buckets: ", PercentageOfEmpty(H))
    print("\nComparing word values")
    
    start = time.time()
    with open("test.txt" , 'r', encoding="utf8") as f: #Read from test file.
            for line in f: #For every line,
                line = line.strip('\n') #remove next line character,
                splitLine = line.split(' ') #Split line into individual strings.
                print("Similarity [", splitLine[0], ", ",splitLine[1], "] =", CompareC(H, splitLine[0],splitLine[1])) #Compare the two words used.
    end = time.time()
   
    print("\nRunning time for hash table query processing: ", end - start)
    
    

def OptionBST(): #Used when BST is selected as a data structure.
    B = None
    print("\nBuilding BST..")
    start = time.time()
    B = ReadAndStoreB(B)
    end = time.time()
    
    print("\nBST build time: ", end - start)
    print("\nHeigh of Tree: ", GetHeight(B))
    print("\nNumber of nodes: ", NumberNodes(B))
    
    start = time.time()
    with open("test.txt" , 'r', encoding="utf8") as f:
            for line in f:
                line = line.strip('\n')
                splitLine = line.split(' ')
                print("Similarity [", splitLine[0], ", ",splitLine[1], "] =", CompareB(B, splitLine[0],splitLine[1]))
    end = time.time()
    print("\nRunning time for BST query processing: ", end - start)


"""
Ask for input #################################################################
"""
print("Which data structure should be used?\n BST or Hash Table?")
choice = input("B/H\n")

if choice.lower() == 'b':
    OptionBST()
elif choice.lower() == 'h':
    OptionHash()
else:
    print("Invalid Input, please retry.")


















































