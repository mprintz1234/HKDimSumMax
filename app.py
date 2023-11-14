from flask import Flask
from flask import request
from modules.TestQuestion import TestQuestion
from modules.CalendarScheduling import CalendarScheduling
from modules.CoinChange import CoinChange
from modules.FileReorganization import FileReorganization

app = Flask(__name__)

# global cs = CalendarScheduling()
cs = CalendarScheduling()
coinChangeModule = CoinChange()
fr = FileReorganization()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return cs.get_input()

# @app.route('/calendar-scheduling', methods = ['POST'])
# def calendarScheduling():
#     data = request.get_json()
#     cs.set_input(data)
#     print(len(data))
#     return cs.answer(data)

# @app.route('/digital-colony', methods = ['POST'])
# def digitalColony():
#     data = request.get_json()
#     cs.set_input(data)
#     print(len(data))
#     return cs.answer(data)


@app.route('/coin-change',  methods = ['POST'])
def coinChange():
    data = request.get_json()
    return coinChangeModule.answer(data)

@app.route('/file-reorganization', methods = ['POST'])
def FileReorganization():
    data = request.get_json()
    return fr.answer(data)