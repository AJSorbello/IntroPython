class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output

    def __add__(self, other):
        # Converting both objects' heights into inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        # Adding them up
        total_height_inches = height_A_inches + height_B_inches

        # Getting the output in feet
        output_feet = total_height_inches // 12

        # Getting the output in inches
        output_inches = total_height_inches - (output_feet * 12)

        # Returning the final output as a new Height object
        return Height(output_feet, output_inches)

    def __sub__(self, other):
        # Converting both objects' heights into inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        # Subtracting them
        total_height_inches = height_A_inches - height_B_inches

        # Getting the output in feet
        output_feet = total_height_inches // 12

        # Getting the output in inches
        output_inches = total_height_inches - (output_feet * 12)

        # Returning the final output as a new Height object
        return Height(output_feet, output_inches)
    
    def __lt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A < height_inches_B

    def __le__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A <= height_inches_B

    def __eq__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A == height_inches_B
    
    def __ge__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A >= height_inches_B
    
    def __gt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A > height_inches_B
    
    def __ne__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A != height_inches_B
    
person_A_height = Height(5, 10)
person_B_height = Height(4, 10)
# add sum
height_sum = person_A_height + person_B_height

print("Total height:", height_sum)
person_C_height = Height(3, 9)

# subtract sub
height_sub = person_A_height - person_C_height
print("Height Difference:", height_sub)

print(Height(4, 6) < Height(4, 5))
print(Height(4, 5) > Height(4, 5))
print(Height(5, 9) <= Height(5, 10))  
print(Height(4, 6) >= Height(4, 5))
print(Height(4, 5) == Height(4, 5))
print(Height(5, 9) != Height(5, 10))

height_1 = Height(4, 10)
height_2 = Height(5, 6)
height_3 = Height(7, 1)
height_4 = Height(5, 5)
height_5 = Height(6, 7)
height_6 = Height(5, 6)
heights = [height_1, height_2, height_3, height_4, height_5, height_6]

heights = sorted(heights, reverse=True)
for height in heights:
    print(height)
