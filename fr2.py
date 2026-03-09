import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
 
df=pd.read_csv("fraud_500.csv")

encoder = LabelEncoder()
df["transaction_type"] = encoder.fit_transform(df["transaction_type"])
df["city"] = encoder.fit_transform(df["city"])

X=df.drop(["is_fraud","transaction_id","customer_id","transaction_date"],axis=1)
y=df["is_fraud"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = RandomForestClassifier(n_estimators=100, class_weight="balanced", random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
print("accuracy=",accuracy)

new_transaction=pd.DataFrame([{
    "transaction_amount":55000,
    "transaction_type":encoder.fit_transform(["ATM"])[0],
    "city":encoder.fit_transform(["Houston"])[0],
    "is_foreign_transaction":0,
    "account_age_days":300,
}])


prediction = model.predict(new_transaction)
print("prediction:",prediction)

if prediction[0] == 1:
    print("Fraud")
else:
    print("Not Fraud")
