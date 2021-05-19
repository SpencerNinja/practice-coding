# This program implements an Unordered Unique Container (UUC) ADT
#       using a Linked List implementation

class Node:
    def __init__(self, item, nxt):
        self.mItem = item
        self.mNext = nxt

class UUC: # implemented as a linked list
    def __init__(self):
        self.mStart = None

    def Insert(self, item): # returns False on duplicate
        if self.Exists(item):
            return False
        n = Node(item, self.mStart)
        self.mStart = n
        return True
        
    def Exists(self, item): # returns True if item is in the bag, else False
        current = self.mStart
        while current != None:
            if current.mItem == item:
                return True
            current = current.mNext
        return False

    def Delete(self, item): # returns False if not there
        if not self.Exists(item):
            return False # can't delete if not there

        # detect if item is the first:
        if self.mFirst.mItem == item:
            self.mFirst = self.mFirst.mNext
            return True
        
        current = self.mStart
        while not (current.mNext.mItem == item):
            current = current.mNext

        # At this point, current is pointing to the node BEFORE the one that needs deleting
        current.mNext = current.mNext.mNext
        return True

    def Retrieve(self, item): # returns None if not found
        current = self.mStart
        while current != None:
            if current.mItem == item:
                return current.mItem
            current = current.mNext
        return None

    def Size(self):
        count = 0
        current = self.mStart
        while current != None:
            count += 1
            current = current.mNext
        return count
    
    def Traverse(self, callback):
        current = self.mStart
        while current != None:
            callback(current.mItem)
            current = current.mNext
            

    


            
        
        
