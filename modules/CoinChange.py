class CoinChange():

    def getNumAndCoins(self, data):
        n = int(data[0].split()[0])
        coins = data[1].split()
        coins = [int(i) for i in coins]

        return n, sorted(coins)

    def answer(self, data):
        ans = []

        for testcase in data["inputs"]:
            n, s_coins = self.getNumAndCoins(testcase)
            dp = [[0 for _ in range(n+1)] for _ in range(len(s_coins)+1)]
            
            for num in range(1, len(s_coins)+1):
                dp[num][s_coins[num-1]] = 1

            for i in range(1, len(s_coins)+1):
                for j in range(n+1):
                    total = dp[i][j]
                    total += dp[i][j-s_coins[i-1]]
                    if i > 1:
                        total += dp[i-1][j]

                    dp[i][j] = total

            ans.append(dp[len(s_coins)][n])

        return {"answer": ans}

# cc = CoinChange()

# testdata = {
#   "inputs": [[
#                 "12 4",
#                 "2 3 4 5"
#             ],
#             [
#                 "206 4",
#                 "2 20 9 30"
#             ]]
# }

