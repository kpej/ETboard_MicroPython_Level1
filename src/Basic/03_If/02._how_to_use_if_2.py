# ******************************************************************************************
# FileName     : 02._how_to_use_if_2
# Description  : if 조건문 알아보기_2
# Description  : data의 값이 50보다 크면 쉘에 "data의 값은 50보다 큽니다." 출력해 보기
# Author       : 오경석
# Created Date : 2023.11.02
# Reference    :
# Modified     : 2024.03.13 : PEJ : 변수명, 파일명, 주석 수정
# Modified     : 2024.03.26 : PEJ : 코드 구조 변경(setup, loop)
# Modified     : 2024.04.04 : PEJ : 아두이노와 동일하게 코드 변경(100 => 50)
# ******************************************************************************************


# import
import time                                     # 시간 관련 라이브러리


# global variable
data = 51                                       # data 변수에 51 저장


# setup
def setup():
    pass                                        # 아무것도 하지 않고 건너뜀


# main loop
def loop():
    if data > 50:                               # data의 값이 50보다 크다면
        print("data의 값은 50보다 큽니다.")     # 쉘에 "data의 값은 50보다 큽니다." 출력

    time.sleep(1)                               # 1초간 대기


# start point
if __name__ == "__main__":
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
