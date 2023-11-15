import math

class DataEncryption():

    def answer(self, data):
        ans_lst = []

        for testcase in data["inputs"]:
            testcase = testcase.replace(" ", "")
            n = len(testcase)
            rows = int(math.sqrt(n))
            cols = int(math.sqrt(n))

            while rows*cols < n:
                if cols < int(math.sqrt(n))+1:
                    cols += 1
                elif rows < int(math.sqrt(n))+1:
                    rows += 1
            
            char_lst = list(testcase)

            ans = ""
            print(rows, cols)
            for i in range(cols):
                for j in range(rows):
                    if j*cols+i >= n:
                        continue
                    ans += char_lst[j*cols+i]
                ans += " "
            
            ans_lst.append(ans.strip())

        return {"answer": ans_lst}


# tc = {
#     "inputs": ["coding", "its harder to read code than to write it"]
# }

# dc = DataEncryption()
# print(dc.answer(tc))