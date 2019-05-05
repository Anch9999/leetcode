class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        S, L, res, flag = 0, 0, "", 0

        if A >= B:
            L = A
            S = B
            flag = 1
        else:
            L = B
            S = A
            flag = 2

        while(L-S >= 2 and L >= 2 and S >= 1):
            if flag == 1:
                res += 'aab'
            else:
                res += 'bba'
            L -= 2
            S -= 1

        while(L > 0 and S > 0):
            if flag == 1:
                res += 'ab'
            else:
                res += 'ba'
            L -= 1
            S -= 1

        if flag == 1:
            res += 'a' * L
        else:
            res += 'b' * L

        return res

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.strWithout3a3b(4,1))
