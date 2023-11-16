class RiskMitigation():

    def answer(self, data):
        ans_lst = []

        for testcase in data["inputs"]:

            n = int(testcase[0].split()[0])
            costs = [int(num) for num in testcase[1].split()]

            start = 0
            end = 0
            increasing = []

            for i in range(1, len(costs)):
                if costs[i] <= costs[i-1] and start==end:
                    start += 1
                    end += 1
                elif costs[i] <= costs[i-1] and start!= end:
                    increasing.append([start, end, costs[end] - costs[start]])
                    start = i
                    end = i
                elif costs[i] > costs[i-1]:
                    end = i

            if start != end:
                increasing.append([start, end, costs[end] - costs[start]])

            while len(increasing) > n:
                loss = increasing[0][2]
                loss_i = 0

                for i in range(1, len(increasing)):
                    curr_loss = increasing[i][2]
                    if costs[increasing[i][1]] > costs[increasing[i-1][1]]:
                        curr_loss -= costs[increasing[i][1]] - costs[increasing[i-1][1]]
                    if curr_loss < loss:
                        loss = curr_loss
                        loss_i = i

                if loss_i == 0:
                    increasing = increasing[1:]
                else:
                    if costs[increasing[i][1]] > costs[increasing[i-1][1]]:
                        increasing[loss_i-1][1] = increasing[loss_i][1]
                    increasing = increasing[:loss_i] + increasing[loss_i+1:]

            total = 0
            for i in range(len(increasing)):
                total += increasing[i][2]
            ans_lst.append(total)
        
        return {"answer": ans_lst}

tc = {
  "inputs": [[
                "2 3",
                "2 4 1"
            ],
            [
                "2 11",
                "3 2 6 5 0 3 5 4 3 1 6"
            ]]
}
rm = RiskMitigation()
print(rm.answer(tc))