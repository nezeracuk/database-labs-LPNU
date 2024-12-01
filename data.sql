-- Insert data into athlete table
INSERT INTO `athlete` (`firstname`, `lastname`, `height`, `weight`) VALUES
('Ivan', 'Petrenko', 180.5, 75.0),
('Oleksandr', 'Ivanov', 175.0, 68.2),
('Olga', 'Kovalchuk', 165.0, 55.0),
('Dmytro', 'Sydorenko', 182.0, 80.0),
('Natalia', 'Melnyk', 168.0, 60.0),
('Serhiy', 'Lysenko', 185.0, 90.0),
('Iryna', 'Shevchenko', 170.0, 58.0),
('Viktor', 'Kravchenko', 178.0, 72.0),
('Maria', 'Bondarenko', 160.0, 50.0),
('Oleg', 'Tkachenko', 190.0, 85.0);

-- Insert data into schedule_meal table
INSERT INTO `schedule_meal` (`meal_name`, `day_of_week`, `meal_time`, `ServingSize`) VALUES
('Oatmeal', 'Monday', 'Breakfast', '200g'),
('Chicken Breast', 'Monday', 'Lunch', '250g'),
('Rice with Vegetables', 'Monday', 'Dinner', '300g'),
('Tuna Salad', 'Tuesday', 'Lunch', '200g'),
('Eggs with Tomatoes', 'Tuesday', 'Breakfast', '150g'),
('Vegetable Soup', 'Wednesday', 'Lunch', '300g'),
('Turkey Patty', 'Wednesday', 'Dinner', '200g'),
('Baked Salmon', 'Thursday', 'Dinner', '250g'),
('Seafood', 'Friday', 'Lunch', '200g'),
('Vegetable Stew', 'Saturday', 'Dinner', '300g');

-- Insert data into ingredient table
INSERT INTO `ingredient` (`name`, `description`, `quantity`, `unit`) VALUES
('Oats', 'Whole grain oats', '500', 'grams'),
('Chicken Fillet', 'Chicken breast', '1', 'kilogram'),
('Rice', 'White long-grain rice', '1', 'kilogram'),
('Tuna', 'Canned tuna', '200', 'grams'),
('Eggs', 'Chicken eggs', '6', 'pieces'),
('Tomatoes', 'Fresh tomatoes', '500', 'grams'),
('Turkey', 'Turkey fillet', '1', 'kilogram'),
('Salmon', 'Baked salmon', '300', 'grams'),
('Seafood', 'Shrimps, squids', '500', 'grams'),
('Vegetables', 'Vegetable mix', '1', 'kilogram');

-- Insert data into trainer_doctor table
INSERT INTO `trainer_doctor` (`firstname`, `lastname`, `contact_info`) VALUES
('Oleksandr', 'Melnyk', '+380633581135'),
('Anna', 'Honchar', '+380674234567'),
('Serhiy', 'Pavlenko', '+380937234567'),
('Iryna', 'Tkachuk', '+380631254567'),
('Dmytro', 'Shevchenko', '+380671112233'),
('Maria', 'Koval', '+380661114233'),
('Oleg', 'Bondar', '+380931115222'),
('Natalia', 'Herasymenko', '+380671834888'),
('Yuriy', 'Vasylenko', '+380731244567'),
('Ivan', 'Sydorenko', '+380931237999');

-- Insert data into competition table
INSERT INTO `competition` (`name`, `date`, `Location`, `athlete_id`) VALUES
('Kyiv Championship', '2023-09-25', 'Kyiv', 1),
('City Competition', '2023-10-05', 'Lviv', 2),
('Regional Tournament', '2023-11-12', 'Odesa', 3),
('Ukrainian Cup', '2023-12-20', 'Dnipro', 4),
('Kharkiv Championship', '2023-09-15', 'Kharkiv', 5),
('International Tournament', '2023-10-15', 'Cherkasy', 6),
('Winter Cup', '2023-12-01', 'Chernivtsi', 7),
('Kyiv Region Cup', '2023-11-25', 'Bucha', 8),
('Lviv Region Cup', '2023-12-10', 'Lviv', 9),
('Strongman Competition', '2023-12-15', 'Kyiv', 10);

-- Insert data into schedule_supplements table
INSERT INTO `schedule_supplements` (`supplement_name`, `dosage`, `time_of_day`, `duration`) VALUES
('Creatine', '5g', 'Morning', '30 days'),
('Protein', '30g', 'Morning', '60 days'),
('Vitamin D', '2000 IU', 'Afternoon', '90 days'),
('Omega-3', '2 capsules', 'Evening', '60 days'),
('Magnesium', '400mg', 'Morning', '30 days'),
('BCAA', '10g', 'Morning', '30 days'),
('Glutamine', '5g', 'Evening', '30 days'),
('Zinc', '50mg', 'Evening', '90 days'),
('Vitamin C', '1000mg', 'Morning', '30 days'),
('Arginine', '5g', 'Morning', '30 days');

-- Insert data into schedule table
INSERT INTO `schedule` (`id`, `schedule_meal_id`, `schedule_supplements_id`, `start_date`, `end_date`, `frequency`, `athlete_id`, `trainer_doctor_id`) VALUES
(1, 1, 1, '2023-10-01', '2023-10-31', 'Daily', 1, 1),
(2, 2, 2, '2023-11-01', '2023-11-30', 'Daily', 2, 2),
(3, 3, 3, '2023-12-01', '2023-12-31', 'Daily', 3, 3),
(4, 4, 4, '2023-10-01', '2023-10-31', 'Daily', 4, 4),
(5, 5, 5, '2023-11-01', '2023-11-30', 'Daily', 5, 5),
(6, 6, 6, '2023-12-01', '2023-12-31', 'Daily', 6, 6),
(7, 7, 7, '2023-10-01', '2023-10-31', 'Daily', 7, 7),
(8, 8, 8, '2023-11-01', '2023-11-30', 'Daily', 8, 8),
(9, 9, 9, '2023-12-01', '2023-12-31', 'Daily', 9, 9),
(10, 10, 10, '2023-12-01', '2023-12-31', 'Daily', 10, 10);

-- Insert data into supplement table
INSERT INTO `supplement` (`name`, `description`, `dosage`, `Frequency`, `schedule_supplements_id`) VALUES
('Creatine', 'Increases muscle mass', '5g', 'Daily', 1),
('Protein', 'Source of protein for muscles', '30g', 'Daily', 2),
('Vitamin D', 'Supports immunity', '2000 IU', 'Daily', 3),
('Omega-3', 'Improves heart health', '2 capsules', 'Daily', 4),
('Magnesium', 'Reduces stress levels', '400mg', 'Daily', 5),
('BCAA', 'Aids in recovery', '10g', 'Daily', 6),
('Glutamine', 'Speeds up recovery', '5g', 'Daily', 7),
('Zinc', 'Supports immune system', '50mg', 'Daily', 8),
('Vitamin C', 'Antioxidant', '1000mg', 'Daily', 9),
('Arginine', 'Improves circulation', '5g', 'Daily', 10);

-- Insert data into meal_ingredients table
INSERT INTO `meal_ingredients` (`id`, `ingredient_id`, `meal_id`, `meal_schedule_meal_id`, `quantity`, `unit`) VALUES
(1, 1, 1, 1, 100, 'grams'),
(2, 2, 2, 2, 200, 'grams'),
(3, 3, 3, 3, 150, 'grams'),
(4, 4, 4, 4, 100, 'grams'),
(5, 5, 5, 5, 150, 'grams'),
(6, 6, 6, 6, 200, 'grams'),
(7, 7, 7, 7, 250, 'grams'),
(8, 8, 8, 8, 300, 'grams'),
(9, 9, 9, 9, 350, 'grams'),
(10, 10, 10, 10, 400, 'grams');

-- Insert data into meal table
INSERT INTO `meal` (`name`, `description`, `energy_value`, `meal_type`, `schedule_meal_id`) VALUES
('Oatmeal', 'Oatmeal with fruits', 350.5, 'Breakfast', 1),
('Chicken Breast', 'Chicken breast with vegetables', 450.0, 'Lunch', 2),
('Rice with Vegetables', 'Rice with vegetables and spices', 300.0, 'Dinner', 3),
('Tuna Salad', 'Light salad with tuna and vegetables', 200.0, 'Lunch', 4),
('Eggs with Tomatoes', 'Fried eggs with tomatoes', 180.0, 'Breakfast', 5),
('Vegetable Soup', 'Low-calorie vegetable soup', 150.0, 'Lunch', 6),
('Turkey Patty', 'Baked turkey with garnish', 250.0, 'Dinner', 7),
('Baked Salmon', 'Baked salmon with lemon', 350.0, 'Dinner', 8),
('Seafood', 'Seafood assortment with vegetables', 400.0, 'Lunch', 9),
('Vegetable Stew', 'Stewed vegetables with potatoes', 300.0, 'Dinner', 10);

INSERT INTO `athlete_trainer` (`athlete_id`, `trainer_doctor_id`) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(3, 1),
(4, 2),
(4, 3),
(5, 4),
(5, 5);