# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'Part 1/Section 02 - A Quick Refresher'))
    print(os.getcwd())
except:
    pass
# %% [markdown]
# ### Conditionals
# %% [markdown]
# A conditional is a construct that allows you to branch your code based on conditions being met (or not)
# %% [markdown]
# This is achieved using **if**, **elif** and **else** or the **ternary operator** (aka conditional expression)

# %%
a = 2
if a < 3:
    print('a < 3')
else:
    print('a >= 3')

# %% [markdown]
# **if** statements can be nested:

# %%
a = 15

if a < 5:
    print('a < 5')
else:
    if a < 10:
        print('5 <= a < 10')
    else:
        print('a >= 10')

# %% [markdown]
# But the **elif** statement provides far better readability:

# %%
a = 15
if a < 5:
    print('a < 5')
elif a < 10:
    print('5 <= a < 10')
else:
    print('a >= 10')

# %% [markdown]
# In Python, **elif** is the closest you'll find to the switch/case statement available in some other languages.
# %% [markdown]
# Python also provides a conditional expression (ternary operator):
#
# X if (condition) else Y
#
# returns (and evaluates) X if (condition) is True, otherwise returns (and evaluates) Y

# %%
a = 5
res = 'a < 10' if a < 10 else 'a >= 10'
print(res)


# %%
a = 15
res = 'a < 10' if a < 10 else 'a >= 10'
print(res)

# %% [markdown]
# Note that **X** and **Y** can be any expression, not just literal values:

# %%


def say_hello():
    print('Hello!')


def say_goodbye():
    print('Goodbye!')


# %%
a = 5
say_hello() if a < 10 else say_goodbye()


# %%
a = 15
say_hello() if a < 10 else say_goodbye()
