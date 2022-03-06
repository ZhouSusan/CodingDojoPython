from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        users = []
        if results:
            for user in results:
                users.append( cls(user) )
            return users
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM Dojos WHERE id = %(id)s;"
        result = connectToMySQL("dojo_survey_schema").query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_one(cls, data):
        pass

    @classmethod
    def update(cls, data):
        query = "UPDATE Dojos SET name=%(name)s,location=%(location)s, language=%(language)s,comment=%(comment)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL("dojo_survey_schema").query_db(query, data)


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO Dojoss ( name , location , language , comment, created_at, updated_at ) VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_survey_schema').query_db( query, data )

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM Dojos WHERE id = %(id)s;"
        return connectToMySQL("dojo_survey_schema").query_db(query, data)    