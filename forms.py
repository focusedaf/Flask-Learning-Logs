from flask import Flask, render_template,request,jsonify

forms = Flask(__name__, template_folder='templates')

@forms.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('forms.html')
    elif request.method == 'POST': 
        # from the following statements we are trying to retrieve the data from the form .get() and .form[] both have the same functionality
        username = request.form.get('username')
        password = request.form['password']

        # handling username and password
        if username == 'morpheus' and password =='jamy@99':
            return 'Success'
        else:
            return 'Failure'

@forms.route('/file_upload', methods =['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        # since it would be in binary 
        return file.read().decode()
    else:
        return ""

@forms.route('/handle_post', methods =['POST'])
def handle_post():
    greeting = request.json['greeting']
    name = request.json['name']

    with open('hello.txt','w') as f:
        f.write(f'{greeting}, {name}')
        
    return jsonify({'message':'successfully written'})



if __name__ == '__main__':
    forms.run(host = '0.0.0.0', debug = True)