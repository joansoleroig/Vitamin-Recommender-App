# BEAM - Vitamin Supplement Recommendation System
## Welcome to BEAM! This Streamlit app provides personalized vitamin supplement recommendations based on user-specific health parameters and test results.

### You can find the app up and running here: https://vitamin-recommender.streamlit.app/

## Features

User Input Parameters: Age, gender, pregnancy status, lifestyle, medications, illnesses, and test results.
Personalized Recommendations: Tailored vitamin supplement suggestions based on individual deficits.
Monthly Supplement Receipt: A detailed receipt with cost breakdown for the recommended supplements.
Easy Checkout: Autofilled shopping basket with a "Pay Now" button for convenience.

## How to Use

Install Requirements: Ensure you have Streamlit installed.
Run the App: Execute the app using the Streamlit command.
Input Parameters: Use the sidebar to enter your details, including:
Age
Gender
Pregnancy status
Lifestyle (athlete or non-athlete)
Medications
Illnesses
Test results for various vitamins (scale 1-10)
Get Recommendations: Click the "Get Recommendations" button to view personalized vitamin suggestions.
Review Receipt: Check your monthly supplement receipt and total cost.
Proceed to Payment: Click the "Pay Now" button to proceed with the purchase.

### Custom Styling

The app includes custom CSS for enhanced aesthetics:
Main Background: Light grey
Sidebar Background: Light blue-grey
Title: Centered, bold, black text
Recommendations and Receipt: White background, rounded corners, shadow effects
Info Message: Red background, white text, centered
Pay Button: Red background, white text, rounded corners, with hover effect
Code Structure
app.py: Contains the Streamlit app code.
vitamin_suggester.py: Contains the logic for generating vitamin supplement recommendations based on user inputs.
Example Usage

### Here's an example usage scenario for the app:

User enters the following details:
Age: 65
Gender: Male
Medications: Blood thinners, statins
Illnesses: Anemia, heart disease
Test results: Vitamin D (5), Calcium (3), Magnesium (8), Vitamin A (9), Vitamin C (10), Iron (2), Folate (1)
The app provides personalized recommendations based on these inputs, displayed in categorized sections (High Need, Moderate Need, Low Need, No Need).
The user can review the monthly supplement receipt, detailing the cost for each recommended supplement.
Finally, the user can click "Pay Now" to complete the purchase.

Enjoy using BEAM to manage your vitamin supplementation needs!
