def ticket_both():
    # n, t = map(int, input().split())
    n = str(input())
    # t = int(input())
    t = int(n.split()[0])
    s = int(n.split()[1])
    count = s // t 
    if s % t != 0:
        count += 1
    print(count)
    # print(t)

ticket_both()
