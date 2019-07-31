from flask import Flask,url_for,redirect,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Shiyanlou"

@app.route('/courses/<name>')
def courses(name):
    #return "Courses: {}".format(name)
    return render_template('courses.html',coursename=name)

@app.route('/test')
def test():
    print(url_for('courses',name='java',_external=True))
    return redirect(url_for('index'))

@app.route('/httptest',methods=['GET','POST'])
def httptest():
    met = request.method
    if met=='GET':
        print('t:',request.args.get('t'))
        print('q:',request.args.get('q'))
        return 'It is a get request!'
    else:
        print('Q:',request.form.getlist('Q'))
        return 'It is a post request!'

if __name__ == '__main__':
    app.run()
