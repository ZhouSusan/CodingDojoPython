from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    class User:
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("mydb").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_flask').query_db(query)
        users = []
        if results:
            for user in results:
                users.append( cls(user) )
            return users
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM Users WHERE id = %(id)s;"
        result = connectToMySQL("users_flask").query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_one(cls, data):
        pass

    @classmethod
    def update(cls, data):
        query = "UPDATE Users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL("users_flask").query_db(query, data)


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_flask').query_db( query, data )

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM Users WHERE id = %(id)s;"
        return connectToMySQL("users_flask").query_db(query, data)

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s);"
        return connectToMySQL("mydb").mysql.query_db(query, data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("mydb").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s);"
        return connectToMySQL("mydb").mysql.query_db(query, data)

