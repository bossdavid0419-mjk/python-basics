from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from datetime import date, timedelta
import os

font_path = "fonts/NanumGothic.ttf"

pdfmetrics.registerFont(TTFont("Korean", font_path))

base = getSampleStyleSheet()

title_style = ParagraphStyle(
    name="TitleKR",
    parent=base["Title"],
    fontName="Korean",
    fontSize=20,
    leading=26
)

h2_style = ParagraphStyle(
    name="H2KR",
    parent=base["Heading2"],
    fontName="Korean",
    fontSize=14,
    leading=18,
    spaceBefore=10,
    spaceAfter=6
)

body_style = ParagraphStyle(
    name="BodyKR",
    parent=base["BodyText"],
    fontName="Korean",
    fontSize=10,
    leading=14
)

cell_style = ParagraphStyle(
    name="CellKR",
    parent=base["BodyText"],
    fontName="Korean",
    fontSize=9,
    leading=12
)

small_style = ParagraphStyle(
    name="SmallKR",
    parent=base["BodyText"],
    fontName="Korean",
    fontSize=8,
    leading=11,
    textColor=colors.gray
)

start = date(2026, 11, 16)
end = date(2027, 2, 28)

plan = []
current = start
week_num = 1

while current <= end:
    if current.weekday() in [0, 2, 4]:
        plan.append((current, f"{week_num}주차 코딩 공부일"))
    elif current.weekday() in [1, 3]:
        plan.append((current, "휴식"))
    else:
        plan.append((current, "클로드 공부"))
    if current.weekday() == 4:
        week_num += 1
    current += timedelta(days=1)

rows = [["날짜", "요일", "계획"]]

weekday_ko = ["월", "화", "수", "목", "금", "토", "일"]

for d, label in plan:
    rows.append([
        d.isoformat(),
        weekday_ko[d.weekday()],
        label
    ])

table = Table(rows, colWidths=[80, 40, 340])

table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563eb")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, -1), "Korean"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#cbd5e1")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")])
]))

doc = SimpleDocTemplate(
    "output/2026-11-16_to_2027-02-28_study_plan_kr.pdf",
    pagesize=A4,
    rightMargin=36,
    leftMargin=36,
    topMargin=42,
    bottomMargin=36
)

story = [
    Paragraph("2026년 11월 16일 ~ 2027년 2월 28일<br/>개인 학습 계획표", title_style),
    Spacer(1, 8),
    Paragraph("현재 진도 기준: Python 기초 복습 및 딕셔너리 심화 진행 중<br/>코딩 공부는 평일 월·수·금, 주말은 클로드 공부, 화·목은 휴식으로 설정했습니다.", body_style),
    Spacer(1, 10),
    Paragraph("주간 학습 원칙", h2_style),
    Paragraph("• 코딩 공부: 월·수·금, 하루 2~4시간<br/>• 휴식: 화·목<br/>• 주말: 클로드 공부<br/>• 진도가 밀려도 주말로 몰아서 공부하지 않기<br/>• 공부일에는 개념·실습·문제·노트·커밋·푸시까지 마무리", body_style),
    Spacer(1, 10),
    Paragraph("주차별 학습 방향", h2_style),
    Paragraph("1~2주차: 딕셔너리 심화, 함수 기초<br/>3~4주차: 함수 심화, 파일 입출력, 예외 처리<br/>5~6주차: 작은 할 일 관리 프로그램 완성 및 정리<br/>7~8주차: 자료구조·알고리즘 기초, 스택·큐·해시<br/>9~10주차: 정렬·이분탐색, BFS·DFS 기초<br/>11~12주차: 웹·DB 기초, FastAPI 또는 Django, SQLite, SQLBolt<br/>13~14주차: 로컬 AI·RAG 기초, Ollama, PDF 추출, Chroma<br/>15~16주차: PDF 업로드·인증·DB·검색·근거 기반 로컬 RAG 앱<br/>17주차 이후: 운영체제·DB 핵심 개념·SQL 예습", body_style),
    Spacer(1, 12),
    Paragraph("날짜별 계획표", h2_style),
    table,
    Spacer(1, 10),
    Paragraph("이 계획은 현재 진도와 주 3일 코딩 공부 조건을 반영한 예시 계획입니다. 실제 진행 상황에 따라 주차별 목표는 조정할 수 있습니다.", small_style)
]

doc.build(story)

print("PDF 생성 완료")f