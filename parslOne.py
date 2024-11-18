import parsl
from parsl import python_app

# Configure Parsl with a local executor
parsl.load(parsl.Config(
    executors=[parsl.executors.LocalExecutor()]
))

@python_app
def Add(x, y):
    return x + y

@python_app
def Multiply(x, y):
    return x * y

# Define tasks
task1 = Add(1, 2)
task2 = Add(3, 4)
task3 = Multiply(task1, task2)

# Retrieve result
result = task3.result()
print(f"Result: {result}")

