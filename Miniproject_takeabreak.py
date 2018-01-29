# This is a mini project that reminds you to take a break. I set it up to 10 seconds.
# Each 10 seconds a song will come up reminding oneself to take a break.
import time
import webbrowser
break_time = 3
break_count = 0

# The time the program will start and the music that will be played on.
print ("This program started on  "+time.ctime())
while (break_count < break_time):
       time.sleep(10)
       webbrowser.open("https://www.youtube.com/watch?v=rMltoD1jCGI")
       break_count = break_count + 1

