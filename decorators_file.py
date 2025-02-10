import time

def execution_timer(func):

  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print("Execution time: {end_time - start_time} seconds")
    return result
  return wrapper

@execution_timer
def example_function():

  print("Running function...")
  time.sleep(2)
  print("Function execution completed")

if __name__ = "__main__":
    example_function()
