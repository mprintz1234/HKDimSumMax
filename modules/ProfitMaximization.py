class ProfitMaximization():

    def answer(self, data):
        ans_lst = []

        for testcase in data["inputs"]:
            n = int(testcase.split()[0])
            pred = [int(num) for num in testcase.split()[1:]]

            min_so_far = pred[0]
            max_so_far = 0
            for num in pred:
                if num < min_so_far:
                    min_so_far = num

                if num - min_so_far > max_so_far:
                    max_so_far = num - min_so_far

            ans_lst.append(max_so_far)
        
        return {"answer": ans_lst}

tc = {
  "inputs": ["14 5 1 6 3 2 5 6 1 3 6 2 5 5 10", "8 100 10 12 5 6 14 5 6"]
}
pm = ProfitMaximization()
print(pm.answer(tc))