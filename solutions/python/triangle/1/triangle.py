def is_valid_triangle(sides):
    a, b, c = sides

    #inequality holds
    inequality_holds = (a + b > c) and (b + c > a) and (c + a > b)

    #has size
    has_size = (a > 0) and (b > 0) and (c > 0)

    #True if only if BOTH are true
    return inequality_holds and has_size



def equilateral(sides):
    """ A function to determine if a triangle is equilateral (all sides the same)

        Param side a: int or float - length of side
        Param side b: int or float - length of side
        Param side c: int or float - length of side
        return - str "triangle is equilateral"
     """
    #unpack the list
    side_a, side_b, side_c = sides

    #ensure the triangle is a valid triangle
    if not is_valid_triangle(sides):
        return False

    #check if sides are different sizes
    if side_a != side_b != side_c:
        return False

    #check if all sides are equal
    if side_a == side_b and side_b == side_c and side_a == side_c:
        return True


def isosceles(sides):
    """A function to determine if a triangle is equilateral (all sides the same)

        Param side a: int or float - length of side
        Param side b: int or float - length of side
        Param side c: int or float - length of side
        return - str "triangle isosceles"""
    #unpack list
    side_a, side_b, side_c = sides

    #check for valid triangle
    if not is_valid_triangle(sides):
       return False

    if (side_a==side_b)  or (side_a==side_c)  or (side_b==side_c):
        return True

    return False

def scalene(sides):
    """A function to determine if a triangle is equilateral (all sides the same)

            Param side a: int or float - length of side
            Param side b: int or float - length of side
            Param side c: int or float - length of side
            return - str "triangle isosceles"""
    side_a, side_b, side_c = sides

    # check for valid triangle
    if not is_valid_triangle(sides):
       return False

    # check to see if all sides are unequal
    if (side_a != side_b) and (side_a != side_c) and (side_b != side_c):
        return True
    return False