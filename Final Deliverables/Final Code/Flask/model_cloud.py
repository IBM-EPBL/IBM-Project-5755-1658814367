import requests

def cloud_model(data):
    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
    API_KEY = "gDD09sX6I55MvqO0c92YsKLieC7VDgMLCKK1MbCuTii0"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
    API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field": ['id','cycle','setting1','setting2','setting3','s1','s2','s3','s4','s5',
                                                 's6','s7','s8','s9','s10','s11','s12','s13','s14','s15','s16','s17','s18',
                                                 's19','s20','s21','ttf'], "values": [data]}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/ibmclouddep/predictions?version=2022-11-19', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    prediction_val = response_scoring.json()
    return prediction_val['predictions'][0]['values'][0][0]

predict_val = [ 2.70000e+01,  1.08000e+02, -4.80000e-03,  0.00000e+00,
        1.00000e+02,  5.18670e+02,  6.42500e+02,  1.58658e+03,
        1.41020e+03,  1.46200e+01,  2.16100e+01,  5.53290e+02,
        2.38810e+03,  9.07818e+03,  1.30000e+00,  4.74700e+01,
        5.21280e+02,  2.38810e+03,  8.15268e+03,  8.44090e+00,
        3.00000e-02,  3.94000e+02,  2.38800e+03,  1.00000e+02,
        3.87300e+01,  2.33405e+01,  4.80000e+01]

