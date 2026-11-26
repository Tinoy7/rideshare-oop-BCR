class DriverAccount:
    def __init__(self, name, vehicle_plate):
        self.name = name
        self.vehicle_plate = vehicle_plate
        self.__rating = 5.0
        self.__total_trips = 0
  
    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.__total_trips += 1
            self.__rating = ((self.__rating * (self.__total_trips - 1)) + rating) / self.__total_trips
        else:
            raise ValueError("Invalid Rating! Rating must be between 1.0 and 5.0.")
        
    @property  
    def get_rating(self):
        return self.__rating
