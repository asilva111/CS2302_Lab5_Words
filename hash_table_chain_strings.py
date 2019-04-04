# Implementation of hash tables with chaining using strings

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        for i in range(size):
            self.item.append([])
        
        self.num_size = 0
        
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k,len(H.item))
    H.item[b].append([k,l]) 
    H.num_size += 1
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return b, i, H.item[b][i][1]
    return b, -1, -1
 
def h(s,n):
    r = 0
    for c in s:
        r = (r*n + ord(c))% n
    return r


def EnlargeC(H):

    newHash = HashTableC((len(H.item) * 2) + 1)
    
    for i in range(len(H.item)):
        for j in range(len(H.item[i])):
           for k in range(len(H.item[i][j]) -1):
                InsertC(newHash, H.item[i][j][0], H.item[i][j][1])

    return newHash


def LoadFactor(H):
    if H.num_size == 0:
        return 0
    else:
        return H.num_size / len(H.item) 
    
    
    
def PercentageOfEmpty(H):
    EmptyCounter = 0
    if len(H.item) == 0:
        return 100
    else:
        for i in range(len(H.item)):
            if len(H.item[i]) == 0:
                EmptyCounter += 1
        
        return (EmptyCounter * 100) / len(H.item)
        
            

#H = HashTableC(11)
#A = ['data','structures','computer','science','university','of','texas','at','el','paso']
#for a in A:
#    InsertC(H,a,len(a))
#    print(H.item)
#
#for a in A: # Prints bucket, position in bucket, and word length
#    print(a,FindC(H,a))
 
