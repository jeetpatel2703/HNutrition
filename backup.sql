-- Step 1: Create the database for food nutrition
create database food_nutrition;

-- Step 2: Use the created database
use food_nutrition;

-- Step 3: Create table to store food categories
create table food_categories (
    id int auto_increment primary key,
    name varchar(255) not null
);

-- Step 4: Create table to store food items
create table food_items (
    id int auto_increment primary key,
    name varchar(255) not null,
    category_id int,
    foreign key (category_id) references food_categories(id)
);

-- Step 5: Create table to store nutritional information
create table nutritional_info (
    id int auto_increment primary key,
    item_id int,
    calories float,
    protein float,
    fat float,
    carbohydrates float,
    foreign key (item_id) references food_items(id)
);

-- Step 6: Insert food categories
insert into food_categories (name) values ('fruits'),('vegetables'),('dairy'),('grains');

-- Step 7: Insert food items for fruits
insert into food_items (name, category_id) values
    ('apple', 1),
    ('banana', 1),
    ('orange', 1),
    ('strawberry', 1),
    ('grapes', 1),
    ('watermelon', 1),
    ('kiwi', 1),
    ('peach', 1),
    ('pear', 1),
    ('plum', 1);

-- Step 8: Insert food items for vegetables
insert into food_items (name, category_id) values
    ('spinach', 2),
    ('carrot', 2),
    ('broccoli', 2),
    ('cucumber', 2),
    ('tomato', 2),
    ('bell pepper', 2),
    ('zucchini', 2),
    ('aubergine', 2),
    ('lettuce', 2),
    ('cabbage', 2);

-- Step 9: Insert food items for dairy
insert into food_items (name, category_id) values
    ('milk', 3),
    ('cheese', 3),
    ('yogurt', 3),
    ('cottage cheese', 3),
    ('soy milk', 3),
    ('almond milk', 3),
    ('coconut milk', 3),
    ('oat milk', 3),
    ('cashew milk', 3),
    ('rice milk', 3);

-- Step 10: Insert food items for grains
insert into food_items (name, category_id) values
    ('bread', 4),
    ('rice', 4),
    ('pasta', 4),
    ('quinoa', 4),
    ('oats', 4),
    ('barley', 4),
    ('couscous', 4),
    ('bulgur', 4),
    ('farro', 4),
    ('millet', 4);
