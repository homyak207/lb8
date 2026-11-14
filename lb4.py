a = [2,2,3,4,5,4]
print("Ручной счётчик")
for i in range(len(a)):
    print(i, a[i])
print("Через enumerate")
for k,v in enumerate(a):
    print(k, v)


name = ["Анна", "Борис", "Вера", "Глеб"]
count = [3, 2, 5, 4]

for n,c in zip(name,count):
    print(f"{n}: {c}")

print("Список циклом")
res = []
for i in range(100+1):
    if i % 2 == 0:
        res.append(i**2)

print(res)
print("Список генератором")
res1 = [i**2 for i in range(100+1) if i % 2 == 0]
print(res1)
print("Сравнение списков")
print(res == res1)


p = ["Клавиатура", "Мышь", "Монитор", "Кабель","Мышь"]
dictf = {}
for i in p:
    dictf[i] = len(i)
print("Словарь циклом")
print(dictf)

dictc = {i: len(i) for i in p}
print("Словрь генератором")
print(dictc)
    

students = [
    {"name": "Анна",  "score": 114, "attempts": 2},
    {"name": "Борис", "score": 50,  "attempts": 4},
    {"name": "Вера",  "score": 43,  "attempts": 7},
    {"name": "Глеб",  "score": 74,  "attempts": 3},
]
res1 = []
for i in students:
    if i["score"] >= 60 and i["attempts"] <= 3:
        res1.append(i["name"])    
res2 = [i["name"] for i in students if i["score"] >= 60 and i["attempts"] <= 3]

print("     Циклом:", res1)
print("Генератором:", res2)


import time

def f1(s):
    res = []
    start_time = time.time()
    for i in s:
        if i % 2 == 0:
            res.append(i**2)
    end_time = time.time()
    return end_time - start_time
            
def f2(s):
    start_time = time.time()
    res = [i**2 for i in s if i % 2 == 0]
    end_time = time.time()  
    return end_time - start_time

def mean(f,a, runs = 7):
    times = []
    for i in range(runs):
        times.append(f(a))
    return times, sum(times) / len(times)

for n in (10_000,100_000,1_000_000):
    s = list(range(n))
    sp1, mn1 = mean(f1,s)
    sp2, mn2 = mean(f2,s)
    print(sp1,"\n", mn1)
    print(sp2,"\n", mn2)
    

    




ticket_ids = [101, 102, 103, 104]
statuses = ["open", "closed", "open", "open"]
priorities = ["low", "high", "high", "medium"]

dictt = {x: y for x,y in zip(ticket_ids, statuses)}
print("Словарь номер → статус:", dictt)
open_high = [tid for tid, st, priot in zip(ticket_ids,statuses,priorities) if st == "open" and priot == "high"]
print("Открытые заявки высокого приоритета:", open_high)



