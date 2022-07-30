import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('/content/drive/My Drive/multiregression.pkl','rb'))

@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    '''
    For rendering results on HTML GUI
    
    '''
    area = float(request.args.get('area'))
    bed = int(request.args.get('bed'))
    bath = int(request.args.get('bath'))
    offer = int(request.args.get('offer'))
    brick = (request.args.get('brick'))

    if brick=="Yes":
      brick = 1
    else:
      brick = 0

    neighbour = (request.args.get('neighbour'))

    if neighbour=="North":
      neighbour = 1
    elif neighbour=="East":
      neighbour = 0
    else:
      neighbour = 2

    
    
    prediction = model.predict([[area, bed, bath, offer, brick, neighbour]])
    
        
    return render_template('index.html', prediction_text='Regression Model  has predicted the price of home based on various parameters is {}'.format(prediction))

if __name__ == "__main__"
app.run(debug =True)

# print("the predicted price is : %.f"  %(regressor.predict([[2190.0,3,3,3,1,1]])))
