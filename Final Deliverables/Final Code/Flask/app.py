
from flask import Flask, render_template, request
from model_cloud import cloud_model

app = Flask(__name__)

@app.route('/')
def load():
    return render_template('Manual_predict.html')

@app.route('/result',methods=['POST'])
def result():
    pred_vals = [float(x) for x in request.form.values()]
    print(pred_vals)
    pred = cloud_model(pred_vals)
    if(pred==0):
        pred_text = "No failure expected within 30 days"
        return render_template('Prediction_no_failure.html',prediction_text_no_failure = pred_text)
    else:
        pred_text = "Maintenance Required! Expected a failure within 30 days"
        return render_template('Prediction_failure.html',prediction_text_failure = pred_text)

if __name__== '__main__':
    app.run(debug=True,port=3000)