import time
from config import MACHINE_SEC

class Timer:   
    def start(self, option):
        min_scheduled = int(input(f"Enter the {option} time...\n"))
        self.timer_seconds = min_scheduled * MACHINE_SEC
        print(f"This timer will work for {self.timer_seconds} seconds or {min_scheduled} mins")
        self.future_time = time.time() + self.timer_seconds

    def check_complete(self):
        if time.time() > self.future_time:
            self.alarm()
            return True
    
    def alarm(self):
        print("Done!!!")
        