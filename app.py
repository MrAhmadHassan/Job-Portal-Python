from flask import Flask, render_template,request,redirect,url_for
from dummydata import job_posts
from databaseConnection import createUser,loginUser,loginAdmin,createjob
app = Flask(__name__)


@app.route('/')
def index():
    length = len(job_posts)
    return render_template('index.html',jobs=job_posts,length = length)

@app.route('/adminlogin',methods=['GET', 'POST'])
def adminLogin():
    error = ''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user=loginAdmin(email,password)
        if user==None:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('dashboard'))
        

    return render_template('adminLogin.html',message=error)
   

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/post',methods=["post"])
def post():
    message = ''
    title = request.form.get('title')
    description = request.form.get('description')
    location = request.form.get('location')
    salary = request.form.get('salary')
    res = createjob(title,description,location,salary)
    if res is True:
        return redirect(url_for('dashboard'))         
    return redirect(url_for('dashboard'))

@app.route('/signup',methods=['post'])
def addUser():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    res = createUser(name,email,password)
    
    if res is True:
        return redirect('/login')
    else:
        message="User already exists with this account"
        return render_template('signup.html',message=message)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginController',methods=['post'])
def loginController():
    email = request.form.get('email')
    password = request.form.get('password')
    user=loginUser(email,password)
    message="Invalid Email or password,please login again"
    print(user)
    if user!=None:
        return redirect(url_for('index',user=user))
    else:
        return redirect(url_for('login',message=message))

if __name__ == '__main__':
    app.run(debug=True)