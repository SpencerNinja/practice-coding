# This program makes a Unordered Unique Container (UUC) ADT
#   implemented with a BST.
# By the CS 2420 class
# October 2020

class Node:
    def __init__(self, item):
        self.mItem = item
        self.mL = None
        self.mR = None

class UUC:
    def __init__(self):
        self.mRoot = None

    def Insert(self, item): # returns False if item is a duplicate
        if self.Exists(item):
            return False
        n = Node(item)
        self.mRoot = self.InsertR(n, self.mRoot)
        return True

    def InsertR(self, n, current):
        if current is None:
            current = n
        elif n.mItem < current.mItem:
            current.mL = self.InsertR(n, current.mL)
        else:
            current.mR = self.InsertR(n, current.mR)
        return current
            

    def Exists(self, item): # returns True if found, False otherwise

        return False

    def Delete(self, item): # return True on success, False otherwise
        if not self.Exists(item):
            return False
        self.mRoot = self.DeleteR(item, self.mRoot)
        return True

    def DeleteR(self, item, current):
        if item < current.mItem:
            current.mL = self.DeleteR(item, current.mL)
        elif item > current.mItem:
            current.mR = self.DeleteR(item, current.mR)
        else:
            # current is now pointing to the node containing the item we want to delete.
            if current.mR is None and current.mL is None:
                # no child node
                current = None
            elif current.mR is not None and current.mL is None:
                # one right child
                current = current.mR
            elif current.mL is not None and current.mR is None:
                # one left child
                current = current.mL
            else: # two child case
                successor = current.mR
                while successor.mL is not None:
                    successor = successor.mL
                current.mItem = successor.mItem
                current.mR = self.DeleteR(successor.mItem, current.mR)
        return current
                
                
                
                
    def Retrieve(self, item): # returns the item if found, None otherwise
        return None

    def Size(self):
        count = 0
        return count

    def Traverse(self, callback):
        self.TraverseR(callback, self.mRoot)

    def TraverseR(self, callback, current):
        pass
        
#####################################################################

def main():            
    clowns = UUC()

    ok = clowns.Insert("Pennywise")
    ok = clowns.Insert("Pennywisx")
    ok = clowns.Insert("Bubbles")
    ok = clowns.Insert("Bozo")
    clowns.Traverse(PrintClown)

    print()
    ok = clowns.Delete("Pennywise")
    clowns.Traverse(PrintClown)


def PrintClown(clown):
    print (clown)
    

main()
        
        
