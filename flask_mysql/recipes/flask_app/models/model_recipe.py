from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.user_id = data['user_id']
        self.description = data['description']
        self.instructions = data['instructions']
        self.less_than_thirty = data['less_than_thirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM Recipes WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipe_list = []
        for result in results:
            recipe_list.append(cls(result))
        return recipe_list    

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO Recipes ( name, description, instructions, less_than_thirty, user_id, created_at) VALUES ( %(name)s , %(description)s, %(instructions)s, %(less_than_thirty)s, %(user_id)s, %(created_at)s );"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def update(cls, data ):
        query = "UPDATE Recipes SET name = %(name)s , description=  %(description)s, instructions = %(instructions)s, less_than_thirty = %(less_than_thirty)s , created_at = %(created_at)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod 
    def delete(cls, data): 
        query = "DELETE FROM Recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description must be at least 3 characters")
            is_valid = False
        if len(recipe['instructions']) < 8:
            flash("Instructions must be 8 characters long")
            is_valid = False
        return is_valid

