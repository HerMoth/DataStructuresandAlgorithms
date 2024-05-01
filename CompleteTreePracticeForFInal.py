#Define a Tress class that will be used to create a binary tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self, data): #this allows us to insert data into the tree
        if self.data is None:
            self.data = data
        else:
            if data < self.data: # check if the data is less than the root node
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data: # check if the data is greater than the root node
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

def OrderList(r): # this function will print the tree in order from smallest to largest
    if r is None:
        return
    else: 
        OrderList(r.left)
        print(r.data, end=' ')
        OrderList(r.right)


#postOrder function will print the tree in order from largest to smallest   
def postOrder(r): 
    if r is None:
        return
    else:
        print(r.data, end=' ')
        postOrder(r.right)
        postOrder(r.left)
        
        

if __name__=='__main__':  #this is the main function that will run the code and print the tree
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(7)
    root.insert(13)
    root.insert(15)
    root.insert(1)
    root.insert(10)
    root.insert(9)
    root.insert(11)
    root.insert(8)
    
    #printing the Node of tree sorted
print('\nthis is the tree in order') 
OrderList(root) #1 3 6 7 8 9 10 11 12 13 14 15
print('\nthis is the tree in post order')
postOrder(root) #1 3 8 11 10 9 7 6 13 15 14 12

