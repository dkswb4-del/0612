
# user = {
# "name": "홍길동",
# "age" : 25,
# "skills" : ["Python", "Git"]
# }

# # 대괄호 사용 (가장 일반적)
# print(user["name"]) # 출력 : 홍길동

# print(user["name"], "은 나이가 ", user["age"], "먹었습니다.")


# mart = {
# "apple" : 100,
# "banana" : 2500,
# "orange" : 1500
# }
# mart["apple"] = 5000


# print(mart.keys()) # 결과 list
# print(mart.values()) # 결과 list
# print(mart.items()) # 결과 튜플


# # items() : Key와 value를 쌍(튜플)으로 모아서 가져오기 (★가장 많이 씀)


# for fruit, price in mart, items():
#     print(f"{friut}의 가은 {price}원입니다.")

# for key in mart.keys():
#     print(f"mart 딕셔너리의 key는 {key}가 있습니다.")


# mart2 = {"apple" : 1000, "banana" : 2500,}


# print("apple" in mart2)  # True
# print("grape" in mart2)  # False

# my_tuple = (1, 2, 3)
# another_tuple = 10, 20, 30 # 소괄호 생략 가능
# # my_tuple[0] = 99 # 튜플은 변경 불가 (immutable)

# my_list = [1, 2, 3]
# my_list[0] = 99 # 리스트는 변경 가능 (mutable)
          
# # 리스트와 튜플의 결정적 차이 (!중요)
# # 리스트[] : 데이터 변경가능. 수정, 추가 , 삭제가 마음대로 가능
# # 튜플 () : 데이터 변경 불가능. 한번 생성된 튜플은 수정, 추가, 삭제가 불가능

# numbers = (1, 2, 3, 4, 5)
# print(numbers[1:4]) # (1, 2, 3) -> 인덱스 1부터 3까지

# a = (1, 2)
# b = (3, 4)

# print(a + b) # (1, 2, 3, 4) -> 튜플끼리 더하기
# print(a * 3) # (1, 2, 1, 2, 1, 2) -> 튜플 3번 반복하기

# # 1. 패킹
# info = ('tom', 20, 'seoul') 

# # 2. 언패킹 (튜플의 개수와 변수의 개수가 같아햐함)
# name, age, city = info

# print(name) # tom
# print(age)  # 20
# print(city) # seoul

 
x = 10
y = 20

# 두 값을 서로 바꾸기 (튜플 언패킹 원리)
x, y = y, x

# print(x) # 20
# print(y) # 10


# sample = (1, 2, 3, 42, 4, 2)
# print(sample.count(2)) 
# print(sample.index(3)) 

# 마음의 다짐을 함

# fruits = ["사과", "바나나", "수박"]
# for fruit in fruits:
#     print(fruit)

# for i in range(5):
#     print(f"{i}번째 반복 중입니다.") 

# total = 0
# for num in range(1, 11): # 1부터 10까지의 숫자
#     total = total + num # 기존 total에 num을 더해서 total에 다시 저장
# print(f"1부터 10까지의 합은 {total}")


for num in range(1, 11):
    if num % 2 !=0: # num이 홀수인 경우
        print(num)

