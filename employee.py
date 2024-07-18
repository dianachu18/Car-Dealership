class Employee:
    def __init__(self, name):
        self.cars_sold = 0
        self.revenue_generated = 0
        self.position = ''
        self.name = name

    def set_position(self, position_name):
        self.position = position_name

    def get_position(self):
        return self.position
    
    def increment_cars_sold(self):
        self.cars_sold += 1

    def get_cars_sold(self):
        return self.cars_sold
    
    def get_revenue_generated(self):
        return self.revenue_generated
    
    def generate_revenue(self, amount):
        self.revenue_generated += amount

def main():
    employee1 = Employee("John")
    employee1.set_position('Salesman')
    for i in range(3):
        employee1.increment_cars_sold()
        employee1.generate_revenue(25000)
    print(f"Employee name: John, Position: {employee1.get_position()}, Cars sold: {employee1.get_cars_sold()}, Revenue generated: {employee1.get_revenue_generated()}")

if __name__ == "__main__":
    main()

    