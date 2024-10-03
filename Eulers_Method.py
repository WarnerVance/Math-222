initial_y = 1
initial_x = 1
step = 0.1
end_x = 1.5
current_x = initial_x
current_y = initial_y

while current_x < end_x:
    x = current_x
    y = current_y
    slope = 3*y + 2*x*y
    current_x += step
    current_y += step * slope
    print(f"x: {x}, y: {y}, slope: {slope}")
    print(f"x: {current_x}, y: {current_y}")
print(f"Final x value: {current_x}") 
print(f"Final y value: {current_y}")