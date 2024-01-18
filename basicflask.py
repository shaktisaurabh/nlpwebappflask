from flask import Flask,render_template,request,redirect,session 
import basicnlp1 as bp 
import komprehendner as kp 
import komprehendsent as ks 
import komprehendabuse as ka
app=Flask(__name__) 
app.secret_key='1234' 
@app.route('/wow') 
def index():
    return "Hello ranbanka 266" 
@app.route('/show') 
def index1():
    return "<h1 style='color:green'>Hello mujahid1</h1>" 
@app.route('/html') 
def index2(): 
    return render_template('basichtht.html') 
@app.route('/human') 
def index3():
    return render_template('basicanchor1.html') 
@app.route('/logger') 
def index4():
    return render_template('loginpage.html') 
@app.route('/') 
def index5():
    return render_template('loginpage1.html') 
@app.route('/logincheck',methods=['post']) 
def index9():
    email=request.form.get('user_ka_email') 
    password=request.form.get('user_ka_pass') 
    new=bp.checkinglogin(email,password) 
    if new:
        session['logged_in']=1
        return redirect('/profile') 
    else:
        return render_template('loginpage1.html',message='Incorrect email or password') 
@app.route('/profile') 
def dumdum():
    if session:
        return render_template('profilekar1.html') 
    else:
        return render_template('/')

@app.route('/nlpkarkar') 
def mandu():
    if session:
       return render_template('nlpkar1.html') 
    else:
        return render_template('/') 

@app.route('/nlpkarkar1',methods=['post']) 
def mandu24():
    if session:
       a1=request.form.get('psyop') 
       response=kp.kompner(a1)  
       return render_template('nlpkar1.html',message=response) 
    else:
        return render_template('/') 


@app.route('/sentanalysis') 
def mandu1():
    if session:
       return render_template('sentanalysis.html') 
    else:
        return render_template('/') 
    
@app.route('/santu1',methods=['post']) 
def man25():
    if session:
        a1=request.form.get('psyop1') 
        response=ks.komsent(a1) 
        return render_template('sentanalysis.html',message=response) 
    else:
        return render_template('/')



@app.route('/abusedetection') 
def mandu2():
    return render_template('abusedetection.html') 

@app.route('/abusal',methods=['post']) 
def rameshwar():
    if session: 
        a1=request.form.get('psyop2') 
        response=ka.komabuse(a1)  
        return render_template('abusedetection.html',response=response) 
    else:
        return render_template('/')  



@app.route('/register') 
def index6():
    return render_template('registration.html') 
@app.route('/checker',methods=['post'])
def index7():
    name=request.form.get('user_ka_name') 
    email=request.form.get('user_ka_email')
    password=request.form.get('user_ka_pass') 
    return name+" "+email+" "+password  
@app.route('/checker1',methods=['post']) 
def index8():
    name=request.form.get('user_ka_name') 
    email=request.form.get('user_ka_email') 
    password=request.form.get('user_ka_pass') 
    amn=bp.uniquer(email,name,password) 
    if amn:
        return render_template('loginpage1.html',message='Successfully Registered!kindly login') 
    else:
        return render_template('registration.html',message='Email already exists')  


if __name__=='__main__':
    app.run(debug=True) 
#flask sets a web server that responds with the execution of a particular function when the 
#user accesses the root path('/' in this case). The app.run() method starts the development 
#server. 
#flask sets a web server that responds with the execution of a particular function when the 
#user accesses the root path('/' in this case). The app.run() method starts the development
#server. 
#flask sets a web server that responds with the execution of particular function when the 
#user accesses the root path('/' in this case). The app.run() method sets the development
#server.
#app=Flask(__name__) creates an instance of Flask class. __name__ here is a special variable
#in python that represents the name of the current module. __name__ is set to __main__ when the
#main module is being executed, when this module is imported then __name__ is set to the name
#of that respective module. 
#@app.route('/')
#def index():
#    return "Hello ranbanka"  This block of code is a flask route decorator. It tells Flask
#that index() function should be called when the user accesses the route path which is '/'
#in this case. The @app.route('/') decorator associates the index() function with this route
#path. 
#When the user accesses the root path('/'), Flask will invoke the index() function as response
#to the user's browser. 
#The line app.run() method starts a development server loally on local host(127.0.0.1) and
#port 5000. This is only for development purposes, for production purposes we use production 
#ready servers. 
#The advantage of debug=True in app.run() method is that when debug=True is done the server
#may not be restarted again and again in order to reflect changes in the code to the client
#side. The code can just be saved using cntrl+s and the change will automatically get 
#reflected to the client side. In this case of development server the server is vscode and 
#client is web browser. 
#What the client sees(google chrome in this case) is actually a HTML template. HTML is used
#for creating structure and layout for the web pages
#Instead of writing a plain string to the web-page, we can modify it using HTML 
#like this ,return <h1 style='color:green'>Hello ranbanka</h1>. The other way of doing that
#is using render_template() method of flask.... This method loads a HTML template to the
#web-page. 
    
#In html page <h1>,<h2>.....<h6> corresponds to headings and <h1> is the biggest heading while
#<h6> is the smallest heading. <p> tag is for paragraphs and <a> is a anchor tag which is used
#to create links and is used to navigate from one web-page to the other. 
    
#form action defines the URL to which form data should be submitted once the user presses the
#submit button. If the method is set to get then the data submitted can be seen in the URL
#itself and if the method is set to post then data submitted can not be seen in the URL itself.

#If you have to receive the information of HTML page(client page that is browser in this case)
#into the server(basicflask.py in this case), we have to use methods=['post'] and then 
#receive values of name,email and password using request.form.get('name') and then we call 
#a function using these arguments.  
    
# nvL4UbtjIMLtusckrfOgkUDQQcXaPsgnae2X5QXeHs4 

#session['logged_in']=1 after a user has been successfully logged in is used to ensure that 
#a web-page is not been accessed even in the incognito mode by a user who hasnot even logged-in
#sucessfully. 
    
#{% if message %} and {% for i in response %} this is jinja technique used for writing python
#code in html. 