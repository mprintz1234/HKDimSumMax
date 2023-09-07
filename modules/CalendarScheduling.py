import copy
import json

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

def fast_copy(d):
    output = d.copy()
    for key, value in output.items():
        output[key] = fast_copy(value) if isinstance(value, dict) else value        
    return output

class CalendarScheduling():
    input_str = ""

    def set_input(self, inp):
        self.input_str = inp

    def get_input(self):
        return self.input_str

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

        for p in sorted(pq, reverse=True):
            tmp = []
            maxVal = 0
            currObj = datamap[p[1]]
            for day in currObj["availableDays"]:
                for option in dp[-1]:
                    # newOption = copy.deepcopy(option)
                    availableTime = option["availability"][day]
                    if availableTime - currObj["duration"] >= 0:
                        if option["value"] + p[0] >= maxVal:
                            maxVal = option["value"] + p[0]

                for option in dp[-1]:
                    if option["value"] + p[0] == maxVal:
                        newOption = json.loads(json.dumps(option))
                        newOption["availability"][day] = availableTime - currObj["duration"]
                        newOption["value"] += p[0]
                        newOption["res"][day].append(p[1])
                        tmp.append(newOption)
                        
            if len(tmp) == 0:
                continue
            else:
                newTmp = []
                for t in tmp:
                    if t["value"] == maxVal:
                        newTmp.append(t)
                del dp
                dp = [newTmp]
            

        maxValue = 0
        res = {}
        for ans in dp[-1]:
            if ans["value"] > maxValue:
                res = ans["res"]
            maxValue = ans["value"]
        
        out = {}
        for k in res.keys():
            if len(res[k]) > 0:
                out[k] = res[k]
        print(maxValue)
        return out
