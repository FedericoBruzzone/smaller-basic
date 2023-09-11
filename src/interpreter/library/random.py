class Random(object):
    """
    Random class for generating random numbers.
    """

    def __init__(self) -> None:
        """
        Initialize Random class.
        """
        pass

    def Random(self, start: int, end: int) -> int:
        """
        Return a random integer in the range [start, end].
        """
        import random
        return random.randint(start, end)

    def Randomize(self, seed: int = 0) -> None:
        """
        Set the seed for the random number generator.
        """
        import random
        random.seed(seed)

    def GetRandomNumber(self) -> int:
        """
        Return a random integer.
        """
        import random
        import sys
        return random.randint(0, sys.maxsize)

    def call(self, func_name: str, *args):
        """
        Call a function with the given arguments and keyword arguments.
        """
        return getattr(self, func_name)(*args)

