"""
Your friend is developing a small image processing program and has asked for your help
in implementing MS-Paint's “paint bucket”-like functionality. Their program represents
images using arrays of characters, with each array value representing a pixel and letters and
symbols representing different colors. For example, the following 4x6 matrix represents the
letter P in color "#", with background color "." (dot)
.###..
.#..#.
.###..
.#....
Your subroutine should take a pixel and a new color and paint the region of that pixel with
the new color, like MS-Paint's “paint bucket” tool.
"""
import pprint


def solve(image, pixel, color):
    original_color = image[0][1]
    if original_color == color:
        return

    for i in range(pixel[0] - 1, len(image)):
        for j in range(pixel[1] - 1, len(image[i])):
            while image[i][j] != "." and image[i][j] != color:
                if image[i][j] != color:
                    image[i][j] = color

                if image[i][j] == color:
                    break

    pprint.pprint(image)


if __name__ == "__main__":
    image = [
        [".", ".", ".", ".", ".", "."],
        [".", ".", "#", "#", "#", "."],
        [".", ".", "#", ".", "#", "."],
        [".", ".", "#", "#", "#", "."],
        [".", ".", "#", ".", ".", "."],
        [".", ".", ".", ".", ".", "."],
    ]

    # paint_bucket(
    #     image, 2, 3, "X"
    # )  # Change the color of the "P" to "X" starting from pixel (2,3)

    # The resulting image should be:
    # [
    #     ['.', '.', '.', '.', '.', '.'],
    #     ['.', '.', 'X', 'X', 'X', '.'],
    #     ['.', '.', 'X', '.', 'X', '.'],
    #     ['.', '.', 'X', 'X', 'X', '.'],
    #     ['.', '.', 'X', '.', '.', '.'],
    #     ['.', '.', '.', '.', '.', '.']
    # ]

    solve(image, (2, 3), "X")
