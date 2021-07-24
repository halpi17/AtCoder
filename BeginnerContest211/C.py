from itertools import *
import itertools

class Solution():
    def chokudai(self, S):
        chokudai_count = 0
        h_list = [''.join(v) for v in list(itertools.combinations(S, 8))]
        for h in h_list:
            if h == 'chokudai':
                chokudai_count += 1

        return chokudai_count % (10**9 + 7)

def main():
    solution = Solution()
    S = input()
    print(solution.chokudai(S))

if __name__ == '__main__':
    main()
