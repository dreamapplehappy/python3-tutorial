import os
import glob

print(os.getcwd())
os.chdir('/Users/dreamapple/Code/github/python3-tutorial/dive-into-python3/native-datatypes')
print(os.getcwd())

pathname = os.path.join('/Users/dreamapple/Code/github/python3-tutorial/dive-into-python3/', 'comprehensions/comprehensions.py')
print(pathname)
print(os.path.expanduser('~'))

(dirname, filename) = os.path.split(pathname)
print(dirname, filename)
(shortname, extension) = os.path.splitext(filename)
print(shortname, extension)

os.chdir('/Users/dreamapple/Code/github/python3-tutorial/dive-into-python3/comprehensions')
print(glob.glob('examples/*.py'))