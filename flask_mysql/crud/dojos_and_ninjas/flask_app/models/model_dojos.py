from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_ninjas

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        if results:
            for dojo in results:
                dojos.append( cls(dojo) )
            return dojos
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM Dojos WHERE id = %(id)s;"
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return cls(result[0])

    @classmethod
    def update_one(cls, data):
        pass

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO Dojos ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    @classmethod
    def destroy(cls, data):
        pass

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM Dojos LEFT JOIN Ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                'id' : row_from_db['Ninjas.id'],
                'first_name': row_from_db['first_name'],
                'last_name': row_from_db['last_name'],
                'age': row_from_db['age'],
                'created_at': row_from_db['Ninjas.created_at'],
                'updated_at': row_from_db['Ninjas.updated_at'],
                'dojo_id' : row_from_db['dojo_id']
            }
            dojo.ninjas.append( model_ninjas.Ninja(ninja_data))
        return dojo
