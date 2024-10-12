def hello():
  return("Hello, World!")

def bye():
  return("Bye, World!")


def test_hello():
  words = hello()
  assert words == "Hello, World!"
