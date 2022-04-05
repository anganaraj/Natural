from flask import Flask,render_template,request,session
from DBConnection import Db
app = Flask(__name__)
app.secret_key = 'hi'




@app.route('/')
def admin_add_login():
    return render_template("login.html")
@app.route('/signup')
def gggg():
    return render_template("login.html")
@app.route('/login_post',methods=['post'])
def login_post():
    username=request.form["textfield"]
    password = request.form["textfield2"]
    db=Db()
    qry="select * from login WHERE username='"+username+"' and password='"+password+"'"
    res=db.selectOne(qry)
    if res!=None:
        session['login_id']= res['lid']

        type=res['type']
        
        return render_template("admin/admin_home.html")

        
    else:
        return '''<script>alert('Invalid User');window.location='/'</script>'''

@app.route('/signup_post',methods=['post'])
def signup_post():
    name=request.form["textfield"]
    dob = request.form["textfield1"]
    place=request.form["textfield2"]
    phone = request.form["textfield3"]
    email=request.form["textfield4"]
    password = request.form["textfield5"]
    db=Db()
    qry="insert into login(username,password,type)values('"+email+"','"+password+"','user')"
    lid=str(db.insert(qry))
    qry="insert into user(lid,name,dob,phone,place,email)values('"+lid+"','"+name+"','"+dob+"','"+phone+"','"+place+"','"+email+"')"
    db.insert(qry)

        
    
    return '''<script>alert('Succeesss');window.location='/'</script>'''




@app.route('/st')
def st():
    return render_template("admin/senti.html")

    
@app.route('/sentipost')
def sentipost():
    a=request.form["name"]
    return render_template("admin/senti.html")
if __name__ == '__main__':
    app.run(debug=True)