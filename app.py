from flask import Flask, render_template, request
import joblib 

app = Flask(__name__)

# business logic

@app.route('/')
def base():
    return render_template('home.html')


@app.route('/predict', methods =['post'])
def predict():

    #Load the model
    model = joblib.load('diabetic_80.pkl')

    Pregnancy = int(request.form.get('Pregnancy'))
    Plasma = int(request.form.get('Plasma'))
    Bp = int(request.form.get('Bp'))
    skin = int(request.form.get('skin'))
    Test = int(request.form.get('Test'))
    mass = int(request.form.get('Mass'))
    pedi = int(request.form.get('pedi'))
    age = int(request.form.get('age'))

    print(Pregnancy,Plasma,Bp,skin,Test,mass,pedi,age)
    output = model.predict([[Pregnancy,Plasma,Bp,skin,Test,mass,pedi,age]])

    if output[0] == 0:
        data = "Person is not diabetic"
    else:
        data = "Person is diabetic"
        
    return render_template('predict.html', data = data)

if __name__ == "__main__":
    app.run(debug=True)

