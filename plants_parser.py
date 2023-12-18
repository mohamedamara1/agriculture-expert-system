import json


def raw_json_file(json_file_path):
    # Open the JSON file and load its content
    with open(json_file_path, 'r') as file:
        plants = json.load(file)
    return plants


def extract_values_from_json(json_file_path):
    # Open the JSON file and load its content
    with open(json_file_path, 'r') as file:
        plants = json.load(file)

    # Extract unique values for each category
    climate_values = set()
    soil_values = set()
    sunlight_values = set()
    water_values = set()
    plant_type_values = set()
    season_values = set()
    wind_values = set()
    plant_values = set()

    for obj in plants:
        climate_values.update(obj["Climate"])
        soil_values.update(obj["Soil"])
        sunlight_values.update(obj["Sunlight"])
        water_values.update(obj["Water"])
        plant_type_values.update(obj["PlantType"])
        season_values.update(obj["Season"])
        wind_values.update(obj["Wind"])
        plant_values.add(obj["Plant"])

    # Convert sets to sorted lists
    CLIMATE_VALUES = sorted(list(climate_values))
    SOIL_VALUES = sorted(list(soil_values))
    SUNLIGHT_VALUES = sorted(list(sunlight_values))
    WATER_VALUES = sorted(list(water_values))
    PLANT_TYPE_VALUES = sorted(list(plant_type_values))
    SEASON_VALUES = sorted(list(season_values))
    WIND_VALUES = sorted(list(wind_values))
    PLANT_VALUES = sorted(list(plant_values))

    # Create and return a dictionary
    result_dict = {
        "CLIMATE_VALUES": CLIMATE_VALUES,
        "SOIL_VALUES": SOIL_VALUES,
        "SUNLIGHT_VALUES": SUNLIGHT_VALUES,
        "WATER_VALUES": WATER_VALUES,
        "PLANT_TYPE_VALUES": PLANT_TYPE_VALUES,
        "SEASON_VALUES": SEASON_VALUES,
        "WIND_VALUES": WIND_VALUES,
        "PLANT_VALUES": PLANT_VALUES
    }

    return result_dict


# Example usage
json_file_path = './plants.json'
result = extract_values_from_json(json_file_path)
