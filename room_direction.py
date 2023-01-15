a,b = map(int, input().split())
c,d = map(int, input().split())

room_key = a-c
room_number = b -d 
print(room_key)
print(room_number)

# if room_key > 0:
#     print("N: %d"%room_key)
# elif room_key < 0:
#     print("S: %d"%room_key)

# if room_number > 0:
#     print("W: %d"%room_number)
# elif room_number < 0:
#     print("E: %d"%room_number)

a = "north" * -*room_key