class PortfolioOperations():
    def answer(self, data):
        ans = []
        for testcase in data["inputs"]:
            maxSum = int(testcase[0].split()[2])
            biggestCount = 0
            s1 = [int(num) for num in testcase[1].split()]
            s2 = [int(num) for num in testcase[2].split()]
            dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

            #dp[1][0] = s1[0]
            # if s1[0] <= maxSum:
            #     biggestCount = max(biggestCount, 1)
            #dp[0][1] = s2[0]
            # if s2[0] <= maxSum:
            #     biggestCount = max(biggestCount, 1)

            # dp[1][1] = max(s1[0], s2[0])
            # if dp[1][1] <= maxSum:
            #     biggestCount = max(biggestCount, 2)


            for i in range(1, len(s1)+1):
                dp[i][0] = dp[i-1][0] + s1[i-1]
                # if dp[i][1] <= maxSum:
                #     biggestCount = max
            
            for i in range(1, len(s2)+1):
                dp[0][i] = dp[0][i-1] + s2[i-1]

            for row in dp:
                print(row)
            print()

            for s1_i in range(1, len(s1)+1):
                for s2_i in range(2, len(s2)+1):
                    dp[s1_i][s2_i] = max(dp[s1_i-1][s2_i] + s1[s1_i-1], dp[s1_i][s2_i-1] + s2[s2_i-1])
            for row in dp:
                print(row)
            print()

            for s1_i in range(1, len(s1)+1):
                for s2_i in range(2, len(s2)+1):
                    if dp[s1_i][s2_i] <= maxSum:
                        biggestCount = max(biggestCount, s1_i+s2_i)
            
            ans.append(biggestCount)
            
        return {"answer": ans}

# tc = {
#   "inputs": [[
#                 "5 4 10",
#                 "4 2 4 6 1",
#                 "2 1 8 5"
#             ],
#             [
#                 "3 7 3696",
#                 "12 21 102",
#                 "167 244 377 56 235 269 23"
#             ]]
# }
# po = PortfolioOperations()
# print(po.answer(tc))