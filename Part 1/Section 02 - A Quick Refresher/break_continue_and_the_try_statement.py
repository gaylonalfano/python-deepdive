# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'Part 1/Section 02 - A Quick Refresher'))
    print(os.getcwd())
except:
    pass
# %% [markdown]
# ### Loop Break and Continue inside a Try...Except...Finally
# %% [markdown]
# Recall that in a ``try`` statement, the ``finally`` clause always runs:

# %%
a = 10
b = 1
try:
    a / b
except ZeroDivisionError:
    print('division by 0')
finally:
    print('this always executes')


# %%
a = 10
b = 0
try:
    a / b
except ZeroDivisionError:
    print('division by 0')
finally:
    print('this always executes')

# %% [markdown]
# So, what happens when using a ``try`` statement within a ``while`` loop, and a ``continue`` or ``break`` statement is encountered?

# %%
a = 0
b = 2

while a < 3:
    print('-------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:

        print('{0}, {1} - division by 0'.format(a, b))
        res = 0
        continue
    finally:
        print('{0}, {1} - always executes'.format(a, b))

    print('{0}, {1} - main loop'.format(a, b))

# %%
a = 0
b = 2

while a < 4:
    print('--------------')
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError as err:
        print(f"{a}, {b} - division by 0")
        continue
    finally:
        print(f"{a}, {b} - always executes")

    print(f"{a}, {b} - main loop")

# %% [markdown]
# As you can see in the above result, the ``finally`` code still executed, even though the current iteration was cut short with the ``continue`` statement.
# %% [markdown]
# This works the same with a ``break`` statement:
# %%
a = 0
b = 2

while a < 4:
    print('--------------')
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError as err:
        print(f"{a}, {b} - division by 0")
        break
    finally:
        print(f"{a}, {b} - always executes")

    print(f"{a}, {b} - main loop")

# %%
a = 0
b = 2

while a < 3:
    print('-------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        res = 0
        break
    finally:
        print('{0}, {1} - always executes'.format(a, b))

    print('{0}, {1} - main loop'.format(a, b))

# %% [markdown]
# We can even combine all this with the ``else`` clause:

# %% [markdown]
# # We can even combine all this with the ``while/else`` clause.
# But first I'm going to **test** some **markdown _out_**
#  * This is a sub-list
#  * Here is another item
#  - Another sub-list but using ``-``
# ```python
# print('hello')
# ````

a = 0
b = 10

while a < 4:
    print('----------------')
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError:
        print(f"{a}, {b} - division by 0")
        break
    finally:
        print(f"{a}, {b} - always executes")

    print(f"{a}, {b} - main loop")
else:
    print('\n\nno errors were encountered!')
# %%
a = 0
b = 2

while a < 3:
    print('-------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        res = 0
        break
    finally:
        print('{0}, {1} - always executes'.format(a, b))

    print('{0}, {1} - main loop'.format(a, b))
else:
    print('\n\nno errors were encountered!')


# %%
a = 0
b = 5

while a < 3:
    print('-------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        res = 0
        break
    finally:
        print('{0}, {1} - always executes'.format(a, b))

    print('{0}, {1} - main loop'.format(a, b))
else:
    print('\n\nno errors were encountered!')
