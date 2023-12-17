import streamlit as st

class PlantExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            'climate': {'hot': ['Cactus', 'Succulents'], 'temperate': ['Rose', 'Lavender']},
            'soil': {'sandy': ['Cactus', 'Carrots'], 'clayey': ['Tulips', 'Tomatoes']},
            'sunlight': {'full_sun': ['Sunflower', 'Tomatoes'], 'shade': ['Fern', 'Hosta']},
        }

    def suggest_plants(self, input_data):
        suggestions = set()

        for factor, conditions in input_data.items():
            if factor in self.knowledge_base and conditions in self.knowledge_base[factor]:
                suggestions.update(self.knowledge_base[factor][conditions])

        return suggestions

# Instantiate the expert system
expert_system = PlantExpertSystem()

# Streamlit app
st.title("Plant Expert System")

# User input form
user_input = {}
user_input['climate'] = st.selectbox("Select Climate:", ['hot', 'temperate'])
user_input['soil'] = st.selectbox("Select Soil Type:", ['sandy', 'clayey'])
user_input['sunlight'] = st.selectbox("Select Sunlight Exposure:", ['full_sun', 'shade'])

# Suggest plants based on user input
if st.button("Get Plant Suggestions"):
    recommended_plants = expert_system.suggest_plants(user_input)
    st.success(f"Recommended plants: {', '.join(recommended_plants)}")
