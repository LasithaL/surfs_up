# Import the dependancies
from flask import Flask

# Create New Flask App Instance
app = Flask(__name__)

# Create Flask Routes and create a function called hello_world()
@app.route('/')
def hello_world():
    return 'Hello World'
