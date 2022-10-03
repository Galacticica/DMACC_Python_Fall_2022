'''
Program: inner_functions.py
Author: Reagan Zierke
Last date modified: 10/03/22

This program calculates the area and perimeter of rectangles.
'''

def measurements(distances):
    '''
    Deternines the area and perimeter of the rectangle.
    :param distances: the length and width of the rectangle
    '''
    #Sets length and width variables
    length = distances[0]
    if len(distances) == 1:
        width = distances[0]
    else:
        width = distances[1]

    #Calculates area
    def area(length, width):
        area = length*width
        return area

    #Calculates perimeter
    def perimeter(length, width):
        perimeter = (2*length) + (2*width)
        return perimeter
    perimeter_value = perimeter(length, width)
    area_value = area(length, width)
    #Returns value
    return (f"Perimeter= {perimeter_value: .1f} Area= {area_value: .1f}")



if __name__ == '__main__':
    #Tests for rectangle
    rectangle = [3.1, 3.4]
    result = measurements(rectangle)
    print(result)
    #Tests for square
    square = [3.5]
    result = measurements(square)
    print(result)
