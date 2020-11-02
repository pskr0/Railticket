import numpy as np
import datetime
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/recheck',methods=['POST','GET'])
def recheck():
    return render_template('index.html')


@app.route('/loginacc',methods=['POST','GET'])
def loginacc():
    return render_template('login.html')

@app.route('/filedata',methods=['POST','GET'])
def filedata():
    return render_template('files.html')
@app.route('/cvr.ac.in',methods=['POST','GET'])
def cvrweb():
    return redirect(url_for('http://cvr.ac.in/home4/'))

@app.route('/code_login')
def codelogin():
    return render_template('code_login.html')



@app.route('/predict',methods=['POST','GET'])
def predicts():  
    source00 = request.form['sourcename']
    destination00=request.form['destinationname']
    projectpath = request.form['inputdata']
    
    a=int(str(projectpath))
    aa=a+1
    aaa=a+2
    aaaa=a+3
    aaaaa=a+4

    projectpath1=str(int(aa))
    projectpath2=str(int(aaa))
    projectpath3=str(int(aaaa))
    projectpath4=str(int(aaaaa))

    prediction = model.predict(projectpath)
    prediction1 = model.predict(projectpath1)
    prediction2 = model.predict(projectpath2)
    prediction3 = model.predict(projectpath3)
    prediction4 = model.predict(projectpath4)
    output = round(prediction[0]*10, 3)
    output1 = round(prediction1[0]*10, 3)
    output2 = round(prediction2[0]*10, 3)
    output3 = round(prediction3[0]*10, 3)
    output4 = round(prediction4[0]*10, 3)
    
    return render_template('conform.html',Date0="DATE [YYYY/MM/DD]",head2="PROBABILITY OF COMFORMATION",prediction_text='{} %'.format(output),pred='{} %'.format(output1),source0='{} =========>>>>'.format(source00),destination0="==========>>>> {}".format(destination00),dat0="{} ".format(projectpath),dat1="{} ".format(projectpath1),dat2="{} ".format(projectpath2),dat3=" {}".format(projectpath3),dat4="{} ".format(projectpath4),pred1='{} %'.format(output2),pred2='{} %'.format(output3),pred3='{} %'.format(output4))

if __name__ == "__main__":
     #app.run(debug=True)
     app.run(host="0.0.0.0",port=6442)
