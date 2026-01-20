# 🎣 낚시대장의 실전 조행기

관리형 저수지 플라이 낚시의 생생한 현장 기록과 데이터를 공유합니다.

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-success)](https://caddis-gr.github.io/fishing-log/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📊 2025년 출조 통계

메인: https://caddis-gr.github.io/fishing-log/index.html

**총 조행**: 5회  
**총 캐치**: 63마리  
**방문 낚시터**: 2곳  
**평균 마릿수**: 12.6마리

### 📍 방문 낚시터
- 🏔️ **용인 한터낚시터** (2회)
- 🌊 **신기사낚시터** (3회)

## 📅 2024-2025 시즌 조행 목록

### 🍂 가을 시즌
- **[11.15] 한터치 조행기** - 바닥 공략의 핵심 ([상세보기](logs/2024-11-15-hanteo.html))
  - 📍 용인 한터낚시터 | 🎯 15마리 | 🌡️ 5°C
  - 🎣 주요 패턴: Vampire Leech, Chironomid
  - 💡 핵심: Deep Lining 전략 수립

- **[11.29] 신기사 조행기 (A)** - 늦가을 저수온 공략 ([상세보기](logs/2024-11-29-singisa.html))
  - 📍 신기사낚시터 | 🎯 12마리 | 🌡️ 3°C
  - 🎣 주요 패턴: Streamer, Nymph
  - 💡 핵심: 저수온기 스트리머 전략

### ❄️ 겨울 시즌
- **[12.13] 신기사 조행기 (B)** - 한파 속 송어 공략 ([상세보기](logs/2024-12-13-singisa.html))
  - 📍 신기사낚시터 | 🎯 8마리 | 🌡️ -2°C
  - 🎣 주요 패턴: Woolly Bugger, Leech
  - 💡 핵심: 한파 대응 바닥 집중

- **[12.20] 한터치 후기** - Deep Lining 검증 ([상세보기](logs/2024-12-20-hanteo.html))
  - 📍 용인 한터낚시터 | 🎯 18마리 | 🌡️ 0°C
  - 🎣 주요 패턴: Chironomid, Bloodworm
  - 💡 핵심: Deep Lining 효과 재확인

- **[01.04] 신기사 조행기 (2025)** - 새해 첫 출조 ([상세보기](logs/2025-01-04-singisa.html))
  - 📍 신기사낚시터 | 🎯 10마리 | 🌡️ -5°C
  - 🎣 주요 패턴: Streamer #8, Leech
  - 💡 핵심: 강추위 느린 리트리브

## 🛠️ 주요 장비

### 로드 & 라인
- **Sage Foundation 690-4** + Rio Elite Stillwater Floater WF5F
- **SCOTT CENTRIC 690-4** + SA Sonar Titan 3D i/3/5 WF6S
- **Sage R8 Core 4100-4** + SA Sonar Sink 25 Cold (Sink 6)

### 효과적인 패턴
- 🔴 **Vampire Leech** - 한터지 최고 히트 패턴
- ⚫ **Chironomid Pupa** - 저수온기 필수
- 🟤 **Woolly Bugger** - 만능 스트리머
- 🔵 **Bloodworm** - 바닥 공략

## 📖 프로젝트 구조

```
fishing-log/
├── index.html              # 메인 대시보드 (조행기 목록)
├── logs/                   # 개별 조행기 HTML 파일들
│   ├── 1115_인터치_조행기.html
│   ├── 1129-신기사춤조후기.html
│   ├── 1213-신기사춤조후기.html
│   ├── 251220-한터치후기.html
│   └── 26-0104-신기사_조행기.html
├── weather_log.md          # 날씨 기록
├── update_weather.py       # 날씨 자동화 스크립트
└── .github/workflows/      # GitHub Actions
```

## 🚀 사용 방법

### 웹에서 보기
[https://caddis-gr.github.io/fishing-log/](https://caddis-gr.github.io/fishing-log/)

### 로컬에서 보기
```bash
git clone https://github.com/CADDIS-GR/fishing-log.git
cd fishing-log
# index.html을 브라우저로 열기
```

## 🎯 조행기 작성 가이드

새로운 조행기를 추가하려면:

1. `logs/` 폴더에 새 HTML 파일 생성
2. 기존 조행기 템플릿 참고
3. `index.html`의 `logsData` 배열에 정보 추가

```javascript
{
    id: 'filename',
    date: '2025-01-20',
    location: '낚시터명',
    weather: '☀️',
    temp: 5,
    waterTemp: 8,
    season: 'winter',
    summary: '조행 요약',
    patterns: ['패턴1', '패턴2'],
    species: ['어종'],
    catch: 15,
    size: 40,
    notes: '메모',
    file: 'logs/filename.html'
}
```

## 💡 주요 인사이트

### 한터낚시터 공략법
- ✅ **수심**: 6m 깊은 저수지
- ✅ **핵심**: 바닥(Bottom) 공략이 필수
- ✅ **전략**: 풀싱킹 라인 + Deep Lining 조합
- ✅ **패턴**: Vampire Leech, Chironomid

### 신기사낚시터 공략법
- ✅ **특징**: 저수온기 반응 좋음
- ✅ **전략**: 스트리머 중심 공략
- ✅ **패턴**: Woolly Bugger, Leech
- ✅ **팁**: 느린 리트리브가 효과적

## 📈 시즌별 통계

| 시즌 | 조행 | 캐치 | 평균 |
|------|------|------|------|
| 가을 | 2회 | 27마리 | 13.5 |
| 겨울 | 3회 | 36마리 | 12.0 |

## 🤝 기여하기

이 저장소는 개인 조행 기록용이지만, 플라이낚시 커뮤니티를 위해 공개합니다.  
질문이나 제안사항은 Issue로 남겨주세요!

## 📝 라이선스

MIT License - 자유롭게 참고하세요!

## 📧 연락처

- GitHub: [@CADDIS-GR](https://github.com/CADDIS-GR)
- Blog: 낚시대장의 실전 조행기

---

**"같은 필드에서도 다양한 기법과 공략으로 서로 다른 결과를 만들어 내는 게 낚시입니다."**

🎣 Tight Lines!
