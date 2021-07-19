number_snowballs = int(input())
max_snowball_value = 0
best_snowball_snow = 0
best_snowball_time = 0
best_snowball_quality = 0

for snowball in range(number_snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball = (snowball_snow / snowball_time) ** snowball_quality
    if snowball > max_snowball_value:
        max_snowball_value = snowball
        best_snowball_snow = snowball_snow
        best_snowball_time = snowball_time
        best_snowball_quality = snowball_quality
print(f"{best_snowball_snow} : {best_snowball_time} = {int(max_snowball_value)} ({best_snowball_quality})")
