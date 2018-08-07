# 1 两数之和

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_nums=nums
        target=target
        n=len(list_nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                target_i=list_nums[i]
                target_j=list_nums[j]
                if target==target_i+target_j:
                    pos_num=[i,j]
                    return pos_num
        return True

    #7 反转整数
    def reverse(self, x):
        l = list(str(x))
        n = len(l)
        for i in range(n-1,0,-1):
            if l[i] != '0':
                l = l[:i+1]
                break
        if l[0] =='-':
                    l = l[:0:-1]
                    l.insert(0,'-')
        else:
            l = l[::-1]
        result=int(''.join(l))
        return result


    # 9 回文数
    def is_palindrome(n):
        n=str(n)
        m=n[::-1]
        return n==m

    # 13
    def romanToInt(self, s):
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for i in range(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                result-= d[s[i]]
            else:
                result+=d[s[i]]
        result+=d[s[len(s)-1]]
        return result if 1 < result < 3999 else False


    # 14
    def longestCommonPrefix(self, strs):
        res = ""
        if len(strs) == 0:
            return ""
        for each in zip(*strs):#zip()函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
            if len(set(each)) == 1:#利用集合创建一个无序不重复元素集
                res += each[0]
            else:
                return res
        return res

    #    26
    def removeDuplicates(self,A):
        k=0
        for i in range(1,len(A)):
            if A[i]!=A[k]:
                k+=1
                A[k]=A[i]
                del A[k+1:len(A)]
        return len(A)

    # 27
    def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        return start

    #28
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
            
