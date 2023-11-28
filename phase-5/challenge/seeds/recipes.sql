DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    recipe_name text,
    cook_time int,
    rating int
);

INSERT INTO recipes (recipe_name, cook_time, rating) VALUES ('tikka masala', 60, 5);
INSERT INTO recipes (recipe_name, cook_time, rating) VALUES ('shepherds pie', 70, 3);
INSERT INTO recipes (recipe_name, cook_time, rating) VALUES ('lasagna', 50, 4);


