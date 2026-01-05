import collections

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Queue():
    def __init__(self):
        self.l = []

    def push(self, elm):
        self.l.append(elm)

    def pop(self):
        return self.l.pop(0)
    
    def is_empty(self):
        return len(self.l) == 0

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        s = Queue()
        d = {} #level -> nodes
        s.push((root, 0))
        d[0] = [root.val]

        while not s.is_empty():
            root, level= s.pop()
            if root != None:
                left_child = root.left
                right_child = root.right
                s.push((left_child, level+1))
                s.push((right_child, level+1))

                if left_child != None or right_child != None:
                    if level+1 not in d:
                        d[level+1] = []

                if left_child != None:
                    d[level+1].append(left_child.val)
                
                if right_child != None:
                    d[level+1].append(right_child.val)
                
        l = []
        for level in d:
            l.append(d[level])
        return l




sol = Solution()
left = TreeNode(val=2, right=None, left=TreeNode(val=4))
right= TreeNode(val=3, right=TreeNode(val=5), left=None)
root = TreeNode(val=1, right=right, left=left)


print(sol.levelOrder(root))

