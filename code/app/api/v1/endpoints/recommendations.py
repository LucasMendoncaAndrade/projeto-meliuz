from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.recommendation_service import get_5_recommendations

router = APIRouter()

@router.get("/recommendations/{user_id}")
def get_recommendations(user_id: int):
    csv_data = 'app/data/products.csv'
    products = get_5_recommendations(csv_data)
    return JSONResponse(status_code=200,content={"user_id": user_id, "products": products})