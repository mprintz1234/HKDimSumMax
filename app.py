from flask import Flask
from flask import request
from modules.TestQuestion import TestQuestion
from modules.CalendarScheduling import CalendarScheduling

app = Flask(__name__)

# global cs = CalendarScheduling()
cs = CalendarScheduling()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return cs.get_input()

@app.route('/calendar-scheduling', methods = ['POST'])
def calendarScheduling():
    data = request.get_json()
    cs.set_input(data)
    #print(len(data))
    #return cs.answer(data)