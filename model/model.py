from xgboost import XGBRegressor

loaded_model = XGBRegressor()
loaded_model.load_model('model/model.bin')

def predict_price(features):
    import numpy as np
    features = np.array(features).reshape(1, -1)  # Ensure 2D format
    prediction = loaded_model.predict(features)
    return prediction[0]
