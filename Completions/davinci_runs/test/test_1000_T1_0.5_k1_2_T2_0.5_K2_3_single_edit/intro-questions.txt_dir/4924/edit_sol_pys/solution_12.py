
#-----main-----

current_time = input()
explosion_time = input()

current_hour, current_minute, current_second = map(int,current_time.split(":"))
explosion_hour, explosion_minute, explosion_second = map(int,explosion_time.split(":"))

if explosion_hour<current_hour:
    explosion_hour+=24

if explosion_hour==current_hour and explosion_minute<current_minute:
    explosion_hour+=24

if explosion_hour==current_hour and explosion_minute==current_minute and explosion_second<current_second:
    explosion_hour+=24

explosion_hour-=current_hour
explosion_minute-=current_minute
explosion_second-=current_second

if explosion_second<0:
    explosion_second+=60
    explosion_minute-=1

if explosion_minute<0:
    explosion_minute+=60
    explosion_hour-=1

print(str(explosion_hour)+":"+str(explosion_minute)+":"+str(explosion_second))
