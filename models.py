from dataclasses import dataclass
from fasthtml.common import database

@dataclass
class Car:
    id:int
    description:str
    model: str
    make: str
    price: int
    
class House:
    id:int
    description:str
    number_of_rooms: int
    number_of_bathrooms: int
    price: int
    
class Job:
    id:int
    description:str
    company: str
    per_hour_wage: int


db = database('gregslist_db.db')
car_table = db.create(Car, pk='id')
house_table = db.create(House, pk='id')
job_table = db.create(Job, pk='id')

if __name__ == "__main__":
    car_table.insert(Car(description="new stuff", model="taurus", make="ford", price=1000))
    car_table.insert(Car(description="newer stuff", model="colorado", make="chevy", price=1000))