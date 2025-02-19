USE lab4;

DROP TRIGGER IF EXISTS prevent_deletion;
DROP TRIGGER IF EXISTS validate_average_score;
DROP TRIGGER IF EXISTS prevent_meal_update;
DROP TRIGGER IF EXISTS prevent_meal_delete;

DELIMITER //

CREATE TRIGGER prevent_meal_update
BEFORE UPDATE ON meal
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Updates are not allowed on the meal table';
END //

CREATE TRIGGER prevent_meal_delete
BEFORE DELETE ON meal
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deletions are not allowed on the meal table';
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER validate_average_score
BEFORE INSERT ON athlete_statistics
FOR EACH ROW
BEGIN
    IF NEW.average_score LIKE '%.00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Average score cannot end with .00';
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER prevent_deletion
BEFORE DELETE ON athlete_statistics
FOR EACH ROW
BEGIN
    IF OLD.total_competitions > 5 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot delete athlete_statistics where total_competitions > 5';
    END IF;
END //

DELIMITER ;
