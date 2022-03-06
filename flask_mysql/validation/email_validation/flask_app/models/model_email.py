from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_email(email):
        is_vaild = True
        if not EMAIL_REGEX.match(email['email']):
            flash("Email is not valid!")
            is_vaild = False
        return is_vaild

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Emails;"
        results = connectToMySQL('emails_db').query_db(query)
        emails = []
        if results:
            for email in results:
                emails.append( cls(email) )
        return emails
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM Emails WHERE id = %(id)s;"
        result = connectToMySQL("emails_db").query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_one(cls, data):
        pass

    @classmethod
    def update(cls, data):
        query = "UPDATE Emails SET email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL("emails_db").query_db(query, data)


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO Emails (email , created_at, updated_at ) VALUES ( %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('emails_db').query_db( query, data )

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM Emails WHERE id = %(id)s;"
        return connectToMySQL("emails_db").query_db(query, data)