#Binary Search Tree
class BST:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key==None:
            self.key=data
            return
        if self.key==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
root=BST(10)