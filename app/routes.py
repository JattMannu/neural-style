from app import app
import method_test;

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"



@app.route('/run')
def run():
    return method_test.sa();
    # return "running"
