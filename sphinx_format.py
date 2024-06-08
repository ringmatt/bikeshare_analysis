# Title: [Name of the Script]
# Author: [Matt Ring]
# Date Created: [YYYY-MM-DD]

# Descrption: [What this script does.]

# Structure
# 1. [Step 1]
# 2. [Step 2]

# %% [Step 1]

# Example Sphinx docstring
"""[Summary]

:param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
:type [ParamName]: [ParamType](, optional)
...
:raises [ErrorType]: [ErrorDescription]
...
:return: [ReturnDescription]
:rtype: [ReturnType]
"""

# %% [Step 2]

# Go to "File > Preferences > Settings" for Windows to change autodocstring format
# https://stackoverflow.com/questions/51716465/python-visual-studio-code-autodocstring-configuration

def simple_function(a = 1, b = 1):
    """_summary_

    :param a: Any number, defaults to 1
    :type a: int or float, optional

    :param b: Any number, defaults to 1
    :type b: int or float, optional

    
    :raises TypeError: Returned when either a or b is not a number.


    :return: The sum of a and b.
    :rtype: int or float
    """

    # Check if a is a number
    if ((isinstance(a, int) | isinstance(a, float))
        
        # Check if b is a number
        & (isinstance(b, int) | isinstance(b, float))):
    
        # Add a and b
        return a + b
    
    # If not, throw an error
    else:
        raise TypeError("One value is not a number.")
