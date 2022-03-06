from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.age = data['age']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        if results:
            for ninja in results:
                ninjas.append( cls(ninja) )
            return ninjas
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM Ninjas WHERE id = %(id)s;"
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
        query = "INSERT INTO Ninjas (first_name , last_name , age, created_at, updated_at, dojo_id ) VALUES ( %(first_name)s , %(last_name)s , %(age)s , NOW() , NOW(), %(dojo_id)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    @classmethod
    def destroy(cls, data):
        pass