class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("accelerating..."
        "\nacceleratel funcanality here")
    def change_gear(self, gear_type):
        print("gear changed"
        "gear related funcanality here")
audi = Car("A6", "red", "audi", 80)
print(audi.accelerate())
