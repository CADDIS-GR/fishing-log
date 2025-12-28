import requests
import os
from datetime import datetime

# 설정: GitHub Secrets에서 가져온 API 키 사용
API_KEY = os.environ.get('WEATHER_API_KEY')
CITY = "Gimpo"

if not API_KEY:
    print("에러: WEATHER_API_KEY를 찾을 수 없습니다.")
    exit(1)

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url).json()
    if response.get("cod") != 200:
        print(f"API 에러: {response.get('message')}")
        exit(1)

    temp = response['main']['temp']
    weather = response['weather'][0]['description']
    humidity = response['main']['humidity']
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    log_line = f"| {date} | {temp}°C | {weather} | {humidity}% |\n"
    
    # 기록할 파일 열기
    with open("weather_log.md", "a", encoding="utf-8") as f:
        f.write(log_line)
        
    print(f"성공적으로 날씨를 적었습니다: {log_line}")

except Exception as e:
    print(f"연결 오류: {e}")
    exit(1)
