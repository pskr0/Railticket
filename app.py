import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predicts():
    projectpath = request.form['inputdata']
    #int_features = [str(x) for x in request.form.values()]
    #projectpath = request.form('miniresult')
    #final_features = [np.array(int_features)]
    a=int(str(projectpath))
    aa=a+1
    aaa=a+2
    aaaa=a+3
    projectpath1=str(int(aa))

    prediction = model.predict(projectpath)
    prediction1 = model.predict(projectpath1)
    #prediction2 = model.predict(projectpath2)
    #prediction3 = model.predict(projectpath3)
    #prediction4 = model.predict(projectpath4)
    #prediction = model.predict(projectpath)
    #prediction = model.predict(projectpath)
    output = round(prediction[0]*10, 3)
    output1 = round(prediction1[0], 3)
    #output2 = round(prediction[0], 3)
    #output3 = round(prediction[0], 3)
    #output4 = round(prediction[0], 3)
    

    #output = round(prediction[0], 3)
    #output1=output
    return render_template('index.html', prediction_text='Ticket Conformation Probability {}'.format(output))
    render_template('index.html', pred1='Ticket Conformation  $ {}'.format(output1))
    #return render_template('index.html', pred1='Ticket Conformation Should be  $ {}'.format(output2))
    #return render_template('index.html', pred2='Ticket Conformation Should be  $ {}'.format(output3))
    #return render_template('index.html', pred3='Ticket Conformation Should be  $ {}'.format(output4))
    #return render_template('index.html', pred4='Ticket Conformation Should be  $ {}'.format(output))



#@app.route('/results',methods=['POST'])
#def results():

    #data = request.get_json(force=True)
    #prediction = results.predict(start="projectpath")

    #output = prediction[0]
    #return jsonify(output)

if __name__ == "__main__":
     #app.run(debug=True)
     app.run(host="0.0.0.0",port=6442)
