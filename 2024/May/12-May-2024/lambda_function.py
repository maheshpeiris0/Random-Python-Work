import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def lambda_handler(event, context):
    # Sample data
    X = np.array([1, 2, 3, 4, 5,6]).reshape(-1, 1)
    y = np.array([2, 4, 5, 4, 6,7])

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Create a linear regression model
    model = LinearRegression()
    
    # Fit the model on the training data
    model.fit(X_train, y_train)
    
    # Make predictions on the test data
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    
    return {
        'statusCode': 200,
        'body': {
            'Mean Squared Error': mse,
            'R-squared': r2_score(y_test, y_pred)
        }
    }

