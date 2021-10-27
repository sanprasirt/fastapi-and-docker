from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_all_cleanings() -> List[dict]:
    cleanings = [
        {"id": 1, "name": "My house", "cleaning_type": "full_clean",
            "price_per_house": 29.99},
        {"id": 2, "name": "SomeOne else's house",
            "cleaning_type": "spot_clean", "price_per_house": 19.99},
    ]
    return cleanings
