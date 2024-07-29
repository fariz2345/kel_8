from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('estimasi_pertumbuhan.pkl', 'rb')
model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html', panjang_ikan=0, berat_ikan=0)

@app.route('/predict', methods=['POST'])
def predict():
    temperatur_udara = request.form['temperatur_udara']
    kelembapan = request.form['kelembapan']
    curah_hujan = request.form['curah_hujan']
    suhu_air = request.form['suhu_air']

    data = [int(x == '1') for x in [temperatur_udara, kelembapan, curah_hujan, suhu_air]]

    prediction = model.predict([data])
    panjang_ikan = round(prediction[0][0], 1)
    berat_ikan = round(prediction[0][1], 1)

    return render_template('index.html', panjang_ikan=panjang_ikan, berat_ikan=berat_ikan, 
                           temperatur_udara=temperatur_udara, 
                           kelembapan=kelembapan, 
                           curah_hujan=curah_hujan, 
                           suhu_air=suhu_air)

if __name__ == '__main__':
    app.run(debug=True)