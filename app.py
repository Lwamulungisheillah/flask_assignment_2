from flask import Flask, render_template, request

app=Flask(__name__)


@app.route('/')
def home ():
   return render_template('home.html')

    
@app.route('/about')
def about ():
    return render_template('about.html')

    
@app.route('/contact')
def contact ():
   return render_template('contact.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # user's name and email 
        name = request.user['name']
        email = request.user['email']

        # Displaying a thank you message
        return render_template('thankyou.html', name=name, email=email)

     # If it's a GET request, render the form
    return render_template('user.html')

 
 
