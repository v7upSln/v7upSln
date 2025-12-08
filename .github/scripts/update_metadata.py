import requests
import pytz
from datetime import datetime
import os
import re

def get_riyadh_time():
    riyadh_tz = pytz.timezone('Asia/Riyadh')
    riyadh_time = datetime.now(riyadh_tz)
    return riyadh_time.strftime("%I:%M %p, %B %d, %Y")

def get_riyadh_weather(api_key):
    if not api_key or api_key == "":
        return "Weather data unavailable"
    
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Riyadh&aqi=no"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if 'current' in data:
            temp_c = data['current']['temp_c']
            condition = data['current']['condition']['text']
            return f"{temp_c}°C, {condition}"
        else:
            return "Weather data unavailable"
    except:
        return "Weather data unavailable"

def update_readme():
    api_key = os.getenv('WEATHER_API_KEY', '')
    
    riyadh_time = get_riyadh_time()
    riyadh_weather = get_riyadh_weather(api_key)
    
    # Read the current README
    with open('README.md', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Update the time and weather section
    time_weather_section = f"""<!-- Saudi Arabia Riyadh Time & Weather -->
<div align="center">
  <h3>🌍 Saudi Arabia, Riyadh</h3>
  <p><strong>Current Time:</strong> {riyadh_time}</p>
  <p><strong>Weather:</strong> {riyadh_weather}</p>
</div>

###"""
    
    # Replace the section in README
    pattern = r'<!-- Saudi Arabia Riyadh Time & Weather -->.*?###'
    updated_content = re.sub(pattern, time_weather_section, content, flags=re.DOTALL)
    
    # Write back to README
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    print(f"Updated README with Riyadh time: {riyadh_time}")
    print(f"Weather: {riyadh_weather}")

if __name__ == "__main__":
    update_readme()
