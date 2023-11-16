class MLMM():
    def answer(self, data):
        ans_lst = []

        for testcase in data["inputs"]:
            cutoff = int(testcase[0])
            n = int(testcase[1])
            nums = [int(num) for num in testcase[2].split()]

            total = 0
            s = []
            for i in range(len(nums)):
                if nums[i] < cutoff:
                    s.append([nums[i], i])
                    total += 1

            while s:
                # print(s)
                curr = s.pop()
                if curr[1]+1 < len(nums) and curr[0] + nums[curr[1]+1] < cutoff:
                    s.append([curr[0]+ nums[curr[1]+1], curr[1]+1])
                    total+=1
                # for j in range(curr[1]+1, len(nums)):
                #     if curr[1] + nums[j] < cutoff:
                #         s.append([curr[1] + nums[j], j])
                #         total += 1
            # print()
            ans_lst.append(total)

        return {"answer": ans_lst}

# tc = {
#     "inputs":[
#     [
#         "16",
#         "4",
#         "10 5 2 6"
#     ],
#     [
#         "2",
#         "18",
#         "1 2 4 4 7 3 3 4 5 6 5 7 7 3 6 5 2 2"
#     ],
#     [
#         "3",
#         "16",
#         "1 2 4 4 7 3 5 6 5 7 7 3 6 5 2 2"
#     ]
#     ]

# }

# m = MLMM()
# print(m.answer(tc))                    


                