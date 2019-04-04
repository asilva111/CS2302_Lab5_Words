# Code to implement a binary search tree with nodes as [string, npArray]

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def StringToDec(word): #Calculates a unique numerical value for a given string.
    value = 0
    for i in range(len(word)):
        value += ord(word[i]) * (26**i) #Add up all the ascii values of each character + 26^index - for a unique value
    
    return value


def InsertB(T,newItem, wordVal): #Modified to compare value of node based on their assigned value by StringToDec.
    if T == None:
        T =  BST(newItem)
    
    elif StringToDec(T.item[0]) > wordVal:
        T.left = InsertB(T.left,newItem, wordVal)
    
    else:
        T.right = InsertB(T.right,newItem, wordVal)
    
    return T


         
def FindB(T,k, wordVal): #Modified to compare value of nodes 
    # Returns the address of k in BST, or None if k is not in the tree on their assigned value by StringToDec.
    if T is None or T.item[0] == k:
        if T != None:
            return T
        else:
            print("Item not in tree.")
   
    if StringToDec(T.item[0]) < wordVal:
        return FindB(T.right,k, wordVal)
    
    return FindB(T.left,k, wordVal)
  
def GetHeight(T):
    if T == None: #At a none node, add 0 to our sum.
        return 0
    else:
        left = GetHeight(T.left) #Get height of left and right subtree.
        right = GetHeight(T.right)
    if right > left: #add 1 to the largest subtree and return int.
        return 1 + right
    else:
        return 1 + left
    
def NumberNodes(T): # Find number of nodes in the Tree
    if T == None:
        return 0
    
    else:
        left = NumberNodes(T.left)
        right = NumberNodes(T.right)
    
        if left == None:
            left = 0
        if right == None:
            right = 0
    
    if T.left is not None:
            return 1 + left
    if T.right is not None:
            return 1 + right
        
        
def NumberNodes(T): # Find number of nodes in the Tree
    if T != None:
        c = 1
        if T.left != None:
            c += NumberNodes(T.left)
        if T.right != None:
            c += NumberNodes(T.right)
    
    return c
    
    

