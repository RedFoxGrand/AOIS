class HashData:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._ID = None
        self._C = 0
        self._U = 0
        self._T = 1
        self._L = 0
        self._D = 0
        self._P0 = -1
        self._Pi = None

    @property
    def ID(self) -> str:
        return self._ID

    @ID.setter
    def ID(self, value: str) -> None:
        self._ID = value

    @property
    def C(self) -> int:
        return self._C

    @C.setter
    def C(self, value: int) -> None:
        self._C = value

    @property
    def U(self) -> int:
        return self._U

    @U.setter
    def U(self, value: int) -> None:
        self._U = value

    @property
    def T(self) -> int:
        return self._T

    @T.setter
    def T(self, value: int) -> None:
        self._T = value

    @property
    def L(self) -> int:
        return self._L

    @L.setter
    def L(self, value: int) -> None:
        self._L = value

    @property
    def D(self) -> int:
        return self._D

    @D.setter
    def D(self, value: int) -> None:
        self._D = value

    @property
    def P0(self) -> int:
        return self._P0

    @P0.setter
    def P0(self, value: int) -> None:
        self._P0 = value

    @property
    def Pi(self) -> str:
        return self._Pi

    @Pi.setter
    def Pi(self, value: str) -> None:
        self._Pi = value

    def __str__(self) -> str:
        ID_str = str(self._ID)[:15].ljust(15) if self._ID else "".ljust(15)
        Pi_str = str(self._Pi)[:25].ljust(25) if self._Pi else "".ljust(25)
        return f"{ID_str} | {self._C} | {self._U} | {self._T} | {self._L} | {self._D} | {self._P0:2} | {Pi_str}"
