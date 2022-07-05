'''
CREATE TABLE Ages ( 
    name VARCHAR(128), 
    age INTEGER
);

INSERT INTO Ages (name, age) VALUES ('Kimberleigh', 31);
INSERT INTO Ages (name, age) VALUES ('Marnie', 19);
INSERT INTO Ages (name, age) VALUES ('Malak', 21);
INSERT INTO Ages (name, age) VALUES ('Maximus', 31);
INSERT INTO Ages (name, age) VALUES ('Makenzie', 32);

SELECT hex(name || age) AS X FROM Ages ORDER BY X
'''
