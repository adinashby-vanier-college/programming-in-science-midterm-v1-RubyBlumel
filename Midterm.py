import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = (radius ** 2) * (math.pi)
    return round(area, 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    if n < 4:
        return "The triangle height should be at least 4."
    elif n == 4:
        #top is the same for all 
        x = "*"
        top1 = "*"
        top2 = "**"
        top3 = "* *"
       
        return f"{top1}\n{top2}\n{top3}\n{x * n}"
        
    else:
        top1 = "*"
        top2 = "**"
        top3 = "* *"
        # middle
        x = "*"
        y = " "
        middle2 = "*"
        for i in range(3, n):
            middle2 = "  " * (n - i - 1)
            return f"{top1}\n{top2}\n{top3}\n{x}{middle2}{x}\n{x * n}"


# Q3: Inverted Pyramid
def inverted_pyramid(n):
    return ""

# ----------------------------------------------------------------
print(hollow_right_triangle(4))
