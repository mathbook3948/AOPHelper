from aspect import Aspect
from examples.loggingAdvice import LoggingAdvice

# Create an AOP instance and set advice
aop = Aspect()
aop.set_advice(LoggingAdvice())

@aop.apply
def test_function(x, y):
    """A simple addition function"""
    return x + y

@aop.apply
def error_function():
    """A function that intentionally raises an exception"""
    raise ValueError("Intentional error!")

@aop.apply
def slow_function():
    """A function that simulates slow execution"""
    import time
    time.sleep(2)
    return "Completed"

@aop.apply
async def test_async_function(x, y):
    return x + y

print(test_function(10, 20))


try:
    error_function()
except ValueError:
    pass

print(slow_function())