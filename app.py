

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
from preprocessing.preprocess import preprocess
import joblib




app = FastAPI()
@app.get("/")
async def root():
    return {"alive"}

class Property(BaseModel): 
    Zip: int
    Living_area: float
    Number_of_rooms:float
    Garden_surface:float
    Terrace_surface: float
    Open_fire: float
    Surface_of_the_land: float
    Number_of_facades: float
    Swimming_pool:float
    Building_cond_values:float
    Kitchen_values:float
    Primary_energy_consumption:float
    Energy_efficiency:float
    

#item = jsonpickle.encode(Property)

model = joblib.load('random_forest_model.pkl')

#@app.post("/property_details")
#def create_property(item:Property): 
    #item = Property()
    #return item

@app.post("/predict_price")
def predict_price(Zip: int,
    Living_area: float,
    Number_of_rooms:float,
    Garden_surface:float,
    Terrace_surface: float,
    Open_fire: float,
    Surface_of_the_land: float,
    Number_of_facades: float,
    Swimming_pool:float,
    Building_cond_values:Literal['To restore',
        'To be done up',
        'Just renovated',
        'To renovate',
        'Good',
        'As new'],
    Kitchen_values:Literal['Not installed',
        'Installed',
        'Semi equipped',
        'Hyper equipped',
        'USA uninstalled',
        'USA installed',
        'USA semi equipped',
        'USA hyper equipped'],
    Primary_energy_consumption:float,
    ):
    
    data = {
    "Zip": Zip,
    "Living_area":Living_area,
    "Number_of_rooms":Number_of_rooms,
    "Garden_surface":Garden_surface,
    "Terrace_surface": Terrace_surface,
    "Open_fire":Open_fire,
    "Surface_of_the_land":Surface_of_the_land,
    "Number_of_facades": Number_of_facades,
    "Swimming_pool":Swimming_pool,
    "Building_cond_values":Building_cond_values,
    "Kitchen_values": Kitchen_values,
    "Primary_energy_consumption":Primary_energy_consumption}

    preprocessed_data = preprocess(data)
    prediction = model.predict(preprocessed_data)[0]
    result = {"prediction": prediction}
    return result