```markdown
#Program Algorithm & Pseudo code

## Main Workflow
1.START program.
2.LOAD raw weather dataset.
3.CALL `process_dataset()` to separate raw data into `valid_records` and `invalid_records`
4.ENTER continuous `while True` loop:
  -Display menu choices(1 to 7).
  -Get user selection.
  -Execute corresponding function (Option 1-6).
  -If choice is 7,exit loop and end program.
  -If choice is invalid,display error and repeat menu.
5.END program.

#Pseudo code
START
    Define sample dataset containing weather records (Station, Temp, Rainfall, Humidity, WindSpeed)
    
    FUNCTION validate_record(record):
        Initialize empty list 'reasons'
        
        IF Temp < -10 OR Temp > 50 THEN
            Append "Temperature must be between -10°C and 50°C" to reasons
        END IF
        
        IF Rainfall < 0 THEN
            Append "Rainfall must be 0 or greater" to reasons
        END IF
        
        IF Humidity < 0 OR Humidity > 100 THEN
            Append "Humidity must be between 0% and 100%" to reasons
        END IF
        
        IF WindSpeed < 0 THEN
            Append "Wind speed must be 0 or greater" to reasons
        END IF
        
        IF length of reasons is 0 THEN
            RETURN (True, [])
        ELSE
            RETURN (False, reasons)
        END IF
    END FUNCTION

    FUNCTION process_dataset(data):
        Initialize valid_records list and invalid_records list
        FOR each record in data DO
            is_valid, reasons = validate_record(record)
            IF is_valid THEN
                Add record to valid_records
            ELSE
                Add (record, reasons) to invalid_records
            END IF
        END FOR
        RETURN valid_records, invalid_records
    END FUNCTION

    FUNCTION classify_temperature(temp):
        IF temp < 20 THEN
            RETURN "Cold"
        ELSE IF 20 <= temp <= 30 THEN
            RETURN "Moderate"
        ELSE
            RETURN "Hot"
        END IF
    END FUNCTION

    MAIN LOOP:
        DISPLAY Menu:
            1. View valid readings
            2. Analyse weather
            3. Search by station
            4. View temperature classifications
            5. View invalid records
            6. View summary
            7. Exit
            
        GET choice from user
        
        SWITCH choice:
            CASE 1: Call function to display valid records
            CASE 2: Call function to calculate averages, min/max temps, max rainfall station, count > 30°C
            CASE 3: Prompt station name -> Call function to search and display matching records
            CASE 4: Call function to classify temperatures and display classification counts
            CASE 5: Call function to display invalid records with rejection reasons
            CASE 6: Call function to display overall dataset summary
            CASE 7: PRINT "Exiting program." -> STOP
            DEFAULT: PRINT "Invalid selection, please try again."
        END SWITCH
    END LOOP
END


