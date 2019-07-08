"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

# automatically closes file after performing methods with 'with'
# otherwise would have to run f.open, methods, f.close
with open('foo.txt', 'r') as f:
    for line in f:
        print(line, end='')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

# non-with version
# b = open('bar.txt', 'w')
# b.write("""One ring to rule them all
# one ring to find them
# one ring to bring them all and in the darkness bind them""")
# b.close()

# cleaner imo
with open('bar.txt', 'w') as b:
    b.write("""One ring to rule them all
one ring to find them
one ring to bring them all and in the darkness bind them""")
