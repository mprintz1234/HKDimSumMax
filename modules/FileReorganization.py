class FileReorganization():

    def answer(self, data):
        print(data)

        ans = []

        for testcase in data["inputs"]:
            d = {}
            largest = 0

            for c in testcase:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1

            for key in d.keys():
                if d[key] == 1:
                    continue
                while d[key] > 1:
                    largest += 2
                    d[key] -= 2

            for key in d.keys():
                if d[key] == 1:
                    largest += 1
                    break

            ans.append(largest)

        return ans


# tc = {
#   "inputs": ["abccccdd", "a"]
# }

# fr = FileReorganization()
