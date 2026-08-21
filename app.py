import streamlit as st

# Custom styling: Comic Sans font & custom muted monochrome badge icons
st.set_page_config(page_title="Weather Analysis Tool", layout="wide")


st.markdown(
    """
    <style>
    /* Global Font Change - Target text elements specifically to avoid layout breakage */
    html, body, p, h1, h2, h3, h4, h5, h6, span, label, div {
        font-family: 'Comic Sans MS', 'Comic Sans', cursive, sans-serif !important;
    }

    /* Fix expander header line-height/alignment */
    [data-testid="stExpander"] details summary p {
        line-height: 1.5 !important;
    }

    /* Muted, monochrome tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 0.95rem;
        font-weight: bold;
        padding: 6px 14px;
        border-radius: 4px;
        background-color: #f0f2f6;
        color: #333333 !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #333333 !important;
        color: #ffffff !important;
    }
    
    /* Metric card styling adjustments */
    [data-testid="stMetricValue"] {
        font-family: 'Comic Sans MS', 'Comic Sans', cursive, sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True if hasattr(st, "allow_html") else True,
)

# Raw Dataset
RAW_WEATHER_DATA = [
    {"station": "Nairobi North", "temp": 22.5, "rainfall": 12.0, "humidity": 65, "wind_speed": 14.2},
    {"station": "Mombasa Port", "temp": 32.0, "rainfall": 0.0, "humidity": 85, "wind_speed": 18.5},
    {"station": "Eldoret High", "temp": 14.5, "rainfall": 25.4, "humidity": 78, "wind_speed": 8.0},
    {"station": "Nakuru Central", "temp": 28.1, "rainfall": 5.2, "humidity": 55, "wind_speed": 11.3},
    {"station": "Kisumu Bay", "temp": 33.5, "rainfall": -2.0, "humidity": 90, "wind_speed": 15.0},
    {"station": "Garissa Station", "temp": 55.0, "rainfall": 0.0, "humidity": 30, "wind_speed": 22.1},
    {"station": "Nyeri Hill", "temp": 18.0, "rainfall": 10.0, "humidity": 105, "wind_speed": 6.5},
    {"station": "Machakos East", "temp": 26.4, "rainfall": 1.5, "humidity": 60, "wind_speed": -4.0},
    {"station": "Lodwar Outpost", "temp": 36.8, "rainfall": 0.0, "humidity": 25, "wind_speed": 20.0},
    {"station": "Nairobi North", "temp": 19.0, "rainfall": 45.0, "humidity": 80, "wind_speed": 10.0},
]

# Validation Logic
def validate_record(record):
    reasons = []
    if not (-10 <= record["temp"] <= 50):
        reasons.append(f"Temperature ({record['temp']}°C) out of bounds [-10°C to 50°C]")
    if record["rainfall"] < 0:
        reasons.append(f"Rainfall ({record['rainfall']} mm) cannot be negative")
    if not (0 <= record["humidity"] <= 100):
        reasons.append(f"Humidity ({record['humidity']}%) out of bounds [0% to 100%]")
    if record["wind_speed"] < 0:
        reasons.append(f"Wind speed ({record['wind_speed']} km/h) cannot be negative")
    return len(reasons) == 0, reasons


def process_dataset(data):
    valid = []
    invalid = []
    for rec in data:
        is_valid, reasons = validate_record(rec)
        if is_valid:
            valid.append(rec)
        else:
            invalid.append((rec, reasons))
    return valid, invalid


valid_records, invalid_records = process_dataset(RAW_WEATHER_DATA)

# Title without colorful emoji
st.title("Weather Observation Analysis Dashboard")

# Navigation Tabs with monochrome UTF-8 symbols
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "[✓] Valid Readings", 
    "[▨] Weather Analysis", 
    "[⚲] Search Station", 
    "[▲] Temperature Classifications", 
    "[✕] Invalid Records",
    "[≡] Summary"
])

# Option 1: Valid Readings
with tab1:
    st.subheader("Valid Weather Readings")
    if not valid_records:
        st.info("No valid records found.")
    else:
        st.table([
            {
                "Station": r["station"],
                "Temp (°C)": f"{r['temp']:.1f}",
                "Rain (mm)": f"{r['rainfall']:.1f}",
                "Humidity (%)": r["humidity"],
                "Wind (km/h)": f"{r['wind_speed']:.1f}",
            }
            for r in valid_records
        ])

# Option 2: Weather Analysis
with tab2:
    st.subheader("Weather Data Analysis")
    if not valid_records:
        st.warning("Cannot perform analysis: No valid records available.")
    else:
        n = len(valid_records)
        avg_temp = sum(r["temp"] for r in valid_records) / n
        avg_rain = sum(r["rainfall"] for r in valid_records) / n
        avg_hum = sum(r["humidity"] for r in valid_records) / n
        avg_wind = sum(r["wind_speed"] for r in valid_records) / n

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Average Temperature", f"{avg_temp:.2f} °C")
        col2.metric("Average Rainfall", f"{avg_rain:.2f} mm")
        col3.metric("Average Humidity", f"{avg_hum:.2f} %")
        col4.metric("Average Wind Speed", f"{avg_wind:.2f} km/h")

        st.divider()

        highest_temp_rec = max(valid_records, key=lambda r: r["temp"])
        lowest_temp_rec = min(valid_records, key=lambda r: r["temp"])
        max_rain_rec = max(valid_records, key=lambda r: r["rainfall"])
        above_30_count = sum(1 for r in valid_records if r["temp"] > 30)

        st.markdown(f"• **Highest Temperature:** {highest_temp_rec['temp']}°C *(Station: {highest_temp_rec['station']})*")
        st.markdown(f"• **Lowest Temperature:** {lowest_temp_rec['temp']}°C *(Station: {lowest_temp_rec['station']})*")
        st.markdown(f"• **Highest Rainfall:** {max_rain_rec['rainfall']} mm *(Station: {max_rain_rec['station']})*")
        st.markdown(f"• **Readings > 30°C:** {above_30_count}")

# Option 3: Search by Station
with tab3:
    st.subheader("Search Records by Station")
    query = st.text_input("Enter station name to search:").strip().lower()

    if query:
        found_valid = [r for r in valid_records if query in r["station"].lower()]
        found_invalid = [r for r, _ in invalid_records if query in r["station"].lower()]

        if not found_valid and not found_invalid:
            st.error(f"No records matching '{query}' were found.")
        else:
            if found_valid:
                st.markdown(f"### Valid Records Found ({len(found_valid)})")
                st.table([
                    {
                        "Station": r["station"],
                        "Temp (°C)": r["temp"],
                        "Rain (mm)": r["rainfall"],
                        "Humidity (%)": r["humidity"],
                        "Wind (km/h)": r["wind_speed"],
                    }
                    for r in found_valid
                ])

            if found_invalid:
                st.markdown(f"### Invalid Records Found ({len(found_invalid)})")
                for r, reasons in [item for item in invalid_records if query in item[0]["station"].lower()]:
                    st.warning(f"**{r['station']}**: Temp={r['temp']}°C | Rejections: {', '.join(reasons)}")

# Option 4: Temperature Classifications
with tab4:
    st.subheader("Temperature Classifications")
    if not valid_records:
        st.info("No valid records to classify.")
    else:
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

        st.markdown("#### Classification Summary")
        for cat, count in counts.items():
            st.markdown(f"• **{cat}:** {count} reading(s)")

        st.markdown("#### Detailed Breakdown")
        for cat, stations in classified_details.items():
            stations_str = ", ".join(stations) if stations else "None"
            st.markdown(f"• **{cat}:** {stations_str}")

# Option 5: Invalid Records
with tab5:
    st.subheader("Invalid Records & Rejection Explanations")
    if not invalid_records:
        st.success("No invalid records found in the dataset.")
    else:
        for idx, (rec, reasons) in enumerate(invalid_records, 1):
            st.markdown(f"**{idx}. Station: {rec['station']}**")
            st.write(f"• **Data:** Temp={rec['temp']}°C, Rain={rec['rainfall']}mm, Humidity={rec['humidity']}%, Wind={rec['wind_speed']}km/h")
            for reason in reasons:
                st.caption(f"↳ {reason}")
            st.divider()                    

# Option 6: Summary
with tab6:
    st.subheader("Dataset Processing Summary Overview")
    total_records = len(valid_records) + len(invalid_records)
    if total_records == 0:
        st.info("No dataset loaded.")
    else:
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Records Processed", total_records)
        col2.metric("Valid Records", f"{len(valid_records)} ({len(valid_records)/total_records*100:.1f}%)")
        col3.metric("Invalid Records", f"{len(invalid_records)} ({len(invalid_records)/total_records*100:.1f}%)")