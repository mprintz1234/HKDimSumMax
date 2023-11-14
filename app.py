from flask import Flask
from flask import request
from modules.TestQuestion import TestQuestion
from modules.CalendarScheduling import CalendarScheduling
from modules.CoinChange import CoinChange
from modules.FileReorganization import FileReorganization
from modules.TimeIntervals import TimeIntervals
from modules.PortfolioOperations import PortfolioOperations

app = Flask(__name__)

# global cs = CalendarScheduling()
cs = CalendarScheduling()
coinChangeModule = CoinChange()
fr = FileReorganization()
ti = TimeIntervals()
po = PortfolioOperations()

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

@app.route('/time-intervals', methods = ['POST'])
def TimeIntervals():
    data = request.get_json()
    return ti.answer(data)

@app.route('/portfolio-operations', methods = ['POST'])
def PortfolioOperations():
    data = request.get_json()
    return po.answer(data)