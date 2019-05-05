class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':

        """
        Calculate all even values of A
        """
        total = 0
        for val in A:
            if val % 2 == 0:
                total += val

        """
        Subtract A[index] is even value.
        We add value to A[index] and examine even values.
        """
        ans = []
        for query in queries:
            val = query[0]
            index = query[1]
            if A[index] % 2 == 0:
                total -= A[index]
            A[index] += val
            if A[index] % 2 == 0:
                total += A[index]
            ans.append(total)
        return ans

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.sumEvenAfterQueries([1,2,3,4],[[1,0],[-3,1],[-4,0],[2,3]]))
