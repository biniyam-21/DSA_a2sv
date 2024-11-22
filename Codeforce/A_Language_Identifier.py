def identify_language():
    t = int(input().strip())
    sent = [input().strip() for _ in range(t)]
    for s in sent:
        # length = len(s)
        if s[-2:] == "po":
            print("FILIPINO")
        elif s[-4:] == "desu" or s[-4:] == "masu":
            print("JAPANESE")
        elif s[-5:] == "mnida":
            print("KOREAN")


identify_language()



# def identify_language():
#     t = int(input().strip())
#     sent = [input().strip() for _ in range(t)]
#     for s in sent:
#         length = len(s)
#         if length >= 2 and s[-2:] == "po":
#             print("FILIPINO")
#         elif length >= 4 and (s[-4:] == "desu" or s[-4:] == "masu"):
#             print("JAPANESE")
#         elif length >= 5 and s[-5:] == "mnida":
#             print("KOREAN")


# identify_language()

