# Test Documentation — Weather Observation Analysis Tool

| Test ID | Category | Test Input / Condition | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC01** | **Normal** | Record: `{"station": "Nairobi North", "temp": 22.5, "rainfall": 12.0, "humidity": 65, "wind_speed": 14.2}` | Record passes validation and is included in analysis. | Processed successfully and categorized as Moderate. | **PASS** |
| **TC02** | **Invalid** | Record: `{"station": "Garissa Station", "temp": 55.0, ...}` (Temp > 50°C) | Record rejected with explicit explanation. | Rejected with reason: *"Temperature (55.0°C) out of bounds [-10°C to 50°C]"* displayed in Option 5. | **PASS** |
| **TC03** | **Invalid** | Record: `{"station": "Thika","rainfall":-12mm,...}` (Rainfall >= 0) | Record rejected with explicit explanation. | Rejected with reason: *"Rainfall(-12 mm) out of bounds [>=0 mm]"* displayed in Option 5. | **PASS** |
| **TC04** | **Invalid** | Record: `{"station": "Thika","humidity": 135%,...}` (Humidity 0%-100%) | Record rejected with explicit explanation. | Rejected with reason: *"Humidity(135%) out of bounds [0%-100%]"* displayed in Option 5. |**PASS** |
| **TC05** | **Invalid** | Record: `{"station": "Dagoretti","temp": Null,...}` (Temp >50°C) | Record rejected with explicit explanation. | Rejected with reason: *"Temp(None) out of bounds [-10°C to 50°C]"* displayed in Option 5. |**PASS**|
| **TC06** | **Boundary**| Record: `{"station": "Nyeri Hill", "temp": 20.0, ...}` (Exactly on 20°C limit) | Classified as **Moderate (20–30°C)** according to boundary condition (20 ≤ T ≤ 30). | Displayed under Moderate category in Option 4. | **PASS** |
| **TC07** | **Search**   | Query: `"Nairobi"` (Existing) & `"Atlantis"` (Non-existing) | `"Nairobi"` lists matching records; `"Atlantis"` displays "No records matching found". | Exact matches listed for Nairobi; clear error notice displayed for Atlantis. | **PASS** |
| **TC08** | **Search** | Query: `" "` or `""` (Empty string/spaces input for search) | Handles empty search input gracefully without program crash. | Displays prompt requiring valid station name or returns no matches notice. | **PASS** |
| **TC09** | **Menu**     | Input: Choice `9` (Invalid) and Choice `7` (Exit) | Choice `9` prints error message and repeats menu. Choice `7` displays goodbye message and exits cleanly. | Menu prompts retry on `9`, terminates execution on `7`. | **PASS** |
