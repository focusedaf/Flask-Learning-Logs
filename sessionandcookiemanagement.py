from flask import Flask, make_response, render_template, session, request, flash

app = Flask(__name__, template_folder='templates')
# in order to use sessions for encryption purposes you will be requiring a secret key. using this key you can give users session id and keep track of indivdiual users/clients on the server side
app.secret_key = 'morpheus'

# cookies are for client side and sessions are for server side both are used to keep track of information for multiple requests since http in general is stateless and its mostly request and response based and there is no state which is present to keep track of this overall exchange


@app.route('/')
def index():
    return render_template('sessionandcookiemanagement.html', message = "you just got hopson'd")

@app.route('/set_data')
def set_data():
    session['name'] = 'Mike'
    session['other'] = 'Hello'
    return render_template('sessionandcookiemanagement.html', message ='session data set')


@app.route('/get_data')
def get_data():
    if 'name'in session.keys() and 'other' in session.keys():
        name = session['name'] 
        other = session['other'] 
        return render_template('sessionandcookiemanagement.html', message =f'Name: {name}, Other:{other}')
    else:
        return render_template('sessionandcookiemanagement.html',message ='No session found')

@app.route('/clear_session')
def clear_session():
    session.clear()
    # popping individual sessions
    # session.pop('other')
    return render_template('sessionandcookiemanagement.html',message ='session cleared')

@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('sessionandcookiemanagement.html', message='Cookie Set'))
    response.set_cookie('cookie_name','cookie_value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('sessionandcookiemanagement.html', message = f'Cookie Value: {cookie_value}')

@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('sessionandcookiemanagement.html', message=' Cookie Removed'))
    # default value is empty string for cookie_value
    response.set_cookie('cookie_name', expires = 0)
    return response

@app.route('/login', methods =['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'mike' and password == '12345':
        flash('Login Successful!')
        return render_template('sessionandcookiemanagement.html')
    else:
        flash('Login Failed!')
        return render_template('sessionandcookiemanagement.html')

if __name__ == '__main__':
    app.run(host ='0.0.0.0', debug=True)