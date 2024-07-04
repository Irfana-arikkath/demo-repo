from flask import current_app as app, render_template,request,redirect,url_for

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit',methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    gender=request.form['gender']
    contact_method=request.form['contact_method']
    interests=request.form['interests']
    file = request.files['photo']
    
    
    
    # Process the data (e.g., save it to a database, send an email, etc.)
    # For this example, we'll just print it to the console
    print(f"Name: {name}, age: {age},gender: {gender},contact_method: {contact_method},interests: {interests},")
    
    # Redirect to a thank you page or back to the form
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return "Thank you for submitting the form!"

if __name__ == '__main__':
    app.run(debug=True)
    render_template("index.html")