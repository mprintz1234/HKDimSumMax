class PortfolioOperations():
    def answer(self, data):
        ans = []
        for testcase in data["inputs"]:
            maxSum = int(testcase[0].split()[2])
            s1 = [int(num) for num in testcase[1].split()]
            s2 = [int(num) for num in testcase[2].split()]
            #dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
            s = []
            currCount = 0
            if s1:
                count = s1[0]
                if count < maxSum:
                    s.append((count, 1, 1, 0))
            if s2:
                count = s2[0]
                if count < maxSum:
                    s.append((count, 1, 0, 1))


            while s:
                top = s.pop(0)
                #print(top)
                if top[1] > currCount:
                    currCount = top[1]
                
                # take from s1
                if top[2] < len(s1) and top[0] + s1[top[2]] < maxSum:
                    s.append((top[0] + s1[top[2]], top[1]+1, top[2]+1, top[3]))

                # take from s2
                if top[3] < len(s2) and top[0] + s2[top[3]] < maxSum:
                    s.append((top[0] + s2[top[3]], top[1]+1, top[2], top[3]+1))
            ans.append(currCount)

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