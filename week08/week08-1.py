class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0: 
            return False
        while n>1:   #到1為止
            if n%3 !=0:   #沒辦法被3整除
                return False
            else:
                n=n//3

        #經過上面while迴圈層層檢查，都沒失敗
        return True