#Member 1
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
#Member 3
#Member 4
#Member 1