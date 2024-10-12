def hello():
  print("Hello, World!")

def bye():
  print("Bye, World!")


def test_hello():
  words = hello()
  assert words == "Hello, World!"
