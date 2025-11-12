import time
import winsound

frequency = 432
duration = 2000

userTime = int(input("For how long you would like to set the timer: "))

for i in range(userTime, 0, -1):
    seconds = i % 60
    minutes = int( i / 60) % 60
    hours = int(i / 3600) % 24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("\nTIME'S UP!!!")
winsound.Beep(frequency, duration)



