from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'baidu'


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        print password

    if not all([username,password,password2]):
        flash(u'参数不完整')

    elif password != password2
        flash('密码不一样')

    else:
        return 'success'

 retrun render_template('index.html')


    url_str = 'www.baidu.com'

    return render_template('index.html', url_str=url_str)

if __name__ == '__main__':
    app.run(debug=True)
