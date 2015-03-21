# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    # Your Code Here
    actual=atMe
    
    if newFrob.myName()<actual.myName():
        while actual!=None and newFrob.myName()<actual.myName():
            anterior=actual
            actual=actual.getBefore()
        if(actual!=None):
            anterior.setBefore(newFrob)
            newFrob.setAfter(anterior)
            actual.setAfter(newFrob)
            newFrob.setBefore(actual)
        else:
            anterior.setBefore(newFrob)
            newFrob.setAfter(anterior)
    else:
        while actual!=None and newFrob.myName()>=actual.myName():
            anterior=actual
            actual=actual.getAfter()
        if(actual!=None):
            anterior.setAfter(newFrob)
            newFrob.setBefore(anterior)
            actual.setBefore(newFrob)
            newFrob.setAfter(actual)
        else:
            anterior.setAfter(newFrob)
            newFrob.setBefore(anterior)
            
def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    # Your Code Here
    if start.getBefore()==None:
        print start.myName()+"if"
        return start
    else:
        print start.myName()+"else"
        findFront(start.getBefore())

p = Frob('percival')
r = Frob('rupert')
insert(p, r)

print findFront(r)