import mouse
from timeit import default_timer as timer
x = int(input("How many clicks do you want? "))
start = timer()

for i in range(0,x):
    mouse.click('left')

end = timer()
print(end - start)
