"""
A huge phone book containing pairs of the form {phone number, person's name} was
stored as a vector sorted by name in alphabetical order. Write a program that finds the
phone number of a given person in this list, bearing in mind that the list is very large and that
users need the search results to be as fast as possible.
"""


def solve(arr, person):
    left, right, orientation = 0, len(arr) - 1, "left"

    while left < right:
        middle = left + (right - left) // 2
        found = arr[middle] if arr[middle].get(person, None) else None

        while not found:
            if orientation == "right":
                middle += 1

            elif orientation == "left":
                middle -= 1

            found = arr[middle] if arr[middle].get(person, None) else None

        # check whether if the found person first letter is higher than the person first letter, eg, "A" > "B"
        if list(found.keys())[0] < person[0]:
            orientation = "right"
            left = middle + 1
        else:
            orientation = "left"
            right = middle

    return found


if __name__ == "__main__":
    n = solve(
        [
            {"A": 1},
            {"B": 2},
            {"C": 3},
            {"D": 4},
            {"E": 5},
            {"F": 6},
            {"G": 7},
            {"H": 8},
            {"I": 9},
            {"J": 10},
        ],
        "J",
    )
    print(n)
