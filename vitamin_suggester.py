def recommend_supplements(user_id, test_results, age, gender, medications, illnesses, pregnant, lifestyle):
    recommendations = {
        'High Need': [],
        'Moderate Need': [],
        'Low Need': [],
        'No Need': []
    }

    # Base nutrient details
    nutrient_details = {
        'Vitamin D': {'base_dosage': 800, 'unit': 'IU'},
        'Calcium': {'base_dosage': 500, 'unit': 'mg'},
        'Magnesium': {'base_dosage': 350, 'unit': 'mg'},
        'Vitamin A': {'base_dosage': 700, 'unit': 'mcg'},
        'Vitamin C': {'base_dosage': 75, 'unit': 'mg'},
        'Iron': {'base_dosage': 18, 'unit': 'mg', 'pregnant_dosage': 27},
        'Folate': {'base_dosage': 400, 'unit': 'mcg', 'pregnant_dosage': 600}
    }

    # Age and gender adjustments
    age_gender_adjustments = {
        ('female', 'teen'): {'Iron': 15, 'Folate': 400},
        ('female', 'adult'): {'Iron': 18, 'Calcium': 1000},
        ('female', 'senior'): {'Vitamin D': 1200, 'Calcium': 1200},
        ('male', 'teen'): {'Iron': 11},
        ('male', 'adult'): {'Iron': 8},
        ('male', 'senior'): {'Vitamin D': 1200}
    }

    # Lifestyle-specific adjustments
    lifestyle_adjustments = {
        'athlete': {'Vitamin D': 1000, 'Iron': 25, 'Magnesium': 400},
        'non-athlete': {'Vitamin D': 800, 'Iron': 18, 'Magnesium': 300}
    }

    # Illness-specific adjustments
    illness_adjustments = {
        'osteoporosis': {'Calcium': 1200, 'Vitamin D': 1200},
        'anemia': {'Iron': 50},
        'diabetes': {'Magnesium': 400, 'Vitamin D': 1000},
        'hypertension': {'Magnesium': 500, 'Calcium': 1000},
        'chronic kidney disease': {'Vitamin D': 1000, 'Calcium': 1200, 'Iron': 20},
        'heart disease': {'Omega-3': 1000, 'Magnesium': 400},
        'thyroid disorder': {'Iodine': 150, 'Selenium': 200},
        'depression': {'Vitamin D': 1000, 'Omega-3': 1000, 'Magnesium': 400},
        # Add more illnesses and their adjustments here
    }

    # Medication-specific adjustments
    medication_adjustments = {
        'blood_thinners': {'Vitamin K': 0},
        'antibiotics': {'Probiotics': 10},
        'diuretics': {'Potassium': 4700, 'Magnesium': 400},
        'statins': {'CoQ10': 100},
        'antidepressants': {'Folate': 600, 'Vitamin B12': 1000},
        'oral_contraceptives': {'Vitamin B6': 2, 'Folate': 400, 'Magnesium': 400},
        'antacids': {'Magnesium': 500, 'Calcium': 1000},
        # Add more medications and their adjustments here
    }

    # Determine age group and apply adjustments
    age_group = 'senior' if age > 65 else 'adult' if age > 18 else 'teen'
    age_gender_key = (gender, age_group)
    general_adjustments = age_gender_adjustments.get(age_gender_key, {})

    # Apply lifestyle adjustments
    lifestyle_specific_adjustments = lifestyle_adjustments.get(lifestyle, {})

    # Apply illness adjustments
    illness_specific_adjustments = {}
    for illness in illnesses:
        if illness in illness_adjustments:
            illness_specific_adjustments.update(illness_adjustments[illness])

    # Apply medication adjustments
    medication_specific_adjustments = {}
    for medication in medications:
        if medication in medication_adjustments:
            medication_specific_adjustments.update(medication_adjustments[medication])

    # Finalize nutrient adjustments
    for nutrient, details in nutrient_details.items():
        adjusted_dosage = details['base_dosage']

        # Apply age and gender adjustments
        if nutrient in general_adjustments:
            adjusted_dosage = general_adjustments[nutrient]

        # Apply lifestyle adjustments
        if nutrient in lifestyle_specific_adjustments:
            adjusted_dosage = lifestyle_specific_adjustments[nutrient]

        # Apply illness adjustments
        if nutrient in illness_specific_adjustments:
            adjusted_dosage = illness_specific_adjustments[nutrient]

        # Apply medication adjustments
        if nutrient in medication_specific_adjustments:
            adjusted_dosage = medication_specific_adjustments[nutrient]

        # Adjust for pregnancy
        if pregnant and nutrient in ['Iron', 'Folate']:
            adjusted_dosage = details['pregnant_dosage']

        # Update the final dosage in the details
        details['final_dosage'] = f"{adjusted_dosage} {details['unit']}"
        details['frequency'] = 'daily'

    # Generate recommendations based on test results
    for nutrient, score in test_results.items():
        details = nutrient_details[nutrient]
        dosage = details.get('final_dosage', 'Check with healthcare provider')
        frequency = details.get('frequency', 'daily')

        if score <= 3:
            suggestion = f"Immediate supplementation needed. Take {dosage} {frequency}."
        elif score <= 6:
            suggestion = f"Supplementation recommended. Take {dosage} {frequency}."
        elif score <= 9:
            suggestion = f"Supplementation could be beneficial. Take {dosage} {frequency}"
        else:
            suggestion = "No supplementation necessary."

        recommendations['High Need' if score <= 3 else 'Moderate Need' if score <= 6 else 'Low Need' if score <= 9 else 'No Need'].append(f"{nutrient}: {suggestion}")

    return recommendations

# Example usage
user_id = 101
test_results = {'Vitamin D': 5, 'Calcium': 3, 'Magnesium': 8, 'Vitamin A': 9, 'Vitamin C': 10, 'Iron': 2, 'Folate': 1}
age = 65
gender = 'male'
medications = ['blood_thinners', 'statins']
illnesses = ['anemia', 'heart disease']
pregnant = False
lifestyle = 'non-athlete'

recommendations = recommend_supplements(user_id, test_results, age, gender, medications, illnesses, pregnant, lifestyle)
for key, value in recommendations.items():
    if value:  # Only print categories with entries
        print(f"{key}:")
        for recommendation in value:
            print(f"  - {recommendation}")
            
            
            

                  