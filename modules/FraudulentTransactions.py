class Fraud():

    def answer(self, data):
        ans_lst = []

        for testcase in data["inputs"]:
            num_clients = int(testcase[0].split()[0])
            num_transactions = int(testcase[0].split()[1])
            transfers = {}
            eligible = True
            for i in range(num_clients):
                transfers[str(i)] = set()

            for i in range(1,len(testcase)):
                sender = testcase[i].split()[0]
                receiver = testcase[i].split()[1]
                if sender == receiver:
                    continue
                history = transfers[sender]

                if receiver in history:
                    eligible = False
                    break
                else:
                    transfers[receiver].update(history)
                    transfers[receiver].add(sender)
                # print(sender, receiver, transfers)

            # print()
            if eligible:
                ans_lst.append("Eligible")
            else:
                ans_lst.append("Ineligible")

        return {"answer": ans_lst}

# tc = {
#   "inputs": [[
#                 "4 5",
#                 "0 1",
#                 "1 2",
#                 "1 3",
#                 "2 0",
#                 "3 2"
#             ],[
#                 "3 2",
#                 "0 1",
#                 "1 1"
#             ]]
# }
# ft = Fraud()
# print(ft.answer(tc))
