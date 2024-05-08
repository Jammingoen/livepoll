import os
import gspread
import time
import json
from modules.advanceprint import *

os.system('')

# 서비스용 API 계정을 만들어야 API를 사용할 수 있는데, 그 때 서비스 계정이 접근할 수 있게 하는 키를 받아야 합니다.
with open(r"C:\Users\p0109\Desktop\민권\학교\학생회\밤절제\livepoll\liveovte-5272b89c70a7.json") as f:
    credentials = json.load(f)

# credentials에 넣은 키 내용을 바탕으로 객체를 생성합니다.
gc = gspread.service_account_from_dict(credentials)

# 실시간 집계하는 함수
def livevote():
    while True:
        sp = gc.open('밤절제 인기투표')
        # C열 데이터 가져오기
        votes_column_c = sp.sheet1.col_values(3)
        # D열 데이터 가져오기
        votes_column_d = sp.sheet1.col_values(4)

        # 후보들의 투표 수 집계
        candidates_c = [
            "에코(밴드부) 그대에게",
            "학생회 이게무슨일이야",
            "T.O.P(댄스부) Centuries",
            "황승태",
            "김규은 외 6명",
            "김영우",
            "손솔빈 외 1명",
            "조예원 외 1명",
            "유경민 외 1명",
            "BAC(연극부)"
        ]
        candidates_d = [
            "1-4 (이지환 외 11명) 사랑",
            "1-8 (이승재 외 17명) 은근히 낯가려요",
            "2-5 잘자요 아가씨",
            "2-10 풍선",
            "2-8 젠틀맨",
            "2-6 아브라카타브라",
            "1-2 (박윤주 외 23명) 나팔바지",
            "2-3 위아래",
            "2-4 Mr.chu",
            "2-1 Love shot",
            "2-9 Magnetic",
            "2-7 텐미닛",
            "2-2 우아하게"
        ]

        count_c = {candidate: (votes_column_c.count(candidate) + votes_column_d.count(candidate)) for candidate in candidates_c}
        count_d = {candidate: (votes_column_c.count(candidate) + votes_column_d.count(candidate)) for candidate in candidates_d}

        # 득표수 기준으로 정렬
        sorted_count_c = sorted(count_c.items(), key=lambda x: x[1], reverse=True)
        sorted_count_d = sorted(count_d.items(), key=lambda x: x[1], reverse=True)

        # E열에 쓸 데이터 준비
        result_c = [f"{rank}등: {candidate} - {count}" for rank, (candidate, count) in enumerate(sorted_count_c, start=1)]
        result_d = [f"{rank}등: {candidate} - {count}" for rank, (candidate, count) in enumerate(sorted_count_d, start=1)]

        # E열에 쓰기
        cell_list = sp.sheet1.range('E1:E25')  # E열의 셀 범위 설정
        for i, data in enumerate(['C열 득표수 순위'] + result_c + ['D열 후보 득표수 순위'] + result_d):
            cell_list[i].value = data
        sp.sheet1.update_cells(cell_list)

       

# 메뉴 함수
def menu():
    log_print('+', 'LIVEVOTE V2', 'green', sliceprint=False)
    log_print('+', 'MADE BY HOSEO HIGHSCHOOL STUDENTS COUNCIL', 'green', sliceprint=False)
    print('')
    log_print('알림', 'Enter키를 누르면 실시간 집계를 시작합니다. 5초 간격으로 수행하며 이는 코드에서 수정할 수 있습니다.', 'yellow', sliceprint=False)
    input("[PRESS ENTER]")
    livevote()

menu()
