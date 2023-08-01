import mysql.connector
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)




# Define the route for the home page (root URL)
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the form data from the request
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Establish a connection to the database
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Kzzs@022704',
            database='clothing'
        )

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Insert the user's data into the 'users' table
        insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        data = (name, email, password)
        cursor.execute(insert_query, data)

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and the database connection
        cursor.close()
        connection.close()

        # Redirect to the login page after successful registration
        return redirect('/login')

    # If the request method is GET, render the register page template
    return render_template('register.html')

# ... (previous code)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the form data from the request
        email = request.form['email']
        password = request.form['password']

        # Establish a connection to the database
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Kzzs@022704',
            database='clothing'
        )

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Check if the user's credentials exist in the 'users' table
        select_query = "SELECT * FROM users WHERE email = %s AND password = %s"
        data = (email, password)
        cursor.execute(select_query, data)

        # Fetch the user's data from the database
        user_data = cursor.fetchone()

        # Close the cursor and the database connection
        cursor.close()
        connection.close()

        # If user_data is not None, the user exists, and we can proceed to the dashboard
        if user_data is not None:
            return redirect('/dashboard')
        else:
            return "Invalid email or password. Please try again."

    # If the request method is GET, render the login page template
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



if __name__ == "__main__":
    app.run(debug=True)
    