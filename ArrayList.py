import numpy as np

class ArrayList:        
    ### subscript-based access ###
    def __init__(self, Num = 0 ):
        self.data = np.empty(Num, dataType = object)
        self.size = 0

    def __getitem__(self, idx):
        """Implements `x = self[idx]`"""
        assert(isinstance(idx, int))
        if idx >= self.size or idx < 0:
            raise IndexError('Array List is out of range')
        return self.data[idx]

    def __setitem__(self, idx, value):
        """Implements `self[idx] = x`"""
        assert(isinstance(idx, int))
        if idx >= self.size or idx < 0:
            raise IndexError('Array List index out of range')
        self.data[idx]=value

    def __delitem__(self, idx):
        """Implements `del self[idx]`"""
        if idx >= self.size or idx < 0:
            raise IndexError('Array List index out of range')
        assert(isinstance(idx,int))
        for i in range(idx+1,self.size): 
            self.data[i-1]=self.data[i]
        self.data[self.size-1]=None
        self.size-=1
    
    ### stringification ###
            
    def __repr__(self):
        """Supports inspection"""
        return '[]'
    
    def __str__(self):
        """Implements `str(self)`"""
        return '[]'

    ### single-element manipulation ###
    
    def append(self, value):
        pass
    
    def insert(self, idx, value):
        pass
    
    def pop(self, idx=-1):
        pass
    
    def remove(self, value):
        pass
    
    ### predicates (T/F queries) ###
    
    def __eq__(self, other):
        """Implements `self == other`"""
        return True

    def __contains__(self, value):
        """Implements `val in self`"""
        return True
    
    ### queries ###
    
    def __len__(self):
        """Implements `len(self)`"""
        return self.size
    
    def min(self):
        pass
    
    def max(self):
        pass
    
    def index(self, value, i, j):
        pass
    
    def count(self, value):
        pass

    ### bulk operations ###

    def __add__(self, other):
        """Implements `self + other_array_list`"""
        return self
    
    def clear(self):
        pass
    
    def copy(self):
        pass

    def extend(self, other):
        pass

    ### iteration ###
    
    def __iter__(self):
        """Supports iteration (via `iter(self)`)"""
        pass