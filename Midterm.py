import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = (radius ** 2) * (math.pi)
    return round(area, 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    if n < 4:
        return "The triangle height should be at least 4."
    else:
        #top is the same for all 
        top1 = "*"
        top2 = "**"
        # middle
        x = "*"
        y = " "
        middle1 = f"{x}{y}{x}"
        middle2 = ""
        for i in range(3, (n + 1)):
            middle2 = f"{x}{y * (n - i)}{x}"
        #bottom
        bottom = f"{x * n}"
    return f"{top1}\n{top2}\n{middle1}\n{middle2}\n{bottom}"


# Q3: Inverted Pyramid
def inverted_pyramid(n):
    return ""

# ----------------------------------------------------------------
print(hollow_right_triangle(6))
