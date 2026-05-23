''' Structure for Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

'''
class Solution:
    def toSumTree(self, root):
        def update_tree(node):
            if not node:
                return 0
            old_val=node.data
            left_sum=update_tree(node.left)
            right_sum=update_tree(node.right)
            node.data=left_sum+right_sum
            return node.data+old_val
        update_tree(root)


'''
 input:    10
         /   \ 
      -2      6
      / \    /  \
   8    -4   2   3
output:    4 
         /   \ 
       4      5
      / \    /  \
    0    0  0    0
'''

   
