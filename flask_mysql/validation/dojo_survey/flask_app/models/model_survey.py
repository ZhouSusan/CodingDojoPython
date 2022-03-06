from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.language = data['language']
        self.location = data['location']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Surveys;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        dojos = []
        if results:
            for dojo in results:
                dojos.append( cls(user) )
        return dojos
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM Surveys WHERE id = %(id)s;"
        result = connectToMySQL("dojo_survey_schema").query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_one(cls, data):
        pass

    @classmethod
    def update(cls, data):
        query = "UPDATE Surveys SET name=%(name)s, location=%(location)s, language=%(language)s, comment=%(comment)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL("dojo_survey_schema").query_db(query, data)


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO Surveys ( name , location , language , comment, created_at, updated_at ) VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_survey_schema').query_db( query, data )

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM Surveys WHERE id = %(id)s;"
        return connectToMySQL("dojo_survey_schema").query_db(query, data)

    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM Surveys ORDER BY id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey_schema').query_db( query )
        return cls(results[0])

    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters long.")
            is_valid = False
        if len(survey['location']) < 1:
            flash("Must select one location")
            is_valid = False
        if len(survey["language"]) < 1:
            flash("Must select one language")
            is_valid = False
        if len(survey['comment']) < 5:
            flash("Comments must be at least 5 characters long.")
            is_valid = False
        return is_valid