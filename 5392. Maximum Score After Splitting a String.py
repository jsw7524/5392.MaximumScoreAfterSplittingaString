class Solution:
    def maxScore(self, s: str) -> int:
        left0=[]
        right1=[]
        counter=0
        for c in s:
            if c == '0':
                counter+=1
            left0.append(counter)
        counter=0
        for c in s[::-1]:
            if c == '1':
                counter += 1
            right1.append(counter)

        smax=0
        slen=len(s)
        right1.reverse()
        for i in range(0,slen-1):
            if left0[i]+right1[i+1] > smax:
                smax=left0[i]+right1[i+1]
        return smax

sln=Solution()
assert 5==sln.maxScore("011101")
assert 5==sln.maxScore("00111")
assert 1==sln.maxScore("00")
assert 3==sln.maxScore("1111")



