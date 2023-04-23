"""
A palindrome is a word that is symmetric: if we write it backward, the result word is the
same. For example, “HANNAH” is a palindrome, but “GAGA” is not. Write a short program
that determines whether a word is a palindrome.
"""

def solve(w: str) -> bool:
    return True if w.lower() == w.lower()[::-1] else False


if __name__ == "__main__":
    print(solve("GAGA"))
