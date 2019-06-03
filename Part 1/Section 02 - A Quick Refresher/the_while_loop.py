# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'Part 1/Section 02 - A Quick Refresher'))
    print(os.getcwd())
except:
    pass
# %% [markdown]
# ### While Loops
# %% [markdown]
# The **while** loop is a way to repeatg a block of code as long as a specified condition is met.
# %% [markdown]
# ``while <exp is true>:
#     code block``

# %%
i = 0
while i < 5:
    print(i)
    i += 1

# %% [markdown]
# Note that there is no guarantee that a **while** loop will execute at all, not even once, because the condition is tested **before** the loop runs.

# %%
i = 5
while i < 5:
    print(i)
    i += 1

# %% [markdown]
# Some languages have a concept of a while loop that is guaranteed to execute at least once:
#
# ``do
#     code block
# while <exp is true>
# ``
# %% [markdown]
# There is no such thing in Python, but it's easy enough to write code that works that way.
#
# We create an infinite loop and test the condition inside the loop and break out of the loop when the condition becomes false:

# %%
i = 5

while True:
    print(i)
    if i >= 5:
        break

# %% [markdown]
# As you can see the loop executed once (and will always execute at least once, no matter the starting value of i.)
#
# This is a standard pattern and can be useful in a variety of scenarios.
#
# A simple example might be getting repetitive user input until the user performs and action or provides some specific value.
# %% [markdown]
# For example, suppose we want to use the console to let users enter their name. We just want to make sure their name is at least 2 characters long, contains printable characters only, and only contains alphabetic characters:
    # We might try it this way:

    # %%
min_length = 2

name = input('Please enter your name:')

while not(len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input('Please enter your name:')

print('Hello, {0}'.format(name))

# %% [markdown]
# This works just fine, but notice that we had to write the code to elicit user input **twice** in our code. This is not good practice, and we can easily clean this up as follows:

# %%
min_length = 2

while True:
    name = input('Please enter your name:')
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break

print('Hello, {0}'.format(name))

# %% [markdown]
# We saw how the **break** statement exits the **while** loop and execution resumes on the line immediately after the while code block.
#
# Sometimes, we just want to cut the current iteration short, but continue looping, without exiting the loop itself.
#
# This is done using the **continue** statement:

# %%
a = 0
while a < 10:
    a += 1
    if a % 2:
        continue
    print(a)

# %% [markdown]
# Note that there are much better ways of doing this! We'll cover that in later videos (comprehensions, generators, etc)
# %% [markdown]
# The **while** loop also can be used with an **else** clause!!
# %% [markdown]
# The **else** is executed if the while loop terminated without hitting a **break** statement (we say the loop terminated **normally**)
# %% [markdown]
# Suppose we want to test if some value is present in some list, and if not we want to append it to the list (again there are better ways of doing this):
# %% [markdown]
# First, here's how we might do it without the benefit of the **else** clause:

# %%
l = [1, 2, 3]
val = 10

found = False
idx = 0
while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1

if not found:
    l.append(val)
print(l)

# %% [markdown]
# Using the **else** clause is easier:

# %%
l = [1, 2, 3]
val = 10

idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)

print(l)


# %%
l = [1, 2, 3]
val = 3

idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)

print(l)
