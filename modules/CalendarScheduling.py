import copy


# data = [{
#     "lessonRequestId": "LR1",
#     "duration": 1,
#     "potentialEarnings": 100,
#     "AvailableDays": ["monday", "wednesday"]
# }, {
#     "lessonRequestId": "LR2",
#     "duration": 2,
#     "potentialEarnings": 50,
#     "AvailableDays": ["monday"]
# }, {
#     "lessonRequestId": "LR3",
#     "duration": 12,
#     "potentialEarnings": 1000,
#     "AvailableDays": ["wednesday"]
# }, {
#     "lessonRequestId": "LR4",
#     "duration": 13,
#     "potentialEarnings": 10000,
#     "AvailableDays": ["friday"]
# }]

class CalendarScheduling():

    def answer(self, data):
        pq = []
        datamap = {}
        dp = [[{"value": 0, 
        "res": {
            "monday": [],
            "tuesday": [],
            "wednesday": [],
            "thursday": [],
            "friday": [],
            "saturday": [],
            "sunday": [],
        },
        "availability": {
            "monday": 12,
            "tuesday": 12,
            "wednesday": 12,
            "thursday": 12,
            "friday": 12,
            "saturday": 12,
            "sunday": 12,
        }
        }]]


        for d in data:
            pq.append((d["duration"]*d["potentialEarnings"], d["lessonRequestId"]))
            datamap[d["lessonRequestId"]] = d

        for p in pq:
            tmp = []

            currObj = datamap[p[1]]
            for day in currObj["availableDays"]:
                for option in dp[-1]:
                    newOption = copy.deepcopy(option)
                    availableTime = option["availability"][day]
                    if availableTime - currObj["duration"] >= 0:
                        newOption["availability"][day] = availableTime - currObj["duration"]
                        newOption["value"] += p[0]
                        newOption["res"][day].append(p[1])
                        tmp.append(newOption)
            
            if len(tmp) == 0:
                break
            else:
                dp.append(tmp)
            

        maxValue = 0
        res = {}
        for ans in dp[-1]:
            if ans["value"] > maxValue:
                res = ans["res"]
        
        out = {}
        for k in res.keys():
            if len(res[k]) > 0:
                out[k] = res[k]
        print(maxValue)
        return out
