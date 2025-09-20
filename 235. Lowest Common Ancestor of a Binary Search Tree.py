class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        temp=root
        if temp== None:
            return -1
        while temp:
            if p.val<temp.val and q.val<temp.val:
                temp=temp.left
            elif p.val>temp.val and q.val>temp.val:
                temp=temp.right
            
            else:
                return temp
        return None
