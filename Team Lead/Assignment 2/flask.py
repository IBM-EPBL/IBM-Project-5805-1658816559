from flask import Flask
app=Flask(__name__)
app.secret_key="123"

class User:
    def _init_(self,id,username,password):
        self.id=id
        self.username=username
        self.password=password
        
users=[]
users.append(User(id=1,username='dhanush',password='dhanush@23'))
users.append(User(id=2,username='srivatsan',password='srivatsan@122'))
users.append(User(id=3,username='rony',password='rony@28'))

@app.route("/",methods=['GET','POST'])
def login():
    if request.method=='POST':
        uname=request.form['uname']
        upass = request.form['upass']
        
        for data in users:
            if data.username==uname and data.password==upass:
                session['userid']=data.id
                g.record=1
                return redirect(url_for('user'))
            else:
                g.record=0
        if g.record!=1:
            flash("Username or Password Mismatch...!!!",'danger')
            return redirect(url_for('login'))
    return render_template("login.html")

@app.before_request
def before_request():
    if 'userid' in session:
        for data in users:
            if data.id==session['userid']:
                g.user=data
                
@app.route('/user')
def user():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('user.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)