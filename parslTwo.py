import parsl
from parsl import python_app, bash_app, ThreadPoolExecutor

# Configuration for the executor
parsl.load(ThreadPoolExecutor(max_workers=4))

@python_app
def add(a, b):
    return a + b

@python_app
def multiply(a, b):
    return a * b

# Creating tasks
result1 = add(1, 2)
result2 = multiply(result1, 3)

# Getting the result
print(result2.result())  # Should print 9

