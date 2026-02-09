class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: In-order traversal to get sorted values
        nodes = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        # Step 2: Build balanced BST from sorted list
        def build_balanced_tree(left, right):
            if left > right:
                return None
            
            # Pick the middle element as the root
            mid = (left + right) // 2
            new_node = TreeNode(nodes[mid])
            
            # Recursively build subtrees
            new_node.left = build_balanced_tree(left, mid - 1)
            new_node.right = build_balanced_tree(mid + 1, right)
            
            return new_node
            
        return build_balanced_tree(0, len(nodes) - 1)