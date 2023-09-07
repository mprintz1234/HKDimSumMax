from flask import Flask
from flask import request
from modules.TestQuestion import TestQuestion
from modules.CalendarScheduling import CalendarScheduling

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return TestQuestion().answer()

@app.route('/calendar-scheduling', methods = ['POST'])
def calendarScheduling():
    cs = CalendarScheduling()
    data = request.get_json()
    print(len(data))
    return cs.answer(data)
