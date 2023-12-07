def rectangle_area(width: int, height: int) -> int:
    """
    Calculates the area of a rectangle with given width and height.
 
    :param width: The width of the rectangle.
    :param height: The height of the rectangle.
    :return: The area of the rectangle.
    """
    return width * height
 
 
assert rectangle_area(4, 10) == 40
assert rectangle_area(5, 6) == 35,"area is not as expected"