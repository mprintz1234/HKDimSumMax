class TimeIntervals():

    def getResStr(self, start, end, num, lstOfIntervals):
        emplLst = []
        for interval in lstOfIntervals:
            emplLst.append(interval[2])

        return_str = str(start) + " " + str(end) + " " + str(num)
        if emplLst:
            return return_str + " " + ' '.join(sorted(emplLst))
        else:
            return return_str

    def answer(self, data):
        
        ans = []

        for testcase in data["inputs"]:
            res = []

            n = 0
            employees = testcase[1].split()
            pq = []

            for i in range(2, len(testcase)):
                interval = testcase[i].split()
                pq.append((int(interval[0]), int(interval[1]), employees[i-2]))

            pq = sorted(pq)            
            curr_time = pq[0][0]
            min_end_interval_time = pq[0][1]

            i = 0

            on_desk_q = {}
            clock = pq[0][0] + 1
            start_time = pq[0][0]
            on_desk_q[start_time] = []
            while pq and pq[0][0] == start_time:
                on_desk_q[start_time].append(pq[0])
                pq.pop(0)                

            while clock <= 21:
                leave = False
                join = False
                combined = [] # get who is currently on desk

                for key in on_desk_q.keys():
                    combined += on_desk_q[key]

                    # any employee need to leave desk
                    while on_desk_q[key] and on_desk_q[key][0][1] == clock:
                        leave = True
                        on_desk_q[key].pop(0)

                # add new employee to desk
                while pq and pq[0][0] == clock:
                    join = True
                    # enqueue users to desk
                    if pq[0][0]in on_desk_q:
                        on_desk_q[pq[0][0]].append(pq[0])
                    else:
                        on_desk_q[pq[0][0]] = [pq[0]]
                    pq.pop(0)

                if leave or join:
                    #res.append([start_time, clock, len(combined), combined])
                    res.append(self.getResStr(start_time, clock, len(combined), combined))
                    n += 1
                    start_time = clock

                clock += 1
            res = [str(n)] + res
            ans.append(res)

        return {"answer": ans}

# tc = {
#     "inputs": [["5",
#         "Alice Bob Cacey Deepak Emma",
#         "10 14",
#         "11 12",
#         "10 15",
#         "12 16",
#         "14 16"],
#         ["3",
#         "Neil Angel Alok",
#         "1 10",
#         "7 9",
#         "7 10"]]
# }


# {
#     "inputs": [
#         "5",
#         "Alice Bob Cacey Deepak Emma",
#         "10 14",
#         "11 12",
#         "10 15",
#         "12 16",
#         "14 16"
#     ],
#     [
#         "3",
#         "Neil Angel Alok",
#         "1 10",
#         "7 9",
#         "7 10"
#     ],
# }

# ti = TimeIntervals()
# print(ti.answer(tc))