import streamlit as st
from experta import Fact, KnowledgeEngine, Rule, DefFacts, NOT, W, AND

from plants_parser import extract_values_from_json, raw_json_file

json_file_path = './plants.json'
rawPlantsFile = raw_json_file('./plants.json')
parsedFile = extract_values_from_json(json_file_path)

# Access the values from the result dictionary
CLIMATE_VALUES = parsedFile["CLIMATE_VALUES"]
SOIL_VALUES = parsedFile["SOIL_VALUES"]
SUNLIGHT_VALUES = parsedFile["SUNLIGHT_VALUES"]
WATER_VALUES = parsedFile["WATER_VALUES"]
PLANT_TYPE_VALUES = parsedFile["PLANT_TYPE_VALUES"]
SEASON_VALUES = parsedFile["SEASON_VALUES"]
WIND_VALUES = parsedFile["WIND_VALUES"]
PLANT_VALUES = parsedFile["PLANT_VALUES"]


class Climate(Fact):
    pass


class Soil(Fact):
    pass


class Sunlight(Fact):
    pass


class Plant(Fact):
    pass


class Water(Fact):
    pass


class PlantType(Fact):
    pass


class Season(Fact):
    pass


class Wind(Fact):
    pass




class PlantExpertSystem(KnowledgeEngine):

    @DefFacts()
    def _initial_action(self):
        yield Fact(action="findPlants")


    @Rule(
        AND(Fact(action="findPlants"),Fact(climate=W()), Fact(soil=W()), Fact(sunlight=W()), Fact(water=W()),
            Fact(plant_type=W()), Fact(season=W()), Fact(wind=W())))
    def rule_find_suitable_plants(self):
        suitable_plants = []
        facts = self.facts
        climate = facts[2]['climate']
        soil = facts[3]['soil']
        sunlight = facts[4]['sunlight']
        water = facts[5]['water']
        plant_type = facts[6]['plant_type']
        season = facts[7]['season']
        wind = facts[8]['wind']

        plant_data = rawPlantsFile

        for plantObject in plant_data:

            climateCondition =  climate.lower() in [value.lower() for value in plantObject['Climate']]
            soilCondition = soil.lower() in [value.lower() for value in plantObject['Soil']]
            sunlightCondition = sunlight.lower() in [value.lower() for value in  plantObject['Sunlight']]
            waterCondition = water.lower() in [value.lower() for value in plantObject['Water']]
            plantTypeCondition = plant_type.lower() in [value.lower() for value in plantObject['PlantType']]
            seasonCondition = season.lower() in [value.lower() for value in  plantObject['Season']]
            windCondition = wind.lower() in [value.lower() for value in  plantObject['Wind']]
            if (climateCondition and soilCondition and sunlightCondition and waterCondition and plantTypeCondition and seasonCondition and windCondition):
                suitable_plants.append(plantObject)

        print("suitable plants", suitable_plants)

        # Display the result in the Streamlit interface
        s = ''

        for i in [plant['Plant'] for plant in suitable_plants]:
            s += "- " + i + "\n"

        st.markdown(s)
        self.declare(Fact(suitable_plants=suitable_plants))


# Streamlit app
st.title("Plant Expert System")

st.write("Hi! I am Mr. Expert.\n\nI will help you determine the best plants to plant based on your criteria.")
# Instantiate the expert system
expert_system = PlantExpertSystem()
# Run the expert system

# Create a form to get user input
submitted = False
with st.form("plant_form"):
    st.write("Hi! I am Mr. Expert.\n\nI will help you determine the best plants to plant based on your criteria.")

    # Add form components for user input
    user_climate = st.selectbox("What is your climate preference?", CLIMATE_VALUES, index=1)

    user_soil = st.selectbox("What type of soil do you have?", SOIL_VALUES, index=1)

    user_sunlight = st.selectbox("What is the sunlight exposure in your area?", SUNLIGHT_VALUES, index=0)

    user_water = st.selectbox("How often do you water your plants?", WATER_VALUES, index=1)

    user_plant_type = st.selectbox("What type of plants are you interested in?", PLANT_TYPE_VALUES, index=1)

    user_season = st.selectbox("Which season are you planting for?", SEASON_VALUES, index=1)

    user_wind = st.selectbox("What is the wind condition in your area?", WIND_VALUES, index=1)

    # Submit button
    submitted = st.form_submit_button("Get Plant Suggestions")

if submitted:
    expert_system.reset()
    expert_system.declare(Fact(climate=user_climate.strip().capitalize()))
    expert_system.declare(Fact(soil=user_soil.strip().capitalize()))
    expert_system.declare(Fact(sunlight=user_sunlight.strip().capitalize()))
    expert_system.declare(Fact(water=user_water.strip().capitalize()))
    expert_system.declare(Fact(plant_type=user_plant_type.strip().capitalize()))
    expert_system.declare(Fact(season=user_season.strip().capitalize()))
    expert_system.declare(Fact(wind=user_wind.strip().capitalize()))
    print("Your plant")
    expert_system.run()
