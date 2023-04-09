from flask import Flask, request, render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
import pickle

with open('src/model.pkl', 'rb') as f:
    gnb = pickle.load(f)

with open('src/vec.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/predict', methods=["GET", "POST"])
def predict():

    text = request.args.get('text')

    features = vectorizer.transform([text])

    prediction = gnb.predict(features.toarray())

    #return str(prediction[0])

    return render_template('predict.html', prediction=prediction[0])

app.run(debug=True)