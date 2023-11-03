class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        
        N = len(arr)

        #for k in range(N):
        #    for i in range(1,N):
        #        if arr[i] < arr[i-1]:
        #            arr[i], arr[i-1] = arr[i-1], arr[i]
        arr.sort()

        for i in range(1,N):
            if arr[i] - arr[i-1] != arr[1] - arr[0]:
                return False
        return True
            