import pandas as pd
from sklearn.preprocessing import OrdinalEncoder,LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import pickle

data = pd.read_csv("filtered.csv")

X = data[['age', 'gender', 'self_employed', 'family_history', 'work_interfere', 'no_employees',
           'remote_work', 'tech_company', 'benefits', 'care_options', 'wellness_program',
           'seek_help', 'anonymity', 'leave', 'mental_health_consequence', 'phys_health_consequence',
           'coworkers', 'supervisor', 'mental_health_interview', 'phys_health_interview', 'mental_vs_physical',
           'obs_consequence']]

ord_encoder = OrdinalEncoder()
X = ord_encoder.fit_transform(X)

y = data['treatment']
le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

classifier = XGBClassifier()

classifier.fit(X_train, y_train)

pickle.dump(classifier, open("model.pkl", "wb"))
