#A Binary Tree is a structure that is either empty , consists of a root node  containing a value and two subtrees, called the left and right subtree.
# These subtree are also binary trees.
# The Left subtree is less than the root Node 
# The Right subtree is greater than the root Node


#this is the recursive version of the binary search
def BinarySearch(x, lst): #Assume lst is sorted
    if len(lst) > 0: 
        middleIndx = len(lst) // 2
        if lst[middleIndx] == x:
            return True
        else:
            if lst[middleIndx] > x:
                return BinarySearch(x, lst[:middleIndx])
            else:
                return BinarySearch(x, lst[middleIndx+1:])
    else:
        return False
    
print("Test for the BinarySearch function")  
print(BinarySearch(5, list(range(10)))) #True
print(BinarySearch(10, list(range(10)))) #False
print(BinarySearch(0, list(range(10)))) #True
print(BinarySearch(9, list(range(10)))) #True
print(BinarySearch(4, list(range(10)))) #True
print(BinarySearch(11, list(range(10)))) #False
print(BinarySearch(88, list(range(100))))

#This is the iterative version of the binary search
def bin_search1(x, lst):   # assumes lst is sorted   
    def rec_bin_search1(x, lst, start, end):   # assumes lst is sorted   start=0    
        if end>=start:   #items left to look at
            midIndex=(start+end)//2
            if lst[midIndex] == x:
                return True
            else:
                if lst[midIndex] > x:   # look at lower half
                    return rec_bin_search1(x,lst,start, midIndex-1)
                else:  #  look at upper half
                    return rec_bin_search1(x,lst,midIndex+1, end)
        else:
            return False
    return rec_bin_search1(x, lst, 0, len(lst)-1)

print("Test for the bin_search1 function")
print(bin_search1(5, list(range(10)))) #True
print(bin_search1(10, list(range(10)))) #False
print(bin_search1(0, list(range(10)))) #True

#Linked Tree structure and manual creation
class myNode:
    def __init__(self, value, left= None, right = None):
        self.value = value
        self.left = left
        self.right= right

#Manual creation of a tree
myTree = myNode(20)
myTree.left = myNode(10)
myTree.right = myNode(30)
myTree.left.left = myNode(5)
myTree.left.right = myNode(15)
myTree.right.left = myNode(25)


#BsT using recursion
def min(myTree):
    if myTree.left:
        return min(myTree.left)
    return myTree.value

def max(myTree):
    if myTree.right:
        return max(myTree.right)
    return myTree.value

def findVal(myTree, x):
    if not myTree:
        return False
    elif myTree.value == x:
        return True
    elif myTree.value > x:
        return findVal(myTree.left, x)
    else:
        return findVal(myTree.right, x)
    
