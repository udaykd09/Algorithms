class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def build_tree(lines, root, pre_tab, cur_tab):
    if pre_tab > cur_tab:
        return root
    root = TreeNode(lines[0])
    for line in lines:
        if '/t' not in line:
            root.children.append(line)
