import sys
import urllib
import urllib.request


# Both packages and modules are type of module.
print(type(urllib))
print(type(urllib.request))

print(urllib.__path__)  # Returns the path of a module
print(sys.path)         # Python searches modules inside the directories listed in sys.path
print(sys.path[0])      # First item in the list is the current directory.
# We can append a directory to sys.path or...
# We can set the directory inside the PYTHONPATH environment variable.