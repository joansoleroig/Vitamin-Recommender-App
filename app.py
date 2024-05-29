# streamlit_app.py

import streamlit as st
from vitamin_suggester import recommend_supplements

def main():
    st.set_page_config(page_title="BEAM", layout="wide")
    
    # Custom CSS to style the app
    st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background-color: #e0e4e8;
    }
    .title {
        font-size: 36px;
        color: #000000;
        font-weight: bold;
        text-align: center;
    }
    .recommendations {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
    }
    .receipt {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        border: 2px solid #ddd;
        position: relative; /* Add relative positioning */
    }
    .receipt-item {
        font-size: 16px;
        margin-bottom: 10px;
        padding: 5px;
        border-bottom: 1px solid #ddd;
        display: flex;
        justify-content: space-between;
    }
    .total {
        font-size: 18px;
        font-weight: bold;
        display: flex;
        justify-content: space-between;
    }
    .pay-button {
        text-align: center; /* Center the button horizontally */
        margin-top: 20px; /* Add some space above the button */
    }

    .pay-now-button {
        background-color: #ff4b4b; /* Same color as the popup */
        border: none;
        color: white;
        padding: 10px 20px; /* Adjust padding for a bigger button */
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px; /* Increase font size */
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        transition: background-color 0.3s ease; /* Add transition for a smoother hover effect */
    }

    .pay-now-button:hover {
        background-color: #ff6666; /* Darker color on hover */
    }

   .info-message {
    text-align: center;
    background-color: #ff4b4b;
    color: white;
    padding: 20px;
    border-radius: 10px;
    margin: 20px auto; /* Center the div horizontally */
    width: 75%; /* Set the width of the div */
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="title">BEAM - Vitamin Supplement Recommendation System</h1>', unsafe_allow_html=True)

    st.sidebar.header("User Input Parameters")

    # Default user ID
    user_id = 1
    age = st.sidebar.number_input("Age", min_value=0, step=1, value=65)
    gender = st.sidebar.selectbox("Gender", ("male", "female"))
    pregnant = st.sidebar.checkbox("Pregnant", False)
    lifestyle = st.sidebar.selectbox("Lifestyle", ("non-athlete", "athlete"))

    medications = st.sidebar.multiselect(
        "Medications",
        ["blood_thinners", "antibiotics", "diuretics", "statins", "antidepressants", "oral_contraceptives", "antacids"]
    )

    illnesses = st.sidebar.multiselect(
        "Illnesses",
        ["osteoporosis", "anemia", "diabetes", "hypertension", "chronic kidney disease", "heart disease", "thyroid disorder", "depression"]
    )

    st.sidebar.header("Test Results (1-10 scale)")

    vitamin_d = st.sidebar.slider("Vitamin D", min_value=0, max_value=10, value=5)
    calcium = st.sidebar.slider("Calcium", min_value=0, max_value=10, value=3)
    magnesium = st.sidebar.slider("Magnesium", min_value=0, max_value=10, value=8)
    vitamin_a = st.sidebar.slider("Vitamin A", min_value=0, max_value=10, value=9)
    vitamin_c = st.sidebar.slider("Vitamin C", min_value=0, max_value=10, value=10)
    iron = st.sidebar.slider("Iron", min_value=0, max_value=10, value=2)
    folate = st.sidebar.slider("Folate", min_value=0, max_value=10, value=1)

    test_results = {
        "Vitamin D": vitamin_d,
        "Calcium": calcium,
        "Magnesium": magnesium,
        "Vitamin A": vitamin_a,
        "Vitamin C": vitamin_c,
        "Iron": iron,
        "Folate": folate
    }

    if st.sidebar.button("Get Recommendations"):
        recommendations = recommend_supplements(user_id, test_results, age, gender, medications, illnesses, pregnant, lifestyle)

        for key, value in recommendations.items():
            if value:  # Only display categories with recommendations
                st.markdown(f"### {key}")
                for recommendation in value:
                    st.markdown(f"<div class='recommendations'><p>{recommendation}</p></div>", unsafe_allow_html=True)

        # Display info message
        st.markdown("<div class='info-message'><h7>Your shopping basket has been autofilled. You can now check your receipt and proceed to the payment.</h7></div>", unsafe_allow_html=True)

        # Display receipt
        st.subheader("Monthly Supplement Receipt")
        receipt_items = []
        prices = {
            "Vitamin D": 0.006,
            "Calcium": 0.004,
            "Magnesium": 0.003,
            "Vitamin A": 0.005,
            "Vitamin C": 0.002,
            "Iron": 0.007,
            "Folate": 0.003
        }
        total_cost = 0

        for need_level, items in recommendations.items():
            for item in items:
                nutrient, details = item.split(':')[0], item.split('.')[1].strip()
                if "Take" in details:
                    amount = details.split('Take ')[1].split(' ')[0]
                    unit = details.split(' ')[2]
                    daily_amount = int(amount)
                    monthly_amount = daily_amount * 30
                    price_per_unit = prices.get(nutrient, 0)
                    cost = price_per_unit * monthly_amount
                    total_cost += cost
                    receipt_items.append(f"{nutrient}: {daily_amount} {unit} x 30 days = {monthly_amount} {unit} - ${cost:.2f}")

        receipt_html = "<div class='receipt'>"
        for item in receipt_items:
            receipt_html += f"<div class='receipt-item'>{item}</div>"
        receipt_html += f"<div class='total'>Total Cost: ${total_cost:.2f}</div>"
        receipt_html += "</div>"
        st.markdown(receipt_html, unsafe_allow_html=True)

        # Pay Button
        st.markdown("<div class='pay-button'><button class='pay-now-button'>Pay Now</button></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
