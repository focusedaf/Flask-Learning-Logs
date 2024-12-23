from flask import Flask,render_template

staticfiles = Flask(__name__,template_folder='templates', static_folder='static', static_url_path='/')

# using templates folder html files can be displayed, so to display static files static folder(it consists folders for images,css,script etc) and static url path is required
@staticfiles.route('/')
def index():
    return render_template('staticfile.html')


if __name__ == '__main__':
    staticfiles.run(host ='0.0.0.0', debug = True)