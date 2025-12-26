import requests
import os
from datetime import datetime

# 설정: API 키와 도시 (낚시대장님이 자주 가시는 지역으로 변경 가능)
API_KEY = os.environ['WEATHER_API_KEY']
CITY = "Gimpo" # 김포 인근 저수지를 위해 김포로 설정

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url).json()
    temp = response['main']['temp']
    weather = response['weather'][0]['description']
    humidity = response['main']['humidity']
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    # weather_log.md 파일에 데이터 추가
    log_line = f"| {date} | {temp}°C | {weather} | {humidity}% |\n"
    
    with open("weather_log.md", "a", encoding="utf-8") as f:
        f.write(log_line)
        
    print(f"성공적으로 기록되었습니다: {log_line}")

except Exception as e:
    print(f"에러 발생: {e}")
