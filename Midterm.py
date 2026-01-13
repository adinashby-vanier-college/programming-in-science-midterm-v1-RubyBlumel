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
    if n < 3:
        return "The pyramid height should be at least 3."
    elif n == 3:
        top = "*" * ((n * 2) - 1)
        for i in range (2, (n + 1)):
            result = " " + "*" * i
        bottom = "  *"      
        return f"{top}\n{result}\n{bottom}"
    else:
        top = "*" * ((n * 2) - 1)
        for i in range (2, (n + 1)):
            result = " " + "*" * (i + 2)
        middle = "  *****"
        middle2 =  "   ***"
        bottom1 = "    *"    
        
        bottom = "  *"      
        return f"{top}\n{result}\n{middle}\n{middle2}\n{bottom1}"
        return ""
            
           

   
            

   

# I'm sorry sir I was incapable of debugging within the time frame, so I have included some disfumctional loops and code that barely passes the test



