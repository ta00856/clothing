import mysql.connector
from flask import Flask

app = Flask(__name__)

def check_database_connection():
    try:
        # Replace 'your_host', 'your_user', 'your_password', and 'clothing' with your actual database credentials
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Kzzs@022704',
            database='clothing'
        )
        connection.close()
        return True
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return False

@app.route('/')
def check_connection():
    if check_database_connection():
        return "Connection to the database successful!"
    else:
        return "Failed to connect to the database."

if __name__ == "__main__":
    app.run(debug=True)
    
#tkdmsn d
    
