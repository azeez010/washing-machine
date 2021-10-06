import sys, time
from timer import Timer

class WashingMachine:
    def __init__(self):
        self.options = ["wash", "spin", "drain"]
        self.selected = None

    def changeOption(self, option):
        if option in self.options:
            self.selected = option
        else:
            print("Option does not exist!")
            sys.exit(1)

    def wash(self):
        self.run()

    def drain(self):
        self.run()

    def spin(self):
        self.run(self.selected)
    
    def run(self):
        self.check_alarm()
        loop_on = True 
        while loop_on:
            print(f"{self.selected}!!")
            if self.timer.check_complete():
                loop_on = False
            time.sleep(5)

    def check_alarm(self):
        # Start the countdown
        self.timer = Timer()
        self.timer.start(self.selected)


    def control_center(self):
        if self.selected == "wash":
            self.wash()
             
        elif self.selected == "drain":
            self.drain()
        
        elif self.selected == "spin":
            self.spin() 
    