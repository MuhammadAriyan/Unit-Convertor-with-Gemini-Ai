import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()
# Dictionary of unit categories with their units
unitCategories = {
    "Area": [
        "Square Meter (m²)", "Square Kilometer (km²)", "Square Centimeter (cm²)",
        "Square Millimeter (mm²)", "Square Micrometer (µm²)", "Hectare (ha)",
        "Acre (ac)", "Square Mile (mi²)", "Square Yard (yd²)", "Square Foot (ft²)", "Square Inch (in²)"
    ],
    "Data Transfer Rate": [
        "Bits per second (bps)", "Kilobits per second (Kbps)", "Megabits per second (Mbps)", 
        "Gigabits per second (Gbps)", "Terabits per second (Tbps)", "Bytes per second (Bps)", 
        "Kilobytes per second (KBps)", "Megabytes per second (MBps)", "Gigabytes per second (GBps)"
    ],
    "Digital Storage": [
        "Bit (b)", "Byte (B)", "Kilobit (Kb)", "Kilobyte (KB)", "Megabit (Mb)", "Megabyte (MB)",
        "Gigabit (Gb)", "Gigabyte (GB)", "Terabit (Tb)", "Terabyte (TB)", "Petabyte (PB)", "Exabyte (EB)"
    ],
    "Energy": [
        "Joule (J)", "Kilojoule (kJ)", "Megajoule (MJ)", "Calorie (cal)", "Kilocalorie (kcal)", 
        "Electronvolt (eV)", "Watt-hour (Wh)", "Kilowatt-hour (kWh)", "Megawatt-hour (MWh)", 
        "British Thermal Unit (BTU)", "Foot-pound (ft⋅lb)", "Erg"
    ],
    "Frequency": [
        "Hertz (Hz)", "Kilohertz (kHz)", "Megahertz (MHz)", "Gigahertz (GHz)", "Terahertz (THz)", "Revolutions per Minute (RPM)"
    ],
    "Fuel Economy": [
        "Kilometers per liter (km/L)", "Miles per gallon (mpg US)", "Miles per gallon (mpg UK)", 
        "Liters per 100 kilometers (L/100km)", "Gallons per mile (gal/mi)"
    ],
    "Length": [
        "Meter (m)", "Kilometer (km)", "Decimeter (dm)", "Centimeter (cm)", "Millimeter (mm)", 
        "Micrometer (µm)", "Nanometer (nm)", "Mile (mi)", "Yard (yd)", "Foot (ft)", "Inch (in)", 
        "Nautical Mile (nmi)", "Light-Year", "Parsec (pc)", "Astronomical Unit (AU)"
    ],
    "Mass": [
        "Kilogram (kg)", "Gram (g)", "Milligram (mg)", "Microgram (µg)", "Ton (t)", 
        "Long Ton (UK)", "Short Ton (US)", "Pound (lb)", "Ounce (oz)", "Stone (st)", 
        "Carat (ct)", "Atomic Mass Unit (u)"
    ],
    "Plane Angle": [
        "Degree (°)", "Radian (rad)", "Gradian (gon)", "Minute of Arc (′)", "Second of Arc (″)", "Milliradian (mrad)"
    ],
    "Pressure": [
        "Pascal (Pa)", "Kilopascal (kPa)", "Hectopascal (hPa)", "Bar", "Millibar (mbar)", 
        "Atmosphere (atm)", "Torr (mmHg)", "Pound per square inch (psi)", "Megapascal (MPa)"
    ],
    "Speed": [
        "Meters per second (m/s)", "Kilometers per hour (km/h)", "Miles per hour (mph)", 
        "Feet per second (ft/s)", "Knots (kn)", "Mach (M)", "Speed of Light (c)"
    ],
    "Temperature": [
        "Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)", "Rankine (°R)", "Delisle (°D)", 
        "Newton (°N)", "Réaumur (°Ré)", "Rømer (°Rø)"
    ],
    "Time": [
        "Second (s)", "Millisecond (ms)", "Microsecond (µs)", "Nanosecond (ns)", 
        "Minute (min)", "Hour (h)", "Day (d)", "Week (wk)", "Month", "Year (yr)", 
        "Decade", "Century", "Millennium", "Planck Time"
    ],
    "Volume": [
        "Cubic Meter (m³)", "Cubic Centimeter (cm³)", "Liter (L)", "Milliliter (mL)", 
        "Cubic Foot (ft³)", "Cubic Inch (in³)", "Cubic Yard (yd³)", "Cup", "Pint (US)", 
        "Pint (UK)", "Quart (US)", "Quart (UK)", "Gallon (US)", "Gallon (UK)", "Barrel (Oil)"
    ]
}
# page configuration
st.set_page_config(page_title="Unit Converter", page_icon="📏",layout='centered')
# toast
# title of the app
st.title("Distance Converter 🎍")
# category selection 
unitCategory = st.selectbox("Select the unit category 🥓", list(unitCategories.keys()))
# 2 cols for both unit
col1,col2 = st.columns(2)
with col1:
    # slect initial unit
    initialUnit = st.selectbox("Select the initial unit ✨", unitCategories[unitCategory])
with col2:
    # select final unit
    finalUnit = st.selectbox("Select the final Unit 🎋", unitCategories[unitCategory])

# input value
initialValue = st.number_input("Enter the initial value 🎑", value=0.0)

# convert button   
if st.button("Convert"):
    # get the key
    api_key = os.getenv("api_key")
    # makes the client
    client = genai.Client(api_key=api_key)
    # response
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=f'''Convert {initialValue} {initialUnit} to {finalUnit}. Only return the numeric value followed by the unit. No explanations, no extra text.
        If the input is invalid, respond with: 'Oops, it's a string! Are you from Mars? 👽 and be creative with all errors but it should be one lineror less'''
    )
    # display the response
    st.subheader(response.text)
    st.balloons()
    st.toast('Conversion Successful! 🎉', icon="🎉")
st.snow()
