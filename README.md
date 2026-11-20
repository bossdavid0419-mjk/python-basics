# 🐍 Python 기초 복습

> 전역 후 복학을 준비하면서 파이썬 기초를 처음부터 다시 다지는 학습 기록입니다.
> 매일 **개념 정리 노트**와 **직접 푼 실습 코드**를 함께 남기고 있습니다.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Study Days](https://img.shields.io/badge/학습일-Day%209-success?style=flat-square)
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
| 8 | **⭐ 미니 프로젝트** | 할 일 관리 프로그램 | [📝](./notes/day08.md) | [💻](./practice/day_08) |
| 9 | 파일 다루기 | `open()`, `with`, `r`/`w`/`a` 모드 | [📝](./notes/day09.md) | [💻](./practice/day_09) |

<br>

## ⭐ 미니 프로젝트: 할 일 관리 프로그램

지금까지 배운 리스트, 딕셔너리, 함수, 반복문을 모아서 만든 콘솔 프로그램입니다.

- 할 일 **추가 / 목록 보기 / 완료 표시 / 삭제**
- 할 일 하나를 `{"title": ..., "done": ...}` 딕셔너리로 저장
- 기능마다 함수를 따로 나누고, `while` 메뉴 루프로 계속 실행
- 빈 입력과 잘못된 번호를 검사

```bash
python practice/day_08/day08_todo.py
```

<br>

## 🗺 앞으로의 계획 (2026.11 ~ 2027.02)

| 시기 | 주제 | 상태 |
|---|---|:---:|
| 1~2주차 | 딕셔너리 심화, 함수 기초 | ✅ |
| 3~4주차 | 함수 심화, 파일 입출력, 예외 처리 | 🔄 |
| 5~6주차 | 할 일 관리 프로그램 완성 및 정리 | 🔄 |
| 7~8주차 | 자료구조·알고리즘 기초 (스택, 큐, 해시) | ⬜ |
| 9~10주차 | 정렬, 이분탐색, BFS·DFS 기초 | ⬜ |
| 11~12주차 | 웹·DB 기초 (FastAPI 또는 Django, SQLite) | ⬜ |
| 13~14주차 | 로컬 AI·RAG 기초 (Ollama, PDF 추출, Chroma) | ⬜ |
| 15~16주차 | **최종 프로젝트:** 근거 기반 로컬 RAG 앱 | ⬜ |

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
