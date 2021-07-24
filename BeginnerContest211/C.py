class Solution():
    def chokudai(self, S):
        t = 'chokudai'

        dp = [0] * 9
        dp[0] = 1

        for i in range(len(S)):
            for j in range(8):
                if (S[i] == t[j]):
                    dp[j+1] += dp[j]

        return dp[8] % (10**9 + 7)

def main():
    solution = Solution()
    S = input()
    print(solution.chokudai(S))

if __name__ == '__main__':
    main()
