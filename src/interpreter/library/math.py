class Math(object):
    """
    Math class for performing math operations.
    """

    def __init__(self) -> None:
        """
        Initialize Math class.
        """
        pass

    def __factorial(self, n: int) -> int:
        """
        Return the factorial of n.
        """
        if n == 0:
            return 1
        return n * self.__factorial(n - 1)

    def Sin(self, x: float, terms: int = 10) -> float:
        """
        Return the sine of x radians.
        """
        res: float = 0.0
        for i in range(terms):
            sign: int = (-1) ** i
            term = x ** (2 * i + 1) / self.__factorial(2 * i + 1)
            res += sign * term
        return res

    def Cos(self, x: float, terms: int = 10) -> float:
        """
        Return the cosine of x radians.
        """
        res: float = 0.0
        for i in range(terms):
            sign: int = (-1) ** i
            term = x ** (2 * i) / self.__factorial(2 * i)
            res += sign * term
        return res

    def Tan(self, x: float, terms: int = 10) -> float:
        """
        Return the tangent of x radians.
        """
        return self.Sin(x, terms) / self.Cos(x, terms)

    def Cot(self, x: float, terms: int = 10) -> float:
        """
        Return the cotangent of x radians.
        """
        return self.Cos(x, terms) / self.Sin(x, terms)

    def Abs(self, x: float) -> float:
        """
        Return the absolute value of x.
        """
        if x < 0:
            return -x
        return x

    def Pow(self, x: float, y: float, terms: int = 10) -> float:
        """
        Return x raised to the power of y.
        """
        return x ** y

    def Exp(self, x: float, terms: int = 10) -> float:
        """
        Return e raised to the power of x.
        """
        res: float = 0.0
        for i in range(terms):
            term = x ** i / self.__factorial(i)
            res += term
        return res

    def Log(self, x: float, terms: int = 10) -> float:
        """
        Return the natural logarithm of x.
        """
        res: float = 0.0
        for i in range(1, terms + 1):
            term = (x - 1) ** i / i
            res += term
        return res

    def Sqrt(self, x: float, eps: float = 1e-7, terms: int = 100) -> float:
        """
        Return the square root of x.
        """
        if x < 0:
            raise ValueError("Cannot take square root of negative number.")

        guess: float = x / 2
        for _ in range(terms):
            guess = (guess + x / guess) / 2
            error: float = abs(x - guess ** 2)
            if error < eps:
                return guess
        return guess

    def Pi(self) -> float:
        """
        Return the value of pi.
        """
        return 3.141592653589793

    def E(self) -> float:
        """
        Return the value of e.
        """
        return 2.718281828459045

    def call(self, func_name: str, *args) -> float:
        """
        Call a function with the given arguments and keyword arguments.
        """
        return getattr(self, func_name)(*args)
