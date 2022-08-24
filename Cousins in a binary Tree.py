# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        Que=deque()
        Que.append(root)
        while Que:
            length=len(Que)
            flagX=False
            flagY=False
            for _ in range(length):
                node=Que.popleft()
                if node.left and node.right and ((node.left.val==x and node.right.val==y) or (node.left.val==y and node.right.val==x)):
                    return False
                if node.val==x:
                    flagX=True;
                if node.val==y:
                    flagY=True;
                
                if node.left:
                    Que.append(node.left)
                if node.right:
                    Que.append(node.right)
            if flagX and flagY:
                return True
        return False