#!/usr/bin/env python3   

#리스트부터 이어짐.

#리스트를 만들기 위해 대괄호를 사용한다.
#len()함수를 통해 리스트 내 원소의 수를 센다.
#max()함수와 min()함수는 최대/최소값을 찾는다.
#count()함수는 리스트 내 특정 값이 등장한 횟수를 센다.
a_list = [1, 2, 3]
print("Output #58 : {}".format(a_list))
print("Output #59 : a_list has {} elements.".format(len(a_list)))
print("Output #60 : the maximum value in a_list is {}".format(max(a_list)))
print("Output #61 : the minimum value in a_list is {}".format(min(a_list)))
another_list= ['printer', 5, ['star', 'circle', 9]]
print("Output #62 : {}".format(another_list))
print("Output #63 : another_list also has {} elements.".format(len(another_list)))
print("Output #64 : 5 is in another_list {} time.".format(another_list.count(5)))

#리스트 분할을 사용하여 리스트 원스들의 부분집합 만들기
#맨 앞부터 분할하는 경우, 최초 인덱스를 생략한다. 
#맨 뒤까지 리스트를 분할하는 경우, 마지막 인덱스는 생략한다. 
print("Output #73 : {}".format(a_list[0:2]))
print("Output #74 : {}".format(another_list[:2]))
print("Output #75 : {}".format(another_list[1:]))

#[:]를 이용하여 리스트 복사하기
a_new_list = a_list[:]
print("Output #77 : {}".format(a_new_list))


     
