"""Perform an experiment to study efficiency of containment checking."""

from typing import List
from typing import Tuple
from typing import Union
from typing import Any

from enum import Enum

import random
import timeit

import typer


from rich.console import Console

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for rich text output
console = Console()


class ContainmentCheckApproach(str, Enum):
    """Define the name for the approach for performing containment checking of structured types."""

    # define the three different approaches for containment checking
    list = "list"
    set = "set"
    tuple = "tuple"


def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # produce a human-readable value for a bool
    # True --> "Yes"
    # False --> "No"
    # originally had if answer != True:
    # Flake8 Linting Tool said it needed to be is not instead of !=
    # therefore it needed changed to have a passing build
    """ note that the build failed if we used != True instead of is not True """
    if answer is not True:
        return "No"
    else:
        return "Yes"


def generate_random_number(maximum: int, exceed: bool = False) -> int:
    """Generate a random list defined by the size."""
    # start with a random value that is one greater
    # than the maximum, which is helpful when benchmarking
    # a containment algorithm for a value not in the container
    random_value = maximum - 1
    # generate a random value in consideration of a maximum
    # only take this step when the exceed variable is False
    if exceed is True:
        random_number = random.randint(maximum + 1, maximum + 100)
        return random_number
    # return the randomly generated number of the value
    # that exceeds the specified maximum value
    else:
        return random_value


def generate_random_container(
    size: int,
    maximum: int,
    make_tuple: bool = False,
) -> Union[List[int], Tuple[int, ...]]:
    """Generate a random list defined by the size."""
    # generate a list of random values for a specific size
    # and with a number up to a specific maximum
    # convert the list to a tuple
    # only when the make_tuple boolean variable is True
    # return the randomly generated container of values
    randomlist: List[
        Any,
    ] = []
    while len(randomlist) < size:
        n = random.randint(0, maximum)
        randomlist.append(n)
    # if the make_tuple parameter is True, then return a tuple instead of a list
    if make_tuple is True:
        return tuple(randomlist)
    else:
        return randomlist


def containment_check_list(thelist: List[int], number: int) -> bool:
    """Determine if a value is contained in the list."""
    # assume that the value is not inside of the list
    found = False
    # the value is, in fact, inside of the list
    # so this function should return True
    if number in thelist:
        found = True
    return found
    # return bool to indicate whether or not value is found
    # NOTE: Make sure that you use the "in" operator for this function


def containment_check_tuple(thetuple: Tuple[int], number: int) -> bool:
    """Determine if a value is contained in the tuple."""
    # so this function should return True
    found = False
    # return bool to indicate whether or not value is found
    # Make sure that you use the "in" operator for this function
    # assume that the value is not inside of the tuple
    # the value is, in fact, inside of the tuple
    # so this function should return True
    if number in thetuple:
        found = True
    return found


def containment_check_set(thelist: List[int], number: int) -> bool:
    """Determine if a value is contained in the list."""
    # Conventional wisdom often suggests it is faster to:
    # - Convert a list to a set
    # - Search for a number in the set
    # ... than it is to search through a list
    # Reference to support this assertion:
    # https://docs.quantifiedcode.com/python-anti-patterns/performance/using_key_in_list_to_check_if_key_is_contained_in_a_list.html
    # assume that the value is not inside of the tuple
    found = False
    # convert the list to a set
    theset = set(thelist)
    # the value is, in fact, inside of the set
    # so this function should return True
    if number in theset:
        found = True
    return found
    # return bool to indicate whether or not value is found
    # Make sure that you use the "in" operator for this function


def calculate_average_values(data_list: List[float], data_count: int) -> List[float]:
    """Calculate the average values for the data in the provided list."""
    data_list_averages = []
    for data_value in data_list:
        current_average = data_value / data_count
        data_list_averages.append(current_average)
    return data_list_averages


def perform_containment_check_benchmark(
    containment_check_lambda,
) -> None:
    """Run an experiment using the timeit package for the specific function."""
    # set the number of runs inside of a benchmark
    # you may consider making this a parameter to the tool
    number_runs = 10
    # set the number of repeats for running an entire benchmark
    # you may consider making this a parameter to the tool
    number_repeats = 3
    # use the timeit module to evaluate performance with the current configuration
    # reference to learn about the timeit module:
    # https://docs.python.org/3/library/timeit.html
    # key insights:
    # --> each benchmark run will have a total of number_runs and timeit will report the total across number_runs
    # --> each of the entire benchmark run will be repeated a total of number_repeats times
    # Reference for using the lambda function:
    # https://stackoverflow.com/questions/5086430/how-to-pass-parameters-of-a-function-when-using-timeit-timer
    execution_times = timeit.Timer(containment_check_lambda).repeat(
        repeat=number_repeats, number=number_runs
    )
    # display the results of the benchmarking campaign
    # see the examples of the expected output to understand how to format the benchmark results
    console.print(
        f":stopwatch:  Total time for running {number_runs} runs in {number_repeats} benchmark campaigns: {execution_times}"
    )
    console.print()
    console.print(
        f":abacus: Average time for running one of {number_runs} runs in {number_repeats} benchmark campaigns: {calculate_average_values(execution_times, number_runs)}"
    )


@cli.command()
def containmentcheck(
    size: int = typer.Option(5),
    maximum: int = typer.Option(25),
    exceed: bool = typer.Option(False),
    approach: ContainmentCheckApproach = ContainmentCheckApproach.list,
) -> None:
    """Conduct a doubling experiment to measure the performance of containment checking."""
    # create the starting data container and random number
    random_container = None
    # generate a random value that goes up to the maximum value;
    # if the value of exceed is True then generate a number beyond the maximum
    random_number = generate_random_number(maximum, exceed)
    # display diagnostic details about the configuration of the experiment
    console.print(
        ":sparkles: Conducting an experiment to measure the performance of containment checking!"
    )
    console.print(f"\t Type of the data container: {approach}")
    console.print(f"\t Size of the data container: {size}")
    console.print(f"\t Maximum value for a number in the data container: {maximum}")
    console.print(
        f"\t Should the value to search for exceed the maximum number? {human_readable_boolean(exceed)}"
    )
    console.print(
        f"\t The random number that was generated is: {generate_random_number(random_number)}"
    )
    console.print()
    # conduct a doubling experiment for containment checking with the list data structure
    if approach.value == ContainmentCheckApproach.list:
        # generate the container of inputs consisting of random integer values
        random_container = generate_random_container(size, maximum, make_tuple=False)
        # create the containment check lambda function
        containment_check_lambda = lambda: containment_check_list(random_container, random_number)  # type: ignore
        perform_containment_check_benchmark(containment_check_lambda)
    # conduct a doubling experiment for containment checking with the tuple data structure
    elif approach.value == ContainmentCheckApproach.tuple:
        # generate the container of inputs consisting of random integer values
        random_container = generate_random_container(size, maximum, make_tuple=True)
        # create the containment check lambda function
        containment_check_lambda = lambda: containment_check_tuple(random_container, random_number)  # type: ignore
        perform_containment_check_benchmark(containment_check_lambda)
    # conduct a doubling experiment for containment checking with the set data structure
    elif approach.value == ContainmentCheckApproach.set:
        # generate the container of inputs consisting of random integer values
        random_container = generate_random_container(size, maximum, make_tuple=False)
        # generate a random value that goes up to the maximum value;
        containment_check_lambda = lambda: containment_check_set(random_container, random_number)  # type: ignore
        perform_containment_check_benchmark(containment_check_lambda)
