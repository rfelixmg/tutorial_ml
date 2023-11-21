import numpy as np
from typing import List

from ..schemas import AdUnit


def generate_ad_data(num_ads: int = 100) -> List[AdUnit]:
    """Generates random ad performance data."""
    data = [
        AdUnit(
            **{'ad_id': i,
               'views': np.random.randint(100, 10000),
               'clicks': np.random.randint(0, 1000),
               'engagement_rate': np.random.uniform(0, 1)
               })
        for i in range(num_ads)]

    return data
