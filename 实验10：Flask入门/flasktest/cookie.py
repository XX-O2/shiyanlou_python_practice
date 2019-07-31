from flask import Flask,render_template,request,make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cookie_index.html')

@app.route('/setcookie',methods=['GET','POST'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
        # TODO:
        # 1. 响应返回readcookie.html页面
        # 2. 设置一个cookie的键为userID,值为user
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID',user)
        return resp

@app.route('/getcookie')
def getcookie():
    # TODO:
    # 1.获取 userID 的 cookie,并赋值给 name
    name = request.cookies.get('userID')
    return '<h1>welcome, '+name+'</h1>'
