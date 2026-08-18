#Member 1
# Raw Dataset Storage
RAW_WEATHER_DATA = [
    {"station": "Nairobi North", "temp": 22.5, "rainfall": 12.0, "humidity": 65, "wind_speed": 14.2},
    {"station": "Mombasa Port", "temp": 32.0, "rainfall": 0.0, "humidity": 85, "wind_speed": 18.5},
    {"station": "Eldoret High", "temp": 14.5, "rainfall": 25.4, "humidity": 78, "wind_speed": 8.0},
    {"station": "Nakuru Central", "temp": 28.1, "rainfall": 5.2, "humidity": 55, "wind_speed": 11.3},
    {"station": "Kisumu Bay", "temp": 33.5, "rainfall": -2.0, "humidity": 90, "wind_speed": 15.0},      # Invalid: Negative rainfall
    {"station": "Garissa Station", "temp": 55.0, "rainfall": 0.0, "humidity": 30, "wind_speed": 22.1},    # Invalid: Temp > 50°C
    {"station": "Nyeri Hill", "temp": 18.0, "rainfall": 10.0, "humidity": 105, "wind_speed": 6.5},        # Invalid: Humidity > 100%
    {"station": "Machakos East", "temp": 26.4, "rainfall": 1.5, "humidity": 60, "wind_speed": -4.0},      # Invalid: Negative wind speed
    {"station": "Lodwar Outpost", "temp": 36.8, "rainfall": 0.0, "humidity": 25, "wind_speed": 20.0},
    {"station": "Nairobi North", "temp": 19.0, "rainfall": 45.0, "humidity": 80, "wind_speed": 10.0},
]
#Member 2
def validate_record(record):
    """
    Validates weather readings based on domain rules.
    Returns a tuple: (is_valid: bool, rejection_reasons: list)
    """
    reasons = []
    
    # Rule 1: Temperature is between -10°C and 50°C
    if not (-10 <= record["temp"] <= 50):
        reasons.append(f"Temperature ({record['temp']}°C) out of bounds [-10°C to 50°C]")
        
    # Rule 2: Rainfall is zero or greater
    if record["rainfall"] < 0:
        reasons.append(f"Rainfall ({record['rainfall']} mm) cannot be negative")
        
    # Rule 3: Humidity is between 0% and 100%
    if not (0 <= record["humidity"] <= 100):
        reasons.append(f"Humidity ({record['humidity']}%) out of bounds [0% to 100%]")
        
    # Rule 4: Wind speed is zero or greater
    if record["wind_speed"] < 0:
        reasons.append(f"Wind speed ({record['wind_speed']} km/h) cannot be negative")
        
    return len(reasons) == 0, reasons


def process_dataset(data):
    """
    Processes the raw dataset into separate valid and invalid lists.
    """
    valid = []
    invalid = []
    for rec in data:
        is_valid, reasons = validate_record(rec)
        if is_valid:
            valid.append(rec)
        else:
            invalid.append((rec, reasons))
    return valid, invalid


def view_invalid_records(invalid_records):
    """Option 5: View invalid records with rejection explanations."""
    print("\n--- INVALID RECORDS & REJECTION REASONS ---")
    if not invalid_records:
        print("No invalid records found in the dataset.")
        return

    for idx, (rec, reasons) in enumerate(invalid_records, 1):
        print(f"\n{idx}. Station: {rec['station']}")
        print(f"   Data: Temp={rec['temp']}°C, Rain={rec['rainfall']}mm, Humidity={rec['humidity']}%, Wind={rec['wind_speed']}km/h")
        print("   Rejection Reason(s):")
        for reason in reasons:
            print(f"     - {reason}")
#Member 1
def view_valid_readings(valid_records):
    """Option 1: View valid weather readings in formatted tabular form."""
    print("\n--- VALID WEATHER READINGS ---")
    if not valid_records:
        print("No valid records found.")
        return

    header = f"{'Station':<18} | {'Temp (°C)':<10} | {'Rain (mm)':<10} | {'Humidity (%)':<12} | {'Wind (km/h)':<10}"
    print(header)
    print("-" * len(header))

    for r in valid_records:
        print(f"{r['station']:<18} | {r['temp']:<10.1f} | {r['rainfall']:<10.1f} | {r['humidity']:<12} | {r['wind_speed']:<10.1f}")


#Member 3
def analyse_weather(valid_records):
    """Option 2: Calculate averages, extrema, peak rainfall, and high temp count."""
    print("\n--- WEATHER ANALYSIS ---")
    if not valid_records:
        print("Cannot perform analysis: No valid records available.")
        return

    n = len(valid_records)
    avg_temp = sum(r["temp"] for r in valid_records) / n
    avg_rain = sum(r["rainfall"] for r in valid_records) / n
    avg_hum = sum(r["humidity"] for r in valid_records) / n
    avg_wind = sum(r["wind_speed"] for r in valid_records) / n

    highest_temp_rec = max(valid_records, key=lambda r: r["temp"])
    lowest_temp_rec = min(valid_records, key=lambda r: r["temp"])
    max_rain_rec = max(valid_records, key=lambda r: r["rainfall"])
    above_30_count = sum(1 for r in valid_records if r["temp"] > 30)

    print(f"Average Temperature : {avg_temp:.2f}°C")
    print(f"Average Rainfall    : {avg_rain:.2f} mm")
    print(f"Average Humidity    : {avg_hum:.2f}%")
    print(f"Average Wind Speed  : {avg_wind:.2f} km/h")
    print(f"Highest Temperature : {highest_temp_rec['temp']}°C (Station: {highest_temp_rec['station']})")
    print(f"Lowest Temperature  : {lowest_temp_rec['temp']}°C (Station: {lowest_temp_rec['station']})")
    print(f"Highest Rainfall    : {max_rain_rec['rainfall']} mm (Station: {max_rain_rec['station']})")
    print(f"Readings > 30°C     : {above_30_count}")


def view_summary(valid_records, invalid_records):
    """Option 6: View dataset processing summary overview."""
    print("\n--- DATASET SUMMARY OVERVIEW ---")
    total_records = len(valid_records) + len(invalid_records)
    if total_records == 0:
        print("No dataset loaded.")
        return

    print(f"Total Records Processed : {total_records}")
    print(f"Valid Records           : {len(valid_records)} ({len(valid_records)/total_records*100:.1f}%)")
    print(f"Invalid Records         : {len(invalid_records)} ({len(invalid_records)/total_records*100:.1f}%)")

#Member 4
def view_temperature_classifications(valid_records):
    """Option 4: Classify temperatures as Cold (<20°C), Moderate (20–30°C), or Hot (>30°C)."""
    print("\n--- TEMPERATURE CLASSIFICATIONS ---")
    if not valid_records:
        print("No valid records to classify.")
        return

    counts = {"Cold (<20°C)": 0, "Moderate (20–30°C)": 0, "Hot (>30°C)": 0}
    classified_details = {"Cold (<20°C)": [], "Moderate (20–30°C)": [], "Hot (>30°C)": []}

    for r in valid_records:
        t = r["temp"]
        if t < 20:
            category = "Cold (<20°C)"
        elif 20 <= t <= 30:
            category = "Moderate (20–30°C)"
        else:
            category = "Hot (>30°C)"

        counts[category] += 1
        classified_details[category].append(f"{r['station']} ({t}°C)")

    print("\nClassification Summary:")
    for cat, count in counts.items():
        print(f"  • {cat:<18}: {count} reading(s)")

    print("\nDetailed Breakdown:")
    for cat, stations in classified_details.items():
        stations_str = ", ".join(stations) if stations else "None"
        print(f"  • {cat:<18}: {stations_str}")


def search_by_station(valid_records, invalid_records):
    """Option 3: Search for a station and display its valid and invalid records."""
    print("\n--- SEARCH BY STATION ---")
    query = input("Enter station name to search: ").strip().lower()

    if not query:
        print("Search query cannot be empty.")
        return

    found_valid = [r for r in valid_records if query in r["station"].lower()]
    found_invalid = [r for r, _ in invalid_records if query in r["station"].lower()]

    if not found_valid and not found_invalid:
        print(f"No records matching '{query}' were found.")
        return

    if found_valid:
        print(f"\nValid Records Found ({len(found_valid)}):")
        for r in found_valid:
            print(f"  • {r['station']}: Temp={r['temp']}°C, Rain={r['rainfall']}mm, Humidity={r['humidity']}%, Wind={r['wind_speed']}km/h")

    if found_invalid:
        print(f"\nInvalid Records Found ({len(found_invalid)}):")
        for r, reasons in [item for item in invalid_records if query in item[0]["station"].lower()]:
            print(f"  • {r['station']}: Temp={r['temp']}°C | Rejections: {', '.join(reasons)}")


#Member 1
def display_menu():
    """Displays the interactive menu choices."""
    print("\n========================================")
    print("   WEATHER OBSERVATION ANALYSIS TOOL    ")
    print("========================================")
    print("1. View valid readings")
    print("2. Analyse weather")
    print("3. Search by station")
    print("4. View temperature classifications")
    print("5. View invalid records")
    print("6. View summary")
    print("7. Exit")
    print("========================================")


def main():
    # Pre-process raw records on startup
    valid_records, invalid_records = process_dataset(RAW_WEATHER_DATA)

    while True:
        display_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            view_valid_readings(valid_records)
        elif choice == "2":
            analyse_weather(valid_records)
        elif choice == "3":
            search_by_station(valid_records, invalid_records)
        elif choice == "4":
            view_temperature_classifications(valid_records)
        elif choice == "5":
            view_invalid_records(invalid_records)
        elif choice == "6":
            view_summary(valid_records, invalid_records)
        elif choice == "7":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\n[ERROR] Invalid selection. Please choose a number between 1 and 7.")


if __name__ == "__main__":
    main()
