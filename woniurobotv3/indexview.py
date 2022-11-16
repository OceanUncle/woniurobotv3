from flask import jsonify

from woniurobotv3 import app,render_template,request


@app.route('/')
def index():
    return render_template('login.html')
@app.route('/login',methods=('GET','POST'))
def login():
    if request.method=='POST':
        app.logger.info(request.form['username'])
        app.logger.info(request.form['password'])
        return render_template('regist.html')
    else:
        return render_template('login.html')