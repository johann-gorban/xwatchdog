from datetime import datetime, timezone

class Pool:
    def __init__(self, url: str, token: str, capacity: float = 100):
        self._url = url
        self._token = token
        self._capacity = capacity
        self._update_time = datetime.now(tz=timezone.utc)

    @property
    def token(self) -> str:
        return self._token
    
    @property
    def url(self) -> str:
        return self._url
    
    @property
    def capacity(self) -> float:
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity: float):
        self._capacity = capacity
        self._update_time = datetime.now(tz=timezone.utc)

    @property
    def update_time(self) -> datetime:
        return self._update_time


pools = [
    Pool(
        url='https://www.exponent.finance/liquidity/shyusd-18Nov25',
        token='sHYUSD'
    )
]