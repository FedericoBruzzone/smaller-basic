class String(object):
    """
    String class for performing string operations.
    """

    def __init__(self):
        """
        Initialize String class.
        """
        pass

    def Length(self, s: str) -> int:
        """
        Return the length of the string.
        """
        res: int = 0
        for _ in s:
            res += 1
        return res

    def Substr(self, s: str, start: int, end: int) -> str:
        """
        Return a substring of the string.
        """
        if start < 0:
            start = 0
        if start >= len(s):
            return ""

        res = ""
        for i in range(start, end):
            res += s[i]

        return res

    def Concat(self, s1: str, s2: str) -> str:
        """
        Concatenate two strings.
        """
        res = ""
        for char in s1:
            res += char
        for char in s2:
            res += char
        return res

    def Find(self, s: str, sub: str) -> int:
        """
        Return the index of the first occurrence of the substring.
        """
        for i in range(len(s)):
            if s[i:i + len(sub)] == sub:
                return i
        return -1

    def ToUpper(self, s: str) -> str:
        """
        Return the string in upper case.
        """
        res = ""
        for char in s:
            if char >= 'a' and char <= 'z':
                res += chr(ord(char) - 32)
            else:
                res += char
        return res

    def ToLower(self, s: str) -> str:
        """
        Return the string in lower case.
        """
        res = ""
        for char in s:
            if char >= 'A' and char <= 'Z':
                res += chr(ord(char) + 32)
            else:
                res += char
        return res

    def Split(self, s: str, sep: str) -> list:
        """
        Return a list of substrings separated by the given separator.
        """
        res = []
        start = 0
        for i in range(len(s)):
            if s[i:i + len(sep)] == sep:
                res.append(s[start:i])
                start = i + len(sep)
        res.append(s[start:])
        return res

    def At(self, s: str, index: int) -> str:
        """
        Return the character at the given index.
        """
        if index < 0 or index >= len(s):
            raise Exception("Index out of bounds")
        return s[index]

    def call(self, func_name: str, *args):
        """
        Call a function with the given arguments and keyword arguments.
        """
        return getattr(self, func_name)(*args)


