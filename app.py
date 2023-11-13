from flask import Flask
from flask import request
from modules.TestQuestion import TestQuestion
from modules.CalendarScheduling import CalendarScheduling
from modules.CoinChange import CoinChange

app = Flask(__name__)

# global cs = CalendarScheduling()
cs = CalendarScheduling()
coinChange = CoinChange()

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
    return coinChange.answer(data)