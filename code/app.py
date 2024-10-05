# import numpy as np
# import pandas as pd
# from flask import Flask, request, render_template
# import pickle
#
# app = Flask(__name__,template_folder='templates')
# #load model
#
# model = pickle.load(open("model.pkl", 'rb'))
# train_data = pd.read_csv(r"C:\Users\Heena\project\dataset\survey.csv")
# xx = train_data.drop('treatment', axis=1)
# y_train = train_data['treatment'].copy()
#
# @app.route('/')
# def home():
#      #result = ''
#      return render_template('home.html', **locals())
#
# @app.route('/home', methods=['POST','GET'])
#
# def predict():
#     age = int(request.form['age'])
#     gender = request.form['gender']
#     self_employed = request.form['self_employed']
#     family_history = request.form['family_history']
#     work_interfere = request.form['work_interfere']
#     no_employees = request.form['no_employees']
#     remote_work = request.form['remote_work']
#     tech_company = request.form['tech_company']
#     benefits = request.form['benefits']
#     care_options = request.form['care_options']
#     wellness_program = request.form['wellness_program']
#     seek_help = request.form['seek_help']
#     anonymity = request.form['anonymity']
#     leave = request.form['leave']
#     mental_health_consequence = request.form['mental_health_consequence']
#     phys_health_consequence = request.form['phys_health_consequence']
#     coworkers = request.form['coworkers']
#     supervisor = request.form['supervisor']
#     mental_health_interview = request.form['mental_health_interview']
#     phys_health_interview = request.form['phys_health_interview']
#     mental_vs_physical = request.form['mental_vs_physical']
#     obs_consequence = request.form['obs_consequence']
#
#     if gender == 'Male':
#         g = 0
#     elif gender == 'Female':
#         g = 1
#     else:
#         g = 2
#     if self_employed == 'Yes':
#         se = 1
#     else:
#         se = 0
#     if family_history == 'Yes':
#         fh= 1
#     else:
#         fh = 0
#     if work_interfere == 'Yes':
#         wi = 1
#     else:
#         wi = 0
#     if no_employees == '1-25':
#         ne = 1
#     elif no_employees == '6-25':
#         ne = 2
#     elif no_employees == '26-100':
#         ne = 3
#     elif no_employees == '100-500':
#         ne = 4
#     elif no_employees == '500-1000':
#         ne = 5
#     else:
#         ne = 6
#     if remote_work == 'Yes':
#         rw = 1
#     else:
#         rw = 0
#     if tech_company == 'Yes':
#         tc = 1
#     else:
#         tc=0
#     if benefits == 'Yes':
#         b = 1
#     elif benefits == "Don't know":
#         b = 2
#     else:
#         b = 0
#     if care_options == 'yes':
#         co = 1
#     elif care_options == 'Not sure':
#         co = 2
#     else:
#         co = 0
#     if wellness_program == 'Yes':
#         wp = 1
#     elif wellness_program == "Don't kow":
#         wp = 2
#     else:
#         wp = 0
#     if seek_help == 'Yes':
#         sh = 1
#     else:
#         sh =0
#     if anonymity == 'Yes':
#         a = 1
#     elif anonymity == "Don't kow":
#         a = 2
#     else:
#         a = 0
#     if leave == 'Somewhat easy':
#         l = 1
#     elif leave == 'Very easy':
#         l = 2
#     elif leave == 'Somewhat difficult':
#         l = 3
#     elif leave == 'Very difficult':
#         l = 4
#     else:
#         l = 0
#     if mental_health_consequence == 'Yes':
#         mhc = 1
#     elif mental_health_consequence == 'May be':
#         mhc = 2
#     else:
#         mhc = 0
#     if phys_health_consequence == 'Yes':
#         phc = 1
#     elif phys_health_consequence == 'May be':
#         phc = 2
#     else:
#         phc = 0
#     if coworkers == 'Yes':
#         c = 1
#     elif coworkers == 'Some of them':
#         c = 2
#     else:
#         c = 0
#     if supervisor == 'Yes':
#         s = 1
#     elif supervisor == 'Some of them':
#         s = 2
#     else:
#         s = 0
#     if mental_health_interview == 'Yes':
#         mhi = 1
#     elif mental_health_interview == 'May be':
#         mhi = 2
#     else:
#         mhi = 0
#     if phys_health_interview == 'Yes':
#         phi = 1
#     elif phys_health_interview == 'May be':
#         phi = 2
#     else:
#         phi = 0
#     if mental_vs_physical == 'Yes':
#         mvp = 1
#     elif mental_vs_physical == "Don't know":
#         mvp = 2
#     else:
#         mvp = 0
#     if obs_consequence == 'Yes':
#         oc = 1
#     else:
#         oc = 0
#
#     xx = [['age', ' gender', 'self_employed', 'family_history', 'work_interfere', 'no_employees',
#            'remote_work ', 'tech_company', 'benefits', 'care_options', 'wellness_program',
#            'seek_help', 'anonymity', 'leave', 'mental_health_consequence', 'phys_health_consequence',
#            'coworkers', 'supervisor', 'mental_health_interview', 'phys_health_interview', 'mental_vs_physical',
#            'obs_consequence']]
#
#     xx[0] = xx.append(age)
#     xx[1] = xx.append(g)
#     xx[2] = xx.append(se)
#     xx[3] = xx.append(fh)
#     xx[4] = xx.append(wi)
#     xx[5] = xx.append(ne)
#     xx[6] = xx.append(rw)
#     xx[7] = xx.append(tc)
#     xx[8] = xx.append(b)
#     xx[9] = xx.append(co)
#     xx[10] = xx.append(wp)
#     xx[11] = xx.append(sh)
#     xx[12] = xx.append(a)
#     xx[13] = xx.append(l)
#     xx[14] = xx.append(mhc)
#     xx[15] = xx.append(phc)
#     xx[16] = xx.append(c)
#     xx[17] = xx.append(s)
#     xx[18] = xx.append(mhi)
#     xx[19] = xx.append(phi)
#     xx[20] = xx.append(mvp)
#     xx[21] = xx.append(oc)
#
#     result = model.predict([xx])[0]
#
#     if result[0] == 0:
#         output = 'NO NEED ANY TREATMENT'
#     else:
#         output = 'YOU NEED TREATMENT'
#     return render_template('home.html', result=output)
#
#     #return render_template('home.html', **locals())
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
import pickle
import pandas as pd

app = Flask(__name__, template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))

data = pd.read_csv("filtered.csv")

X = data[['age', 'gender', 'self_employed', 'family_history', 'work_interfere', 'no_employees',
        'remote_work', 'tech_company', 'benefits', 'care_options', 'wellness_program',
        'seek_help', 'anonymity', 'leave', 'mental_health_consequence', 'phys_health_consequence',
        'coworkers', 'supervisor', 'mental_health_interview', 'phys_health_interview', 'mental_vs_physical',
        'obs_consequence']]

ord_encoder = OrdinalEncoder()
X = ord_encoder.fit_transform(X)

le = LabelEncoder()
y = data["treatment"]

y = le.fit_transform(y)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/home', methods=['POST'])
def predict():
    features = [x for x in request.form.values()]
    ready = ord_encoder.fit_transform([features])
    prediction = model.predict(ready)
    if prediction[0] == 0:
        output = 'NO NEED ANY TREATMENT'
    else:
        output = 'YOU NEED TREATMENT'
    return render_template('home.html', prediction=output)


if __name__ == '__main__':
    app.run(debug=True)
