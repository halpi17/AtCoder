class Solution():
    def chokudai(self, S):
        t = 'chokudai'

        dp = [[0] * (len(S) + 1) for _ in range(9)]

        for i in range(9):
            for j in range(len(S) + 1):
                if i == 0:
                    dp[i][j] = 1
                    continue
                if j == 0:
                    dp[i][j] = 0
                    continue
                if S[j-1] != t[i-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

        return dp[-1][-1] % (10**9 + 7)

def main():
    solution = Solution()
    S = input()
    print(solution.chokudai(S))

if __name__ == '__main__':
    main()
