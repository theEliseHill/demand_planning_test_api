from fastapi import APIRouter, HTTPException, Depends

# the moving average class 
from app.services.forecast_service import ForecastService
from app.models.schemas import ForecastRequest
from app.repositories.sales_repository import SalesRepository

router = APIRouter()

# service = ForecastService()
# def get_service():
#     return ForecastService()
def get_repository():
    return SalesRepository()

# This is called from the endpoint but then we do the same thing and call the repository
def get_service(repo: SalesRepository = Depends(get_repository)):
    return ForecastService(repo)

@router.get("/health")
def health_check():
    return {"status": "ok :)"}

# Gets called when I use the website (swagger ui)
# Forecast request is the validation
# Forecast servive gets the information for the calculation
@router.post("/forecast")
def forecast(request : ForecastRequest, 
             service : ForecastService = Depends(get_service)):
    # So we have the repo from the above call, now we attempt to calculate the forecast
    try:
        result = service.moving_average(
            request.values,
            request.window
        )
        return {"forecast": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/forecast-from-db")
def forecast_from_db(service : ForecastService = Depends(get_service)):
    result = service.forecast_from_repository()
    return {"forecast": result}