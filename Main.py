import time
from datetime import datetime
import winsound  # Use playsound for non-Windows systems

# Function to play alarm sound
def play_alarm():
    frequency = 2500  # Set frequency (Hz)
    duration = 1000  # Set duration (milliseconds)
    winsound.Beep(frequency, duration)  # Windows only

# Get user input for alarm time
alarm_time = input("Enter alarm time (HH:MM:SS - 24hr format): ")
print(f"Alarm set for {alarm_time}. Waiting...")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("Wake up! ⏰")
        play_alarm()
        break
    time.sleep(1)  # Wait one second before checking again
