""" Binary Search Tree Implementation. """

class Node:
    def __init__(self, left=None, item=None, right=None) -> None:
        self.left = left
        self.right =right
        self.item = item

class BST:
    def __init__(self, root=None) -> None:
        self.root = root

    def get_insert_parents(self, root_node, data):
        # data come on left side of tree
        if root_node.item > data:
            if not root_node.left:
                n = Node(item=data)
                root_node.left = n
                return 

            new_root_node = root_node.left
            return self.get_insert_parents(root_node=new_root_node, data=data)
        # data come on right side of tree
        else:
            if not root_node.right:
                n = Node(item=data)
                root_node.right = n
                return
            
            new_root_node = root_node.right
            return self.get_insert_parents(root_node=new_root_node, data=data)

    def insert(self, data):
        if not self.root:
            n = Node(item=data)
            self.root = n
        else:
            parents_insert_node = self.get_insert_parents(root_node=self.root, data=data)
            # parents_insert_node.left

    def search(self, data, root_node=None):
        if not root_node:
            root_node = self.root
    
        if root_node.item == data:
            return root_node
        elif root_node.item > data:
            new_root_node = root_node.left
            if new_root_node:
                return self.search(data=data, root_node=new_root_node)
            return None
        elif root_node.item < data:
            new_root_node = root_node.right
            if new_root_node:
                return self.search(data=data, root_node=new_root_node)
            return None
        else:
            return None

    def inorder_traversal(self, root_node=None):
        """Left Tree -> Root -> Right Tree"""
        
        result = []
        self.recursive_inorder_traversal(self.root, result)
        return result
        
    def recursive_inorder_traversal(self, root, result):
        if root:
            self.recursive_inorder_traversal(root.left, result)
            result.append(root.item)
            self.recursive_inorder_traversal(root.right, result)
            

    def preorder_traversal(self, root_node=None):
        """Root -> Left Tree -> Right Tree"""
        result = []
        self.recursive_preorder_traversal(self.root, result)
        return result
    
    def recursive_preorder_traversal(self, root, result):
        if root:
            result.append(root.item)
            self.recursive_preorder_traversal(root.left, result)
            self.recursive_preorder_traversal(root.right, result)

    def postorder_traversal(self):
        """Left Tree -> Right Tree -> Root"""
        result = []
        self.recursive_postorder_traversal(self.root, result)
        return result
    
    def recursive_postorder_traversal(self, root, result):
        if root:
            self.recursive_postorder_traversal(root.left, result)
            self.recursive_postorder_traversal(root.right, result)
            result.append(root.item)



if __name__ == "__main__":
    bst_obj = BST()

    bst_obj.insert(50)
    bst_obj.insert(30)
    bst_obj.insert(70)
    bst_obj.insert(10)
    bst_obj.insert(40)
    bst_obj.insert(60)
    bst_obj.insert(35)
    bst_obj.insert(45)
  

    print(bst_obj.root)
    a = bst_obj.search(data=25)
    b = bst_obj.search(data=1)

    print(f"inorder traversal: {bst_obj.inorder_traversal()}")
    print(f"pre_order_traversal: {bst_obj.preorder_traversal()}")
    print(f"post_order_traversal: {bst_obj.postorder_traversal()}")
    
