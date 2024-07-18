#== dealership.py ==#

class Dealership():
    def __init__():
        staff = []
        inventory = []
        revenue = 0
    
    def get_revenue(self):
        return self.revenue
    
    def sell_car(self, modelN, used, employee_who_sold):
        # find car
        for i in self.inventory:
            if i.model == modelN:
                break
        
        self.inventory.remove(i)

        employee_who_sold.increment_cars_sold()

        #== Still need to increase revenue, and increase staff revenue ===#
        print("incomplete")

    def add_car(self, modelN, used):
        #== am I suppose to create a new car object here? ==#
        print("incomplete")

    
        

