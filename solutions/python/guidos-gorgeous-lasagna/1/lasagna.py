"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40

def preparation_time_in_minutes(number_of_layers):
    """Function that evaluates prep time from each additional layer of lasagna
    :param number_of_layers: int - number of layers of lasagna
    :return: int - prep time in minutes

    Function that takes the number of layers of lasagna and multiplies it by the time
    required to prepare each layer which the recipe states is 2 minutes per layer. """
    prep_time_per_layer = 2
    return number_of_layers * prep_time_per_layer

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the minutes for bake time from the recipe and subtracts the
    actual time spent baking to produce an integer value for remaining bake time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed bake time

    :param number_of_layers: int - number of layers of lasagna
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - elapsed bake time in minutes

    Function that adds the amount of time it takes to produce each layer of lasagna
    in minutes and adds that to the amount of time the lasagna has spent baking
    to provide the total amount of time spent that has elapsed to prepare and cook the
    lasagna.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


print(elapsed_time_in_minutes(1, 3))
# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
