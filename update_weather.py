import requests
import os
from datetime import datetime

API_KEY = os.environ.get('WEATHER_API_KEY')
CITY = "Gimpo,KR" # 더 정확하게 한국 김포로 지정

print(f"--- 낚시터 날씨 확인 시작 (도시: {CITY}) ---")

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url).json()
    if response.get("cod") != 200:
        print(f"❌ 날씨 정보를 못 가져왔어요: {response.get('message')}")
        exit(0) # 에러로 중단시키지 않고 조용히 종료

    temp = response['main']['temp']
    weather = response['weather'][0]['description']
    humidity = response['main']['humidity']
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    log_line = f"| {date} | {temp}°C | {weather} | {humidity}% |\n"
    print(f"✅ 기록할 내용: {log_line}")

    with open("weather_log.md", "a", encoding="utf-8") as f:
        f.write(log_line)

except Exception as e:
    print(f"❌ 예상치 못한 오류 발생: {e}")
