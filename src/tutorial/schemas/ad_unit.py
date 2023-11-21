from pydantic import BaseModel


class AdUnit(BaseModel):
    ad_id: int
    views: int
    clicks: float
    engagement_rate: float
