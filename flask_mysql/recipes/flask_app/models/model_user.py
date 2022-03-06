from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import bcrypt, DATABASE
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM Users WHERE email = %(email)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM Users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO Users ( first_name, last_name, email, password) VALUES ( %(first_name)s , %(last_name)s, %(email)s, %(password)s );"
        return connectToMySQL(DATABASE).query_db( query, data )

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters")
            is_valid = False
        if len(user['password']) < 8:
            flash("Passwords must be 8 characters long")
            is_valid = False
        if user['password'] != user['cpassword']:
            flash("Passwords does not match")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email!") 
            return False      
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,email)
        if results != False and len(results) != 0:
            flash("Emails already taken.")
            is_valid = False
        return is_valid
