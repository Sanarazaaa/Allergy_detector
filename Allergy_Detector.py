import streamlit as st
import os

class AllergyChecker:
    def __init__(self):
        self.allergen_mapping = {
            'peanut butter': ['peanuts'],
            'milk': ['dairy'],
            'shrimp': ['shellfish'],
            'bread': ['gluten'],
            'cheese': ['dairy'],
            'soy sauce': ['soy'],
            'egg salad': ['eggs'],
            'almond milk': ['almonds'],
            'soy milk': ['soy'],
            'wheat bread': ['gluten'],
            'yogurt': ['dairy'],
            'salmon': ['fish'],
            'chocolate': ['dairy', 'nuts'],
            'hummus': ['chickpeas'],
            'coconut milk': ['coconut'],
            'tofu': ['soy'],
            'salsa': ['tomato', 'onion'],
            'butter': []
        }
        self.user_profile = {}

    def set_allergies(self, username, allergies):
        self.user_profile[username] = [allergy.strip().lower() for allergy in allergies.split(',')]
        return f"Allergy profile updated for {username}."

    def predict_ingredients(self):
        return list(self.allergen_mapping.keys())

    def check_allergy(self, username):
        detected_ingredients = self.predict_ingredients()
        user_allergies = self.user_profile.get(username, [])

        matched_allergens = []
        for ingredient in detected_ingredients:
            if ingredient in self.allergen_mapping:
                allergens = self.allergen_mapping[ingredient]
                if any(allergen in user_allergies for allergen in allergens):
                    matched_allergens.append(ingredient)

        if matched_allergens:
            ingredients_list = "<br>".join(['🚫 ' + ingredient for ingredient in matched_allergens])
            result_text = (f"<strong style='color: red;'>This food is dangerous!</strong><br><br>"
                           f"Oh, honey, put that fork down!<br><br>"
                           f"You don’t want to play with fire, do you?<br><br>"
                           f"That could make you <strong>seriously ill</strong>! 😱<br><br>"
                           f"Let’s spill the tea on what’s in that dish:<br>{ingredients_list}<br><br>"
                           f"And listen up! You absolutely *have* to steer clear of these party crashers! 🥳")
            sound_file = "alert_sound.mp3"  # Path to the alert sound file
        else:
            ingredients_list = "<br>".join([f"✓ {ingredient}" for ingredient in detected_ingredients])
            result_text = (f"<strong>🟢 Safe to Eat!</strong><br><br>"
                           f"<strong>Detected Ingredients:</strong><br>{ingredients_list}<br><br>"
                           f"This food is good for you! 😊<br><br>"
                           f"Now go ahead and feast, darling! ✨")
            sound_file = "safe_sound.mp3"  # Path to the safe sound file

        return result_text, sound_file

# Instantiate the AllergyChecker
allergy_checker = AllergyChecker()

# Streamlit Application
st.title("User Allergy Profile Setup and Allergy Checker with Sound Alerts")

# Setup Profile Tab
st.header("Setup Profile")
username_input = st.text_input("Enter Username")
allergies_input = st.text_input("Enter Allergies (comma-separated)", placeholder="e.g., peanuts, dairy")
if st.button("Set/Update Allergy Profile"):
    profile_update_status = allergy_checker.set_allergies(username_input, allergies_input)
    st.success(profile_update_status)

# Check Food Allergies Tab
st.header("Check Food Allergies")
username_input_check = st.text_input("Enter Username for Allergy Check")
food_image = st.file_uploader("Upload an image of the food", type=['jpg', 'jpeg', 'png'])
if st.button("Check Allergy"):
    if food_image is not None:
        text, sound_file = allergy_checker.check_allergy(username_input_check)
        st.markdown(text, unsafe_allow_html=True)

        # Check if sound file exists before attempting to play it
        if os.path.exists(sound_file):
            st.audio(sound_file)  # Play the appropriate sound file
        else:
            st.warning(f"Sound file '{sound_file}' not found.")
    else:
        st.warning("Please upload an image of the food.")
