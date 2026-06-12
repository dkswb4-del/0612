
user = {
“name” : “홍길동”,
“age” : 25,
“skills” : [“Python”, “Git”]
}

대괄호 사용 (가장 일반적)
print(user[“name”]) # 출력 : 홍길동

print(user[“name”], “은 나이가 ”, user[“age”], “먹었습니다.”)


mart = (
“apple” : 100
“banan” : 2500
“orange” : 1500
)
mart[“apple”] = 5000


print(mart.keys())
print(mart.values())
print(mart.items())


# items() : Key와 value를 쌍(튜플)으로 모아서 가져오기 (★가장 많이 씀)


for fruit, price in mart, items():
    print(f"{friut}의 가은 {price}원입니다.")

          
