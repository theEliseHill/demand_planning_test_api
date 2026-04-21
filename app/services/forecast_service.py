from app.repositories.sales_repository import SalesRepository

class ForecastService:
    def __init__(self, repo: SalesRepository):
        self.repo = repo
# I think we use 8 weeks in o9 but I'm not really sure
    def moving_average(self, values: list[float], window: int = 8) -> float:
        if len(values) < window:
            raise ValueError("Not enough data")

        return sum(values[-window:]) / window
    def forecast_from_repository(self, window: int = 3) -> float:
        data = self.repo.get_sales_data()
        return self.moving_average(data, window)