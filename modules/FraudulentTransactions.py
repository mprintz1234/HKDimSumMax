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
                #history = transfers[sender]

                s = []
                s.append(sender)
                lookup_set = set()
                while s:
                    curr = s.pop()
                    if curr in lookup_set:
                        continue
                    else:
                        lookup_set.add(curr)

                    if curr == receiver:
                        eligible = False
                        break
                    else:
                        for p in transfers[curr]:
                            s.append(p)

                transfers[receiver].add(sender)
                # if receiver in history:
                #     eligible = False
                #     break
                # else:
                #     transfers[receiver].add(sender)
                #     #transfers[receiver].add(sender)
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
#             ],[
#                 "7 8","0 5","6 4","6 2","2 0","4 1","5 3","2 1","3 2"
#             ]]
# }
# ft = Fraud()
# print(ft.answer(tc))
