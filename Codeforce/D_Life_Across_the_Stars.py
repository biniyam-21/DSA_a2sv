def find_max_population(n, people):
    max_year = 0
    max_alive = 0
    
    for year in range(1, 10**9 + 1):
        current_alive = 0
        for i in range(n):
            if people[i][0] <= year < people[i][1]:
                current_alive += 1
        if current_alive > max_alive:
            max_alive = current_alive
            max_year = year
    
    print(max_year, max_alive)

n = int(input())
people = []
for _ in range(n):
    b, d = map(int, input().split())
    people.append([b, d])

find_max_population(n, people)
