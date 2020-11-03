Trips_Since_Maintenance = []


class Vehicle:
    def __init__(self, make, model, year, weight):
        self.Make = make
        self.Model = model
        self.Year = year
        self.Weight = weight
        self.NeedMaintenance = False
        self.TripsSinceMaintenance = 0

    def getMake(self):
        return self.Make

    def getModel(self):
        return self.Model

    def getYear(self):
        return self.Year

    def getWeight(self):
        return self.Weight

    def getNeedMaintenance(self):
        return self.NeedMaintenance

    def getTripsSinceMaintenance(self):
        return self.TripsSinceMaintenance

    def setMake(self, make):
        self.Make = make

    def setModel(self, model):
        self.Model = model

    def setYear(self, year):
        self.Year = year

    def setWeight(self, weight):
        self.Weight = weight

    def setTripsSinceMaintenance(self,count=0):
        self.TripsSinceMaintenance = count

        for i in range(len(Trips_Since_Maintenance)):
            try:
                if Trips_Since_Maintenance[0 + i] == True and Trips_Since_Maintenance[1 + i] == False:
                    self.TripsSinceMaintenance += 1

                else:
                    self.TripsSinceMaintenance += 0


            except IndexError:
                break

        if self.getTripsSinceMaintenance() == 100:
            self.NeedMaintenance = True







    def Repair(self):
        if self.NeedMaintenance:
            self.TripsSinceMaintenance = 0
            self.NeedMaintenance = False
            Trips_Since_Maintenance.clear()


class Cars(Vehicle):
    def __init__(self, make, model, year, weight, isDriving=True, ):
        self.__isDriving = isDriving

        Vehicle.__init__(self, make, model, year, weight)

    def Drive(self, isDriving=True):
        self.__isDriving = isDriving
        return Trips_Since_Maintenance.append(isDriving), self.setTripsSinceMaintenance(+1)

    def Stop(self, isDriving=False):
        self.__isDriving = isDriving

        return Trips_Since_Maintenance.append(isDriving), self.setTripsSinceMaintenance(+0)

class Planes(Vehicle):
        def __init__(self, make, model, year, weight, isFlying=True, ):
            self.__isFlying = isFlying

            Vehicle.__init__(self, make, model, year, weight)

        def Flying(self, isFlying=True):
            self.__isFlying = isFlying
            return Trips_Since_Maintenance.append(isFlying), self.setTripsSinceMaintenance(+1)

        def Landing(self, isLanding=False):
            self.__isFlying = isLanding

            return Trips_Since_Maintenance.append(isLanding), self.setTripsSinceMaintenance(+0)

car1 = Cars("Nissan Motor Company, Ltd.", "Nissan Versa S", 2020, "2466 lbs")
car2 = Cars("General Motors Company, Ltd.", "Chevrolet Spark LS", 2020, "2278 lbs")
car3 = Cars("Kia Motors Corporation", "Kia Soul", 2020, "2,945 lbs")
for i in range(100):
    car1.Drive()
    car1.Stop()

for i in range(25):
    car2.Drive()
    car2.Stop()

for i in range(25):
    car3.Drive()
    car3.Stop()

desg = "--" * len(car1.getMake())

print(f'{desg}\nMaker: {car1.getMake()}\nName: {car1.getModel()}\nYear: {car1.getYear()}\nWeight: {car1.getWeight()}\nNo. of Trips: {car1.getTripsSinceMaintenance()}\n{desg}\n')

print(f'{desg}\nMaker: {car2.getMake()}\nName: {car2.getModel()}\nYear: {car2.getYear()}\nWeight: {car2.getWeight()}\nNo. of Trips: {car2.getTripsSinceMaintenance()-car1.getTripsSinceMaintenance()}\n{desg}\n')

print(f'{desg}\nMaker: {car3.getMake()}\nName: {car3.getModel()}\nYear: {car3.getYear()}\nWeight: {car3.getWeight()}\nNo. of Trips: {car3.getTripsSinceMaintenance()-car2.getTripsSinceMaintenance()}\n{desg}\n')


