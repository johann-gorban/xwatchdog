class Pool:
    def __init__(self, url: str, token: str, capacity: float = 0):
        self._url = url
        self._token = token
        self._capacity = capacity

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


pools = [
    Pool(
        url="https://www.exponent.finance/liquidity/xsol-26Nov25",
        token="xSOL"
    ),
    Pool(
        url='https://www.exponent.finance/liquidity/shyusd-18Nov25',
        token='sHYUSD'
    ),
    Pool(
        url='https://www.exponent.finance/liquidity/kysol-30Sep25',
        token='kySOL'
    )
]