from flask import Flask,request,make_response

app = Flask(__name__)

# every route needs to start with a '/'
# static
@app.route('/')
def index():
    return "<h1>My first flask app</h1>"

# static
# methods by default is get but you can specify only post or only get or both
# types of methods: GET to get info, POST to submit info, PUT to update info, DELETE to delete info
# status codes : 200 for assuring that everything worked fine, 300 for redirection, 400 for errors, 500 for server errors
@app.route('/hello', methods=['GET','POST','PUT','DELETE'])
def hello():
    # response = make_response("hello world")
    # response.status_code = 202
    # response.headers['content-type'] = 'text/plain'
    # return response

    if request.method == 'GET':
        return '\nYou made a GET request'
    elif request.method == 'POST':
        return '\nYou made a POST request',201
    elif request.method == 'PUT':
        return '\nYou made a PUT request'
    else:
        return '\nYou made a DELETE request'
    

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
    app.run(host='0.0.0.0', port=5555, debug=True,use_reloader =True)
    # debug =false while its been deployed
