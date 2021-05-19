# This program makes a Unordered Unique Container (UUC) ADT
#   implemented with a Linked List.
# By the CS 2420 class
# October 2020

class Node:
    def __init__(self, item, nxt):
        self.mItem = item
        self.mNext = nxt

class UUC:
    def __init__(self):
        self.mFirst = None

    def Insert(self, item): # returns False if item is a duplicate
        if self.Exists(item):
            return False
        n = Node(item, self.mFirst)
        self.mFirst = n
        return True

    def Exists(self, item): # returns True if found, False otherwise
        current = self.mFirst
        while current is not None:
            if current.mItem == item:
                return True
            current = current.mNext
        return False

    def Delete(self, item): # return True on success, False otherwise
        if not self.Exists(item):
            return False

        # check for First item special case:
        if self.mFirst.mItem == item:
            self.mFirst = self.mFirst.mNext
            return True
            
        current = self.mFirst
        while not (current.mNext.mItem == item):
            current = current.mNext

        # When we get here, current is pointing to the node BEFORE the one to delete
        current.mNext = current.mNext.mNext
        return True

    def Retrieve(self, item): # returns the item if found, None otherwise
        current = self.mFirst
        while current is not None:
            if current.mItem == item:
                return current.mItem
            current = current.mNext
        return None

    def Size(self):
        count = 0
        current = self.mFirst
        while current is not None:
            count += 1
            current = current.mNext
        return count

    def Traverse(self, callback):
        current = self.mFirst
        while current is not None:
            callback(current.mItem)
            current = current.mNext
        
#####################################################################

def main():            
    clowns = UUC()

    ok = clowns.Insert("Pennywise")
    print(ok)
    clowns.Traverse(PrintClown)
    
    ok = clowns.Insert("Pennywise")
    print(ok)
    clowns.Traverse(PrintClown)

    ok = clowns.Insert("bubbles")
    ok = clowns.Insert("bozo")
    print(ok)
    clowns.Traverse(PrintClown)

    print(clowns.Size())

def PrintClown(clown):
    print (clown)
    

# main()
        
        
