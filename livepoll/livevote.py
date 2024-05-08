import os
import gspread
import time
import json
from modules.advanceprint import *

os.system('')

# 서비스용 API 계정을 만들어야 API를 사용할 수 있는데, 그 때 서비스 계정이 접근할 수 있게 하는 키를 받아야 합니다.
with open(r'C:\Users\p0109\Desktop\민권\학교\학생회\밤절제\실시간 투표\liveovte-5272b89c70a7.json') as f:
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

        #개인파트
        count_에코 = votes_column_c.count('에코(밴드부) 그대에게')
        count_학생회 = votes_column_c.count('학생회 이게무슨일이야')
        count_TOP = votes_column_c.count('T.O.P(댄스부) Centuries')
        count_황승태 = votes_column_c.count('황승태')
        count_김규은외6명 = votes_column_c.count('김규은 외 6명')
        count_김영우 = votes_column_c.count('김영우')
        count_손솔빈외1명 = votes_column_c.count('손솔빈 외 1명')
        count_조예원외1명 = votes_column_c.count('조예원 외 1명')
        count_유경민외1명 = votes_column_c.count('유경민 외 1명')
        count_BAC = votes_column_c.count('BAC(연극부)')

        count_14 = votes_column_d.count('1-4 (이지환 외 11명) 사랑')
        count_18 = votes_column_d.count('1-8 (이승재 외 17명) 은근히 낯가려요')
        count_25 = votes_column_d.count('2-5 잘자요 아가씨')
        count_210 = votes_column_d.count('2-10 풍선')
        count_28 = votes_column_d.count('2-8 젠틀맨')
        count_26 = votes_column_d.count('2-6 아브라카타브라')
        count_12 = votes_column_d.count('1-2 (박윤주 외 23명) 나팔바지')
        count_23 = votes_column_d.count('2-3 위아래')
        count_24 = votes_column_d.count('2-4 Mr.chu')
        count_21 = votes_column_d.count('2-1 Love shot')
        count_29 = votes_column_d.count('2-9 Magnetic')
        count_27 = votes_column_d.count('2-7 텐미닛')
        count_22 = votes_column_d.count('2-2 우아하게')

        # 결과 출력
        result_str = (
            "황승태: " + str(count_황승태) +
            ", 김규은 외 6명: " + str(count_김규은외6명) +
            ", 김영우: " + str(count_김영우) +
            ", 손솔빈 외 1명: " + str(count_손솔빈외1명) +
            ", 조예원 외 1명: " + str(count_조예원외1명) +
            ", 유경민 외 1명: " + str(count_유경민외1명) +
            ", 에코: " + str(count_에코) +
            ", 학생회: " + str(count_학생회) +
            ", TOP: " + str(count_TOP) +
            ", 1-4 (이지환 외 11명) 사랑: " + str(count_14) +
            ", 1-8 (이승재 외 17명) 은근히 낯가려요: " + str(count_18) +
            ", 2-5 잘자요 아가씨: " + str(count_25) +
            ", 2-10 풍선: " + str(count_210) +
            ", 2-8 젠틀맨: " + str(count_28) +
            ", 2-6 아브라카타브라: " + str(count_26) +
            ", 1-2 (박윤주 외 23명) 나팔바지: " + str(count_12) +
            ", 2-3 위아래: " + str(count_23) +
            ", 2-4 Mr.chu: " + str(count_24) +
            ", 2-1 Love shot: " + str(count_21) +
            ", BAC(연극부): " + str(count_BAC) +
            ", 2-9 Magnetic: " + str(count_29) +
            ", 2-7 텐미닛: " + str(count_27) +
            ", 2-2 우아하게: " + str(count_22)
        )
        log_print('진행', result_str, 'blue', sliceprint=False)
        print(result_str)
        
        time.sleep(5)

def menu():
    log_print('+', 'LIVEVOTE V2', 'green', sliceprint=False)
    log_print('+', 'MADE BY HOSEO HIGHSCHOOL STUDENTS COUNCIL', 'green', sliceprint=False)
    print('')
    log_print('알림', 'Enter키를 누르면 실시간 집계를 시작합니다.', 'yellow', sliceprint=False)
    input("[PRESS ENTER]")
    livevote()
menu()

#2024호서고등학교 학생회 기술행정부 차장 조민권, 준학생회 오승제 // 2024 05 08