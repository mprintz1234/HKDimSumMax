from flask import Flask
from flask import request
from modules.TestQuestion import TestQuestion
from modules.CalendarScheduling import CalendarScheduling
from modules.CoinChange import CoinChange
from modules.FileReorganization import FileReorganization
from modules.TimeIntervals import TimeIntervals
from modules.PortfolioOperations import PortfolioOperations
from modules.DataEncryption import DataEncryption
from modules.RiskMitigation import RiskMitigation
from modules.ProfitMaximization import ProfitMaximization
from modules.mlmm import MLMM
from modules.FraudulentTransactions import Fraud

app = Flask(__name__)

# global cs = CalendarScheduling()
cs = CalendarScheduling()
coinChangeModule = CoinChange()
fr = FileReorganization()
ti = TimeIntervals()
po = PortfolioOperations()
de = DataEncryption()
rm = RiskMitigation()
pm = ProfitMaximization()
mlmm = MLMM()
ft = Fraud()

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

@app.route('/data-encryption', methods = ['POST'])
def DataEncryption():
    data = request.get_json()
    return de.answer(data)

@app.route('/risk-mitigation', methods = ['POST'])
def RiskMitigation():
    data = request.get_json()
    return rm.answer(data)

@app.route('/profit-maximization', methods = ['POST'])
def ProfitMaximization():
    data = request.get_json()
    return pm.answer(data)

@app.route('/mlmm-program', methods = ['POST'])
def MLMM():
    data = request.get_json()
    return mlmm.answer(data)

@app.route('/fraudulent-transactions', methods = ['POST'])
def Fraud():
    data = request.get_json()
    return ft.answer(data)