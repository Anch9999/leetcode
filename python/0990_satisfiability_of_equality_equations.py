class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':

        def find(val):
            if dic[val] != val:
                dic[val] = find(dic[val])
            return dic[val]

        equations = sorted(equations, key=lambda x: x[1] =='!')

        dic = {}
        for code in range(ord('a'), ord('z')+1):
            dic[chr(code)] = chr(code)

        for e in equations:
            if e[1] == '=':
                dic[find(e[0])] = find(e[3])
            if e[1] == '!' and find(e[0]) == find(e[3]):
                return False

        return True

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.equationsPossible(["a==b","b!=c","c==a"]))
