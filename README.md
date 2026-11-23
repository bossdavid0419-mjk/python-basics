# 🐍 Python 기초 복습

> 전역 후 복학을 준비하면서 파이썬 기초를 처음부터 다시 다지는 학습 기록입니다.
> 매일 **개념 정리 노트**와 **직접 푼 실습 코드**를 함께 남기고 있습니다.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Study Days](https://img.shields.io/badge/학습일-Day%2012-success?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/bossdavid0419-mjk/python-basics?style=flat-square)

<br>

## 📚 학습 기록

| Day | 주제 | 주요 내용 | 노트 | 코드 |
|:---:|---|---|:---:|:---:|
| 1 | 변수와 문자열 | `input()`, `int()`, f-string | [📝](./notes/day01.md) | [💻](./practice/day_01) |
| 2 | 숫자와 연산 | `/`, `//`, `%`, `**` 연산자, 간단한 계산기 | [📝](./notes/day02.md) | [💻](./practice/day_02) |
| 3 | 리스트 | 인덱스, 슬라이싱, `append()`, `len()` | [📝](./notes/day03.md) | [💻](./practice/day_03) |
| 4 | 반복문 | `for`, `range()`, `while`, `break`, `continue` | [📝](./notes/day04.md) | [💻](./practice/day_04) |
| 5 | 딕셔너리 | 키:값 저장, 수정·추가·삭제 | [📝](./notes/day05.md) | [💻](./practice/day_05) |
| 6 | 딕셔너리 심화 | 중첩 자료구조, `.get()` | [📝](./notes/day06.md) | [💻](./practice/day_06) |
| 7 | 함수 | 매개변수, 반환값, 함수 안에서 함수 호출 | [📝](./notes/day07.md) | [💻](./practice/day_07) |
| 8 | **⭐ 미니 프로젝트** | 할 일 관리 프로그램 (파일 저장 기능 포함) | [📝](./notes/day08.md) | [💻](./practice/day_08) |
| 9 | 파일 다루기 | `open()`, `with`, `r`/`w`/`a` 모드 | [📝](./notes/day09.md) | [💻](./practice/day_09) |
| 10 | 예외 처리 | `try`/`except`, `ValueError`, `FileNotFoundError`, `OSError` | [📝](./notes/day10.md) | [💻](./practice/day_08) |
| 11 | 함수로 코드 정리 | 매개변수·반환값, `None`, 중복 코드를 함수로 분리 | [📝](./notes/day11.md) | [💻](./practice/day_11) |
| 12 | 필터와 검색 | 리스트 컴프리헨션, 문자열 `in`, 완료/미완료 필터 | [📝](./notes/day12.md) | [💻](./practice/day_12) |

<br>

## ⭐ 미니 프로젝트: 할 일 관리 프로그램

지금까지 배운 리스트, 딕셔너리, 함수, 반복문을 모아서 만든 콘솔 프로그램입니다.

- 할 일 **목록 보기 / 추가 / 완료 표시 / 삭제**
- 할 일 하나를 `{"title": ..., "done": ...}` 딕셔너리로 관리
- 💾 **파일 저장:** 바뀔 때마다 `todos.txt`에 저장하고, 실행할 때 다시 불러와서 껐다 켜도 목록이 유지됨 *(Day 9 파일 입출력 적용)*
- 🛡 **예외 처리:** 숫자가 아닌 입력은 `try/except ValueError`로, 저장 파일이 없을 때는 `FileNotFoundError`로 처리
- 🔎 **필터와 검색:** 완료/미완료 할 일만 보기, 제목으로 검색 *(Day 12 리스트 컴프리헨션 적용)*
- 🧩 **함수로 정리:** 입력·검사·출력을 작은 함수로 나누고, 메뉴 처리는 `run_menu()`로 분리 *(Day 11)*

```bash
python practice/day_08/day08_todo.py
```

<br>

## 🗺 앞으로의 계획 (2026.11 ~ 2027.02)

할 일 관리 프로그램을 Python → C++ → 웹 API 순서로 키우고, 이후 RAG와 ROS 2(자율주행 기초)로 넘어갑니다. C++과 ROS 2는 별도 저장소에 기록할 예정입니다.

| 기간 | 주제 | 결과물 | 상태 |
|---|---|---|:---:|
| 11/2 ~ 11/24 | Python 기초 (Day 1~12) | 할 일 관리 프로그램 v1 | ✅ |
| 11/23 ~ 11/29 | Python 마무리: 클래스·JSON·모듈·테스트 | 할 일 관리 프로그램 v2 | 🔄 |
| 11/30 ~ 12/13 | C++ 기초, 포인터, 객체지향, STL | 할 일 관리 프로그램 C++ 버전 | ⬜ |
| 12/14 ~ 12/20 | 자료구조·알고리즘 (스택, 큐, 해시, 정렬, 이분탐색) | 자료구조 구현 + 문제 기록 | ⬜ |
| 12/21 ~ 12/27 | Linux·운영체제 기초, Ubuntu 개발 환경 | Ubuntu 개발 환경 | ⬜ |
| 12/28 ~ 1/15 | AI 부트캠프 (LLM, 피지컬 AI 시뮬레이션, 헬스케어 로봇) | 부트캠프 결과물 정리 | ⬜ |
| 1/18 ~ 1/24 | 웹·DB 기초 (FastAPI, SQLite) | 할 일 관리 프로그램 v3 (REST API) | ⬜ |
| 1/25 ~ 1/31 | 로컬 AI·RAG 기초 (Ollama, PDF 추출, Chroma) | DriveNotes lite | ⬜ |
| 2/1 ~ 2/21 | ROS 2 기초 (노드·토픽, C++ 노드, 센서 데이터) | ROS 2 미니 프로젝트 | ⬜ |
| 2/22 ~ 2/28 | 운영체제·DB 정리, 포트폴리오, 복학 준비 | GitHub 포트폴리오 | ⬜ |

✅ 완료 · 🔄 진행 중 · ⬜ 예정

<br>

## 🗂 폴더 구조

```
python-basics/
├── notes/          # 날짜별 학습 노트 (배운 것 · 어려웠던 점 · 해결 방법)
│   ├── day01.md
│   └── ...
├── practice/       # 날짜별 실습 코드와 문제 풀이
│   ├── day_01/
│   └── ...
└── make_study_plan_pdf.py   # 학습 계획표 PDF 생성 스크립트
```

<br>

## ✍️ 커밋 규칙

| 태그 | 의미 | 예시 |
|---|---|---|
| `practice:` | 실습 코드·문제 풀이 | `practice: Day 9 파일 다루기 실습 추가` |
| `docs:` | 학습 노트·README | `docs: Day 9 학습 노트 추가` |
| `feat:` | 프로그램 기능 추가 | `feat: 할 일 목록 파일 저장 기능` |
| `fix:` | 버그 수정 | `fix: 할 일 관리 메뉴 번호 오류 수정` |
