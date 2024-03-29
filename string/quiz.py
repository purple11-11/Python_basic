""" 
    Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.

    예) http://naver.com
    규칙1 : http:// 부분은 제외 => naver.com
    규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
    규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
                    (nav)               (5)             (1)         (!)
    => 생성된 비밀번호 : nav51!
 """

""" ------------------------------- 내 풀이 ------------------------------------- """
url = "http://naver.com"

dot = url.find('.')
password = url[7:dot] # naver
print(f"{password[:3]}{len(password)}{password.count('e')}!")

""" ------------------------------- 강사님 풀이 ---------------------------------- """

""" 

my_str = url.replace("http://", "") # 규칙 1
# print(my_str) # naver.com 

my_str = my_str[:my_str.index(".")]  # 규칙 2
# == my_str[0:5] -> 0 ~ 4 까지 출력
# print(my_str) # naver 

password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + "!"
print("{0}의 비밀번호는 {1}입니다." .format(url, password)) 

"""