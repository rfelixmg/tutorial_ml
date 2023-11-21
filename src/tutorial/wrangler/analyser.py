from typing import List, Any, Tuple

import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from ..schemas import AdUnit


def analyze_ad_performance(data: List[AdUnit]) -> Tuple[LinearRegression, Any]:
    """Analyzes ad performance using a linear regression model."""
    X = np.asarray([[datum.views, datum.clicks] for datum in data])
    y = np.asarray([datum.engagement_rate for datum in data])

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict and evaluate the model
    predictions = model.predict(X_test)
    return model, predictions
