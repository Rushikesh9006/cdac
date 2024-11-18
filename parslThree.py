import parsl
from parsl import python_app, LocalExecutor

# Load the LocalExecutor
parsl.load(LocalExecutor())

@python_app
def add(a, b):
    return a + b

@python_app
def multiply(a, b):
    return a * b

# Create tasks
result1 = add(3, 5)       # Task to add 3 and 5
result2 = multiply(result1, 2)  # Task to multiply the result of the first task by 2

# Get the result
print(f"Result of multiplication: {result2.result()}")  # Should print 16

