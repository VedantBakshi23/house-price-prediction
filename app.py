import json
from flask import Flask, render_template, request
import pandas as pd
from model.model import predict_price  # Import prediction function

app = Flask(__name__)

# Initialize an empty DataFrame
df = pd.DataFrame(columns=[
    "UNDER_CONSTRUCTION", "RERA", "BHK_NO.", "RESALE", "LONGITUDE", "LATITUDE",
    "area", "POSTED_BY Dealer", "POSTED_BY Owner", "BHK_OR_RK", "city_tier tier2", "city_tier tier3"
])

@app.route('/', methods=['GET', 'POST'])
def index():
    global df  
    message = ""

    if request.method == 'POST':
        try:
            print("Received form data:", request.form)  # Debugging

            # Convert form data into correct format
            filters = {
                "UNDER_CONSTRUCTION": int(request.form["under_construction"]),
                "RERA": int(request.form["RERA"]),
                "BHK_NO.": int(request.form["BHK_NO"]),
                "RESALE": int(request.form["RESALE"]),
                "LONGITUDE": float(request.form["LONGITUDE"]),
                "LATITUDE": float(request.form["LATITUDE"]),
                "area": float(request.form["area"]),
                "POSTED_BY Dealer": int(request.form["POSTED_BY_Dealer"]),
                "POSTED_BY Owner": int(request.form["POSTED_BY_Owner"]),
                "BHK_OR_RK": int(request.form["BHK_OR_RK"]),
                "city_tier tier2": int(request.form["city_tier_2"]),
                "city_tier tier3": int(request.form["city_tier_3"])
            }

            # Append new entry to DataFrame
            df = pd.concat([df, pd.DataFrame([filters])], ignore_index=True)

            # Reshape the data before passing to prediction function
            predicted_price = predict_price([df.iloc[-1].tolist()])  
            
            message = f"Predicted Price: ₹{predicted_price:.2f}"
        except Exception as e:
            message = f"Error: {str(e)}"
        print(message)

    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)
