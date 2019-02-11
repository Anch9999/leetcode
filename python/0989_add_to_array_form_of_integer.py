class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        res = 0
        for val in A:
            res = res * 10 + val
        res += K
        ans = []
        while res // 10 > 0:
            val = res % 10
            ans.insert(0, val)
            res //= 10
        ans.insert(0, res)
        return ans

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.addToArrayForm([1,2,0,0], 34))
