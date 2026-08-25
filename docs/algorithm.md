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


    FUNCTION view_invalid_readings(invalid_records):
        PRINT "INVALID RECORDS WITH REJECTION EXPLANATIONS"

        IF invalid_records is EMPTY THEN
            PRINT "No invalid record found in the dataset."
            RETURN
        END IF
        SET idx = 1
        FOR EACH (rec,reasons) IN invalid_record DO 
            PRINT blank line
            PRINT idx, "Station:",rec.station

            PRINT "DATA: Temp=",rec.temp,"°C,Rain=",rec.rainfall,"mm,Humidity=",rec.humidity,"%,Wind=",rec.wind_speed,"km/h"
            PRINT "Rejection Reason(s):"
            FOR EACH reason IN reasons DO 
                PRINT"  -",reason
            END FOR

            idx = idx + 1
        END FOR
    END FUNCTION


    FUNCTION view_valid_readings(valid_records):
        PRINT "VALID WEATHER READINGS" header

        IF valid_records is EMPTY THEN
            PRINT "No valid records found."
            RETURN
        END IF
        // Build and print table header
        SET header = "Station | Temp (°C) | Rain (mm) | Humidity (%) | Wind (km/h)"
        PRINT header
        PRINT a line of dashes as long as header

        // Loop through each record and print as a formatted row
        FOR EACH record r IN valid_records DO
            PRINT r.station (left-aligned, 18 chars),
                  r.temp (left-aligned, 10 chars, 1 decimal),
                  r.rainfall (left-aligned, 10 chars, 1 decimal),
                  r.humidity (left-aligned, 12 chars),
                  r.wind_speed (left-aligned, 10 chars, 1 decimal)
                  separated by " | "
        END FOR
    END FUNCTION


    FUNCTION analyse_weather(valid_records):
        PRINT "WEATHER ANALYSIS"
        IF valid_records is EMPTY THEN
            PRINT "Cannot perform analysis: No valid records available."
            RETURN
        SET n = count of valid_records
        //---Calculate averages ---
        SET total_temp = 0
        FOR EACH r IN valid_records DO
            total_temp = total_temp + r.temp
        END FOR
        SET avg_temp= total_temp / n

        SET total_rain = 0
        FOR EACH r IN valid_records
            total_rain = total_rain + r.rainfall
        END FOR
        SET avg_rain = total_rain / n

        SET total_hum = 0
        FOR EACH r IN valid_records DO
            total_hum = total_hum + r.humidity
        END FOR 
        SET avg_hum = total_hum / n

        SET total_wind = 0
        FOR EACH r IN valid_records DO
            total_wind = total_wind + r.wind_speed
        END FOR
        SET avg_wind = total_wind/n

        //---Find highest/lowest temperature records ---
        SET highest_temp_rec = valid_records[0]
        SET lowest_temp_rec = valid_record[0]
        FOR EACH r IN valid_records DO
            IF r.temp > highest_temp_rec.temp THEN
                highest_temp_rec = r
            END IF
            IF r.temp < lowest_temp_rec.temp THEN
                lowest_temp_rec = r
            END IF
        END FOR  

        // --- Find record with highest rainfall
        SET max_rain_rec = valid_records[0]
        FOR EACH r IN valid_records DO 
            IF r.rainfall > max_rain_rec.rainfall THEN
                max_rain_rec = r
            END IF
        END FOR 
        // --- Count readings above 30°C ---
        SET above_30_count = 0
        FOR EACH r IN valid_records DO
            IF r.temp > 30 THEN
                above_30_count = above_30_count + 1
            END IF
        END FOR
        
        // --- Output results ---
        PRINT "Average Temperature : ", avg_temp (2 decimal places), "°C"
        PRINT "Average Rainfall    : ", avg_rain (2 decimal places), " mm"
        PRINT "Average Humidity    : ", avg_hum (2 decimal places), "%"
        PRINT "Average Wind Speed  : ", avg_wind (2 decimal places), " km/h"
        PRINT "Highest Temperature : ", highest_temp_rec.temp, "°C (Station: ", highest_temp_rec.station, ")"  
        PRINT "Lowest Temperature  : ", lowest_temp_rec.temp, "°C (Station: ", lowest_temp_rec.station, ")"
        PRINT "Highest Rainfall    : ", max_rain_rec.rainfall, " mm (Station: ", max_rain_rec.station, ")"
        PRINT "Readings > 30°C     : ", above_30_count
    END FUNCTION


    FUNCTION view_summary(valid_records,invalid_records):
        PRINT "DATASET SUMMARY OVERVIEW" header

        SET total_records = COUNT of valid_records + COUNT of invalid_records

        IF total_records == 0 THEN
            PRINT "No dataset loaded"
            RETURN
        END IF

        SET valid_count = COUNT of valid_records
        SET invalid_count = COUNT of invalid_records
        SET valid_percent = (valid_count/total_records) * 100
        SET invalid_percent = (invalid/total_records) * 100

        PRINT "Total Records Processed : ",total_records
        PRINT "Valid Records           : ",valid_count, "(",valid_percent(1 decimal place),"%)"
        PRINT "Invalid Records         : ",invalid_count,"("invalid_percent(1 decimal place),"%)"
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

    FUNCTION search_by_station(valid_records,invalid_records)
        PRINT "SEARCH BY STATION " header

         PROMPT user: "Enter station name to search: "
         SET query = user input, TRIMMED and CONVERTED TO LOWERCASE

         IF query IS EMPTY THEN
             PRINT "Search query cannot be empty."
             RETURN
         END IF
         //---Search valid records
         SET found_valid = EMPTY LIST
         FOR EACH r IN valid_records DO
             IF query IS SUBSTRING OF (r.station CONVERTED TO LOWERCASE) THEN
               ADD r TO found_valid
             END IF
         END FOR
         // --- Search invalid records ---
         SET found_invalid = EMPTY LIST
         FOR EACH (r, reasons) IN invalid_records DO
             IF query IS SUBSTRING OF (r.station CONVERTED TO LOWERCASE) THEN
                 ADD r TO found_invalid
             END IF
         END FOR
         // --- No matches at all ---
         IF found_valid IS EMPTY AND found_invalid IS EMPTY THEN
             PRINT "No records matching '", query, "' were found."
             RETURN
         END IF
         //---Display valid matches ---
         IF found_valid IS NOT EMPTY THEN
             PRINT blank line
             PRINT "Valid Records Found (", COUNT of found_valid, "):"
             FOR EACH r IN found_valid DO
                 PRINT "  • ", r.station, ": Temp=", r.temp, "°C, Rain=", r.rainfall,
                  "mm, Humidity=", r.humidity, "%, Wind=", r.wind_speed, "km/h"
             END FOR
         END IF 
         //---Display invalid matches ---
         IF found_invalid IS NOT EMPTY THEN
             PRINT blank line
             PRINT "Invalid Records Found (", COUNT of found_invalid, "):"
             FOR EACH (r, reasons) IN invalid_records DO
                 IF query IS SUBSTRING OF (r.station CONVERTED TO LOWERCASE) THEN
                    SET reasons_joined = reasons JOINED WITH ", "
                    PRINT "  • ", r.station, ": Temp=", r.temp, "°C | Rejections: ", reasons_joined
                 END IF
             END FOR
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


