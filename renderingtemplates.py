from flask import Flask, redirect, render_template, url_for

renderingtemplates = Flask(__name__,template_folder='templates')

@renderingtemplates.route('/')
def index(): 
    favline = "I remember you was conflicted"
    favmc = "Kdot" 
    mylist = ["10","20","30", "40"]
    mytuple = (1,2,3,4,5)
    # the rhs doesnt matter while you are passing the values to the render_template()
    return render_template('index.html', a = favline , b = favmc, c = mylist, d = mytuple)

@renderingtemplates.route('/other')
def other():
    newvalue = "Hola!!"
    return render_template('other.html', newvalue = newvalue)
# if the url of endpoint other is going to be changed in the future then you can just link other() in index.html

# reidrects to other endpoint
@renderingtemplates.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))


# creating your own filters

@renderingtemplates.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@renderingtemplates.template_filter('repeat')
def reverse_string(s, times = 2):
    return s * times



if __name__ == '__main__':
    renderingtemplates.run(host = '0.0.0.0', debug = True)