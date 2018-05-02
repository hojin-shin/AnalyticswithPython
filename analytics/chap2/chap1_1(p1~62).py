#!usr/bin/env python3
from math import exp, log, sqrt 
import re  #정규 표현식 같은 특정한 패턴을 찾아주는 모듈(regular expression)
from datetime import date, time, datetime, timedelta #날짜와 시간처리용 모듈

#문자 바꾸기
string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(" ","!@!")
print("Output #32 (with !@!): {0:s}".format(string5_replace))
string5_replace = string5.replace(" ",",")
print("Output #33 (with commas) : {0:s}".format(string5_replace))

# 대소문자 바꿈
string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #34 : {0:s}".format(string6.lower()))
print("OUtput #35 : {0:s}".format(string6.upper()))
string5 = "here's WHAT Happens WHEN you use Capitalize."
print("Output #36 : {0:s}".format(string5.capitalize()))
string5_list = string5.split()
print("Output #37 (on each word): ")
for word in string5_list:
    print("{0:s}".format(word.capitalize()))

# 문자열 내에 등장하는 패턴의 횟수를 세기
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"the", re.I)   # re.I : 패턴이 대/소문자 구분없이 해줌
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print("Output #38: {0:d}".format(count))

#문자열 내에서 발견된 패턴 출력하기
string= "The quick brown fox jumps over the laze dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)", re.I) #메타문자사용 (?P<이름>)
print("Output #39 : ")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))

#문자열 내 "a"를 'the"로 대체하기
string = "The quick brown fox jumps over the lazy dog."
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
print("Output #40 : {:s}".format(pattern.sub("a",string)))

# 오늘 날짜와 년, 월, 일 요소들을 출력하기
today = date.today()
print("Output #41 : today: {0!s}".format(today))
print("Output #42 : {0!s}".format(today.year))
print("Output #43 : {0!s}".format(today.month))
print("Output #44 : {0!s}".format(today.day))
current_datetime = datetime.today()
print("Output #45 : {0!s}".format(current_datetime))

#timedelta 함수를 이용하여 새로운 날짜 계산하기 
one_day = timedelta(days =-1)
yesterday = today + one_day
print("Output #46: yesterday : {0!s}".format(yesterday))
eight_hours = timedelta(hours =-8)
print("Output #47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))


#두 날짜 사이의 날짜 차이를 계산하기
date_diff= today -yesterday
print("Output #48 : {0!s}".format(date_diff))
print("Output #49 : {0!s}".format(str(date_diff).split()[0]))

#date 객체를 특정 형식의 문자열로 만들기
print("Output #50 :{:s}".format(today.strftime('%m/ %d/ %Y')))
print("Output #51 :{:s}".format(today.strftime('%b %d, %Y')))
print("Output #52 :{:s}".format(today.strftime('%Y-%m-%d')))
print("Output #53 :{:s}".format(today.strftime('%B %d, %Y')))


#날짜 문자열로부터 특정형식의 datetime 객체를 생성하기
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')
#다른 date형식을 지닌 4가지 문자열에 기반한 각각 2종류의 datetime 객체들과 date 객체들
print("Output #54 : {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("Output #55 : {!s}".format(datetime.strptime(date2, '%b %d, %Y')))
#날짜부분만 출력하기
print("Output #56 : {!s}".format(datetime.date(datetime.strptime(date3, '%Y-%m-%d'))))
print("Output #57 : {!s}".format(datetime.date(datetime.strptime(date4, '%B %d, %Y'))))













