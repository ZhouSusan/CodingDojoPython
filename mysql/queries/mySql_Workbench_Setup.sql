-- Create 3 new users
INSERT INTO Users (first_name, last_name, email) VALUES ("Andrew", "Lee", "andrewlee@gmail.com");
INSERT INTO Users (first_name, last_name, email) VALUES ("Jay", "Patel", "jaypatel@outlook.com");
INSERT INTO USERS (first_name, last_name, email) VALUES ("Kobe", "Bryant", "kb@aol.com");

-- Show all users by their last name
SELECT * FROM Users ORDER BY first_name;  
SELECT * FROM Users ORDER BY last_name;

-- Delete user with id of 1
DELETE FROM Users WHERE id=1;

-- Update kb@aol.come email address to kobewbryant@hotmail.com
UPDATE Users SET email = "kobewbryant@hotmail.com" WHERE id=3;
UPDATE Users SET email = "jpatel@outlook.com" WHERE id =2;

-- --show all users
SELECT * FROM Users;
