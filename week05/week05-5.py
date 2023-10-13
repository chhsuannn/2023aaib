class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        N1 = len(word1)
        N2 = len(word2)
        N = max(N1,N2)

        ans=""
        for i in range(N):
            if i<N1: ans += word1[i]
            if i<N2: ans += word2[i]

        return ans
