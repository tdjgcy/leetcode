class Solution:

    # 104
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            left = 1
            right = 1
            left = left + Solution.maxDepth(root.left)
            right = right + Solution.maxDepth(root.right)

            return max(left, right)


    #118
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n=numRows
        if n==0:
            return []
        if n==1:
            return [[1]]
        if n==2:
            return [[1],[1,1]]
        else:
            list_yanghui=[[1],[1,1]]
            for i in range(2,n):
                list_yanghui.append([])
                for j in range(i+1):
                    if j==0:
                        list_yanghui[i].append(1)
                        print (list_yanghui)
                    elif j==i:
                        list_yanghui[i].append(1)
                    else:
                        list_yanghui[i].append(list_yanghui[i-1][j-1]+list_yanghui[i-1][j])
                #print (i,list_yanghui)
            return list_yanghui
