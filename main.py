from flask import Flask, render_template, json, request, redirect, url_for, flash
from flask_cors import CORS, cross_origin
import driver
import Rainfall
import alerter

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


app.secret_key = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SECRET_KEY']='5791628bb0b13ce0c676dfde280ba245'

# @app.route('/')
# def home():
#     return render_template('main.html')

@app.route('/refreshFlood')
def refreshFlood():
    alerter.water_level_predictior()  # To refresh the flood warning data
    return redirect(url_for('floodHome'))

@app.route('/floodHome')
def floodHome():
    res = alerter.alerting()
    for i in range(len(res)):
        res[i] = 'Flood ALERT for '+res[i]
    return render_template('flood_entry.html', result=res)


@app.route('/rainfallHome')
def rainfallHome():
    return render_template('rain_entry.html')


@app.route('/floodResult', methods=['POST', 'GET'])
def floodResult():
    if request.method == 'POST':
        if len(request.form['DATE']) == 0:
            return redirect(url_for('floodHome'))
        else:
            user_date = request.form['DATE']
            river = request.form['SEL']
            results_dict = driver.drive(river, user_date)
            print("-----------", type(results_dict), "----------")
            Table = []
            for key, value in results_dict.items():
                Table.append(value)
            return render_template('flood_result.html', result=Table)
    else:
        return redirect(url_for('floodHome'))


@app.route('/rainfallResult', methods=['POST', 'GET'])
def rainfallResult():
    if request.method == 'POST':
        if len(request.form['Year']) == 0:
            flash("Please Enter Data!!")
            return redirect(url_for('rainfallHome'))
        else:
            year = request.form['Year']
            region = request.form['SEL']
            print("##3#######", year, "#####", region, "#############")
            mae, score = Rainfall.rainfall(year, region)
            return render_template('rain_result.html', Mae=mae, Score=score)
    else:
        return redirect(url_for('rainfallHome'))


@app.route('/predict', methods=['POST', 'GET'])
@cross_origin()
def predict():
    user_date = request.form['Date']
    river = request.form['River']
    print(river, user_date)

    results_dict, classification_metrics, data, fut = driver.drive(
        river, user_date)

    if fut is 0:
        data["Date"] = data["Date"].astype(str)
        results_dict["Data"] = data.to_dict()

    results_dict["Classification Report"] = classification_metrics

    response = app.response_class(
        response=json.dumps(results_dict),
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5000)
