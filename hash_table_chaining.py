# Implementation of hash tables with chaining

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        for i in range(size):
            self.item.append([])
        
        self.num_items = 0

def InsertC(H,k):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    if H.num_items >= len(H.item):
        H = EnlargeC(H)
        
    b = k[0]%len(H.item)
    H.item[b].append(k) 
    H.num_items += 1
   
def FindC(H,k):
    #Returns the numpy array of k
    b = k%len(H.item)
#    print(b)
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return H.item[b][i][1]
    else:
        return -1


 
def DeleteC(H,k):
    # Returns k from appropriate list
    # Does nothing if k is not in the table
    # Returns 1 in case of a successful deletion, -1 otherwise
    b = k%len(H.item)
    try:
        H.item[b].remove(k)
        return 1
    except:
        return -1

def LoadFactor(H):
    if H.num_items == 0:
        return 0
    else:
        return H.num_items / len(H.item) 


def EnlargeC(H):
    newHash = HashTableC((len(H.item) * 2) + 1)
    for i in range(len(H.item)):
        for j in range(len(H.item[i])):
            InsertC(newHash, H.item[i][j])
    return newHash
    
#H = HashTableC(11)
#A = [23, 16, 11, 10, 27, 8, 21]
#for a in A:
#    InsertC(H,a)
#    print(H.item)
#
#for a in A:
#    print(a,FindC(H,a))
#
#print(3,FindC(H,3))
#
#DeleteC(H,10)
#print(H.item)
#DeleteC(H,21)
#print(H.item)
#DeleteC(H,21)
#print(H.item)
#
#i,j = FindC(H,27)
#print(H.item[i][j])
