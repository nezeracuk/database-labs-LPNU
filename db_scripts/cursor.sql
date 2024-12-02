DELIMITER //

CREATE PROCEDURE create_dynamic_tables()
BEGIN
    DECLARE finished INT DEFAULT 0;
    DECLARE athlete_id INT;
    DECLARE best_score DECIMAL(5,2);
    DECLARE cur CURSOR FOR SELECT athlete_id, best_score FROM athlete_statistics;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;

    SET @table1 = CONCAT('athlete_stats_', UNIX_TIMESTAMP(), '_1');
    SET @table2 = CONCAT('athlete_stats_', UNIX_TIMESTAMP(), '_2');

    -- Динамічно створюємо таблиці
    SET @create_table_sql = CONCAT(
        'CREATE TABLE ', @table1, ' LIKE athlete_statistics;'
    );
    PREPARE stmt FROM @create_table_sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    SET @create_table_sql = CONCAT(
        'CREATE TABLE ', @table2, ' LIKE athlete_statistics;'
    );
    PREPARE stmt FROM @create_table_sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    -- Відкриваємо курсор
    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO athlete_id, best_score;
        IF finished THEN
            LEAVE read_loop;
        END IF;

        -- Випадковий розподіл даних між таблицями
        IF RAND() < 0.5 THEN
            SET @insert_sql = CONCAT(
                'INSERT INTO ', @table1, ' (athlete_id, total_competitions, best_score, average_score) ',
                'SELECT athlete_id, total_competitions, best_score, average_score FROM athlete_statistics WHERE athlete_id = ', athlete_id, ';'
            );
        ELSE
            SET @insert_sql = CONCAT(
                'INSERT INTO ', @table2, ' (athlete_id, total_competitions, best_score, average_score) ',
                'SELECT athlete_id, total_competitions, best_score, average_score FROM athlete_statistics WHERE athlete_id = ', athlete_id, ';'
            );
        END IF;

        PREPARE stmt FROM @insert_sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;

    -- Закриваємо курсор
    CLOSE cur;
END //

DELIMITER ;
