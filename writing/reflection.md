# Containment Checking

## Evelyn Griffith

## Program Output

### Report at least five examples of program output to demonstrate that your `containmentcheck` program works correctly

TODO: Document and justify your choice for all of the experiment parameters

#### One output from running the `containmentcheck` program

TODO: Provide a fenced code block with one output from running the program

#### One output from running the `containmentcheck` program

TODO: Provide a fenced code block with one output from running the program

#### One output from running the `containmentcheck` program

TODO: Provide a fenced code block with one output from running the program

#### One output from running the `containmentcheck` program

TODO: Provide a fenced code block with one output from running the program

#### One output from running the `containmentcheck` program

TODO: Provide a fenced code block with one output from running the program

## Experiment Design

TODO: Explain the setup for your experiment that you ran to characterize the
performance of the different configurations of containment checking algorithms.
For instance, you should consider the following parameters as a part of your
experiment:

- The data container: `set`, `list`, and `tuple`
- The size of the data container: small values (e.g., 1 million numbers) to big
  values (e.g., 32 million numbers)
- Whether or not the value that it being searched for is in the list
- The maximum value of the numbers that are inside of the data container

TODO: You must justify every part of your experiment design and then furnish
output examples to demonstrate that your program generates correct data!

## Research Questions

- RQ 1: How does the size of the container effect the run time of the program when the number being searched for doesn't exceed the maximum value (also consider this when talking about running for a list, set, and tuple)?

- RQ 2: How does the size of the container effect the run time of the program when the number being searched for exceeds the maximum value(also consider this when talking about running for a list, set, and tuple)?

- RQ 3: Which data container is the fastes when searching for a value that exceeds the maximum value in any container size?

## Data Tables

TODO: Use Markdown to provide one or more data tables that summarize the results
from running the `containmentcheck` program in different configurations. You
should provide enough data tables and output values to ensure that you can
answer all of your research questions and use the empirical results to classify
the likely worst-case time complexity of each of the algorithms.

| Exceed |  Size   |  Maximum    |  List Avg Time   |  Tuple Avg Time   |  Set Avg Time   |
| :----: | :-----: | :---------: | :--------------: | :---------------: | :-------------: |
|  Yes   | 5,000   | 50,000,000  |    0.0000718     |    0.0000537      |    0.0003426    |
|  No    | 5,000   | 50,000,000  |                  |                   |                 |
|  Yes   | 10,000  | 50,000,000  |    0.0001607     |    0.0001375      |    0.0005095    |
|  No    | 10,000  | 50,000,000  |                  |                   |                 |
|  Yes   | 20,000  | 50,000,000  |    0.0003311     |    0.0003213      |    0.0016860    |
|  No    | 20,000  | 50,000,000  |                  |                   |                 |
## Performance Analysis

### Empirical Evaluation

TODO: Provide at least three paragraphs that explain which containment checking
algorithm is fastest, by how much it is faster, and how you knew that it was
faster, referencing the data in the aforementioned command outputs and the data
tables to support your response. You should make sure that you answer each of
the at least three research questions that you posed in a previous section.

TODO: Make sure that your responses explain WHY certain configurations are faster!
TODO: It is not sufficient to ONLY explain WHICH configuration is faster!

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.

### Analytical Evaluation

TODO: Using the provided source code for the different containment check
algorithms, your textbook, your experimental results, and any relevant online
resources that you cite in this reflection, define the worst-case time
complexity, using the big-O notation, for the three containment check
algorithms called `containment_check_tuple`, `containment_check_list`, and
`containment_check_set`. You should justify why you picked that complexity.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.

## Source Code

### Describe in detail how the provided source code works

TODO: Use a fenced code block to provide the requested source code
TODO: Write at least one paragraph to explain the request source code

```python
number_runs = 10
number_repeats = 3
execution_times = timeit.Timer(containment_check_lambda).repeat(
    repeat=number_repeats, number=number_runs
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.

## Professional Development

### What is challenging about designing an experiment to evaluate an algorithm's performance?

TODO: Provide a one-paragraph response that answers this question in your own words.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

### Why is it necessary to perform both an analytical and an empirical evaluation of an algorithm?

TODO: Provide a one-paragraph response that answers this question in your own words.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

### How do the empirical results suggest that you don't yet know the entire story about the performance of containment checking?

TODO: Provide a one-paragraph response that answers this question in your own words.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
