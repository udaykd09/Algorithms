class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def least_common_ancestor(root, node1, node2):
    if root.value==node1.value or root.value==node2.value:
        return root

    lca_left = least_common_ancestor(root.left, node1, node2)
    lca_right = least_common_ancestor(root.right, node1, node2)

    if lca_left and lca_right:
        return root

    return lca_left if lca_left else lca_right


# 
#
def lowestCommonAncestor(root, p, q):
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q

