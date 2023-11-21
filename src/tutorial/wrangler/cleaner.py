from typing import List

from ..schemas import AdUnit


def clean_data(data: List[AdUnit]) -> List[AdUnit]:
    """Performs basic data cleaning."""
    # Example: Fill missing values
    # TODO: implement your operation here
    return data


def preprocess_data(data: List[AdUnit]) -> List[AdUnit]:
    """Preprocesses the data for analysis."""
    # Example: Normalize the 'views' and 'clicks'

    for datum in data:
        datum.views -= 10
        datum.clicks /= 100

    return data
