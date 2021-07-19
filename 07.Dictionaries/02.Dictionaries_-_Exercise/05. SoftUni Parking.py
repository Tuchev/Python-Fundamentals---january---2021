n = int(input())

registered_users = {}

for _ in range(n):
    data = input().split()
    command = data[0]
    user = data[1]
    if len(data) > 2:
        license_plate = data[2]
    if command == "register":
        if user not in registered_users:
            registered_users[user] = license_plate
            print(f"{user} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif command == "unregister":
        if user in registered_users:
            registered_users.pop(user)
            print(f"{user} unregistered successfully")
        else:
            print(f"ERROR: user {user} not found")
for user, license_plate in registered_users.items():
    print(f"{user} => {license_plate}")