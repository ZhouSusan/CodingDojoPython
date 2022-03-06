SET SQL_SAFE_UPDATES = 0;

-- Create 3 new dojos
INSERT INTO Dojos(name) VALUES ("Selena Gomez");
INSERT INTO Dojos(name) VALUES ("Cooke Monster");
INSERT INTO DOjos(name) VALUES ("Mr. Rogers");

-- Delete the 3 dojos that was created above 
DELETE FROM Dojos;

-- create 3 new Dojos
INSERT INTO Dojos (name) VALUES ("Andrew LEE");
INSERT INTO Dojos (name) VALUES ("Marsia Guavana");
INSERT INTO Dojos (name) VALUES ("Edward Inn");

-- Create 3 ninjas that belong to the first dojo
INSERT INTO Ninjas(first_name, last_name, age, dojo_id) VALUES ("Jessie", "McHill", 27, 4);
INSERT INTO Ninjas(first_name, last_name, age, dojo_id) VALUES ("Fred", "Mcdonalds", 20, 4);
INSERT INTO Ninjas(first_name, last_name, age, dojo_id) VALUES ("Kyle", "Butterfly", 32, 4);

-- create 3 ninjas that belong to the second dojo
INSERT INTO Ninjas(first_name, last_name, age, dojo_id) VALUES ("Steve", "Urkel", 19, 5);
INSERT INTO Ninjas(first_name, last_name, age, dojo_id) VALUES ("Julie", "Wilson", 41, 5);
INSERT INTO Ninjas(first_name, last_name, age, dojo_id) VALUES ("Cheese", "Smith", 38, 5);

-- create 3 ninjas from the last dojo 
INSERT INTO Ninjas(first_name, last_name, age, dojo_id) VALUES ("Cony", "Ta", 51, 6);
INSERT INTO Ninjas(first_name, last_name, age, dojo_id) VALUES ("Brown", "Bearster", 29, 6);
INSERT INTO Ninjas(first_name, last_name, age, dojo_id) VALUES ("Krispy", "Jones", 18, 6);

-- retireve all the ninjas from the first dojo
SELECT * FROM Ninjas WHERE dojo_id=4;

-- retrieve all the ninjas from the second dojo
SELECT * FROM Ninjas WHERE dojo_id=5;

-- retrieve all the ninjas from the third dojo
SELECT * FROM Ninjas WHERE dojo_id=6;