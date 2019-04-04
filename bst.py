# Code to implement a binary search tree 
# Programmed by Olac Fuentes
# Last modified February 27, 2019

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def StringToDec(word):
    value = 0
    for i in range(len(word)):
        value += ord(word[i]) * (26**i) #Add up all the ascii values of each character + 26^index - for a unique value
    return value


def InsertB(T,newItem, wordVal):
    if T == None:
        T =  BST(newItem)
    
    elif StringToDec(T.item[0]) > wordVal:
        T.left = InsertB(T.left,newItem, wordVal)
    
    else:
        T.right = InsertB(T.right,newItem, wordVal)
    
    return T


         
def FindB(T,k, wordVal):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item[0] == k:
        if T != None:
            return T
        else:
            print("Item not in tree.")
   
    if StringToDec(T.item[0]) < wordVal:
        return FindB(T.right,k, wordVal)
    
    return FindB(T.left,k, wordVal)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
 
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)


