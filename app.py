from flask import Flask,request

app = Flask(__name__)

# every route needs to start with a '/'
# static
@app.route('/')
def index():
    print("hello world")
    return "<h1>My first flask app</h1>"

# static
@app.route('/hello')
def hello():
    return "Hello World"

# url processors = dynamic urls
@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return f"sum is {num1+num2}"

@app.route('/handle_url_params')
def handle_params():
    # since its dic you can write it using [] or even .get() is also feasible
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f"{greeting}, {name}"
    else:
        return 'some parameters are missing'    



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)
    # debug =false while its been deployed
