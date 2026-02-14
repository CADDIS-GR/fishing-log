# 🎣 낚시대장의 실전 조행기

관리형 저수지 플라이 낚시의 생생한 현장 기록과 데이터를 공유합니다.

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-success)](https://caddis-gr.github.io/fishing-log/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📊 2024-2026 시즌 통계

메인: https://caddis-gr.github.io/fishing-log/index.html

**총 조행**: 6회  
**총 캐치**: 95마리  
**방문 낚시터**: 2곳  
**평균 마릿수**: 15.8마리

### 📍 방문 낚시터
- 🏔️ **용인 한터낚시터** (3회)
- 🌊 **신기사낚시터** (3회)

## 📅 조행 목록

### ❄️ 2026 겨울 시즌

- **[02.14] 한터낚시터** - 한파 끝, 32수의 정교한 기록 ⭐ NEW ([상세보기](logs/2026-02-14_hanter.html))
  - 📍 용인 한터낚시터 | 🎯 32마리 | 🌡️ 3°C
  - 🎣 주요 패턴: Zonker Tail Mini Leech #16, White Chironomid, Chironomid Larva (Red Dot)
  - 💡 핵심: 수평에서 수직으로 상승하는 슬로프 구간 입질 집중 / White MVP / Technical Trout Line 첫 투입

### ❄️ 2024-2025 겨울 시즌

- **[01.04] 신기사 조행기 (2025)** - 새해 첫 출조 ([상세보기](logs/2025-01-04-singisa.html))
  - 📍 신기사낚시터 | 🎯 10마리 | 🌡️ -5°C
  - 🎣 주요 패턴: Streamer #8, Leech
  - 💡 핵심: 강추위 느린 리트리브

- **[12.20] 한터낚시터** - Deep Lining 검증 ([상세보기](logs/2024-12-20-hanteo.html))
  - 📍 용인 한터낚시터 | 🎯 18마리 | 🌡️ 0°C
  - 🎣 주요 패턴: Chironomid, Bloodworm
  - 💡 핵심: Deep Lining 효과 재확인

- **[12.13] 신기사 조행기 (B)** - 한파 속 송어 공략 ([상세보기](logs/2024-12-13-singisa.html))
  - 📍 신기사낚시터 | 🎯 8마리 | 🌡️ -2°C
  - 🎣 주요 패턴: Woolly Bugger, Leech
  - 💡 핵심: 한파 대응 바닥 집중

### 🍂 2024 가을 시즌

- **[11.29] 신기사 조행기 (A)** - 늦가을 저수온 공략 ([상세보기](logs/2024-11-29-singisa.html))
  - 📍 신기사낚시터 | 🎯 12마리 | 🌡️ 3°C
  - 🎣 주요 패턴: Streamer, Nymph
  - 💡 핵심: 저수온기 스트리머 전략

- **[11.15] 한터낚시터** - 바닥 공략의 핵심 ([상세보기](logs/2024-11-15-hanteo.html))
  - 📍 용인 한터낚시터 | 🎯 15마리 | 🌡️ 5°C
  - 🎣 주요 패턴: Vampire Leech, Chironomid
  - 💡 핵심: Deep Lining 전략 수립

## 🛠️ 주요 장비

### 로드 & 라인
- **Sage Foundation 690-4** + Rio Elite Stillwater Floater WF5F
- **SCOTT CENTRIC 690-4** + SA Sonar Titan 3D i/3/5 WF6S
- **Vision Onki 3100-4** + Rio Elite Technical Trout WF4F *(2026 신규 투입)*
- **Sage R8 Core 4100-4** + SA Sonar Sink 25 Cold (Sink 6)

### 효과적인 패턴
- 🤍 **Zonker Tail Mini Leech** - 슬로프 수직 상승 구간 MVP *(2026 신규)*
- 🔴 **Vampire Leech** - 한터지 최고 히트 패턴
- ⚫ **Chironomid Pupa / Larva** - 저수온기 필수
- 🟤 **Woolly Bugger** - 만능 스트리머
- 🔵 **Bloodworm** - 바닥 공략

## 📖 프로젝트 구조

```
fishing-log/
├── index.html              # 메인 대시보드 (조행기 목록)
├── images/                 # 현장 사진
│   ├── HanTer.JPEG
│   ├── Fly01~03.JPEG
│   ├── Trout01~05.JPEG
│   ├── Gear.JPEG
│   └── field-bg.jpg
├── logs/                   # 개별 조행기 HTML 파일들
│   ├── 2026-02-14_hanter.html   ⭐ NEW
│   ├── 2025-01-04-singisa.html
│   ├── 2024-12-20-hanteo.html
│   ├── 2024-12-13-singisa.html
│   ├── 2024-11-29-singisa.html
│   └── 2024-11-15-hanteo.html
└── README.md
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

1. `logs/` 폴더에 `YYYY-MM-DD_location.html` 형식으로 파일 생성
2. `index.html`의 `logsData` 배열에 항목 추가

```javascript
{
    id: '2026-02-14-hanter',
    date: '2026-02-14',
    location: '용인 한터낚시터',
    weather: '☀️',
    temp: 3,
    waterTemp: 5,
    season: 'winter',
    summary: '조행 요약',
    patterns: ['패턴1', '패턴2'],
    species: ['무지개송어'],
    catch: 32,
    notes: '메모',
    file: 'logs/2026-02-14_hanter.html'
}
```

## 💡 주요 인사이트

### 한터낚시터 공략법
- ✅ **수심**: 6m 깊은 저수지
- ✅ **핵심**: 바닥(Bottom) 공략 후 슬로프 수직 상승 구간 노리기
- ✅ **전략**: 풀싱킹 라인 + Deep Lining 조합
- ✅ **패턴**: Zonker Tail Mini Leech, Vampire Leech, Chironomid
- ✅ **2026 발견**: 수평 리트리브 → 수직 상승 변화 구간에서 입질 집중

### 신기사낚시터 공략법
- ✅ **특징**: 저수온기 반응 좋음
- ✅ **전략**: 스트리머 중심 공략
- ✅ **패턴**: Woolly Bugger, Leech
- ✅ **팁**: 느린 리트리브가 효과적

## 📈 시즌별 통계

| 시즌 | 조행 | 캐치 | 평균 |
|------|------|------|------|
| 2024 가을 | 2회 | 27마리 | 13.5 |
| 2024-25 겨울 | 3회 | 36마리 | 12.0 |
| 2026 겨울 | 1회 | 32마리 | 32.0 |
| **합계** | **6회** | **95마리** | **15.8** |

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
