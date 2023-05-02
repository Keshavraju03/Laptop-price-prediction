from flask import Flask, render_template, request,url_for
import pickle
import numpy as np

# setup application
app = Flask(__name__)

def prediction(lst):
    filename = 'modal/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    # return "Hello World"
    pred_value = 0
    if request.method == 'POST':
        ram = request.form['ram']
        hdd = request.form['HDD']
        ssd = request.form['SSD']
        ssize = request.form['ScreenSize']
        company = request.form['company']
        cpu = request.form['cpuname']
        gpu = request.form['gpuname']
        ms = request.form.getlist('MsOffice')

        
        feature_list = []

        feature_list.append(int(ram))
        feature_list.append(int(hdd))
        feature_list.append(int(ssd))
        feature_list.append(int(ssize))
        feature_list.append(len(ms))


        company_list = ['APPLE','ASUS','DELL','HP','Lenovo','MSI','acer','other']
        cpu_list = ['Core i3','Core i5','Core i7','Core i9','M1 Max','M1 Pro','M1 Processor','M2 Max','M2 Pro','M2 Processor','Ryzen 3','Ryzen 5','Ryzen 7','Ryzen 9','other']
        gpu_list = ['AMD','Apple','Intel','MediaTek']

        
        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        
        traverse_list(company_list, company)
        traverse_list(cpu_list, cpu)
        traverse_list(gpu_list, gpu)

        pred_value = prediction(feature_list)
        pred_value = np.round(pred_value[0],2)

    return render_template('index.html', pred_value=pred_value)

# extra code for testing


if __name__ == '__main__':
    app.run(debug=True)