---
title: "Testing Scientific Software: A Practical Guide for Developers"
author: dave-bunten
tags:
  - software-testing
  - scientific-software
  - python
  - reproducibility
---

# Testing Scientific Software: A Practical Guide for Developers

{% include blog-post-intro.html %}

## Introduction

{% include figure.html image="images/magnifying-glass-and-bugs.png" width="40%" caption="Software testing helps us find bugs in our code which otherwise may go unseen." %}

<!-- excerpt start -->
**Scientific software plays a crucial role in research.**
When your software is used to analyze data, simulate models, or derive scientific conclusions, ensuring its correctness becomes critical.
**A small bug can have a significant impact on your results**, potentially invalidating months of work, or worse, causing the retraction of published research (for example: [see here](https://www.science.org/doi/10.1126/science.314.5807.1856)).
Fortunately, software testing can help minimize such risks, giving you more confidence in your code and a greater chance to catch issues early.

In this guide, we’ll walk through key types of software tests, practical advice for using popular testing tools like `pytest` and `doctest`, and how you can incorporate these into your scientific development workflow.
<!-- excerpt end -->

## Why testing matters in science

Imagine you’ve written a simulation that generates data based on a complex scientific model.
It works well under some conditions, but during peer review, a colleague finds a subtle bug.
This bug doesn't affect small data sets but produces significant errors on larger simulations.
The consequences?
You have to revise your paper, and time is lost fixing code.
There's also the possibility of bugs taking a long time to find (if ever) potentially leading to erroneous research.

__Consider: how can an audience know a software creates a reproducible outcome without  tests they can run and verify themselves?__
Testing your software upfront ensures that potential errors are caught early and your scientific conclusions remain valid and robust.
This article covers how to write code which automates the process of testing your software.

You may already have tests in place which haven't yet been automated.
If this is the case, consider integrating these with automated tools like those mentioned below to help create reproducible research software!


## Production code vs test code

{% include figure.html image="images/production-and-test-code.png" width="50%" caption="Software testing often involves two distinct sections of production or application code alongside testing code." %}

When working with software testing principles it can be helpful to distinguish __"production" or "application" code__ (code which provides some utility besides testing itself) from __"test" code__ (code which will be used to test the production or application code).
These are often (but not always) stored in separate directories or components within the project.

## Types of tests for scientific software

In software development, tests are typically categorized into several types.
**Each plays a unique role in ensuring your code functions as intended.**

{% include figure.html image="images/unit-test-code.png" width="50%" caption="Unit tests focus on testing an isolated set of functionality within your code." %}

- **Unit tests**: These validate small, isolated parts of your code, like functions or methods.
They are one of the most basic forms of testing but extremely valuable, ensuring the correctness of atomic units in your codebase.

{% include figure.html image="images/integration-test-code.png" width="50%" caption="Integration tests help ensure multiple software components act as expected together." %}

- **Integration tests**: Once your units of code are tested individually, **integration tests ensure software components work together**.
This is especially important in scientific software where different models, algorithms, and data structures interact.

{% include figure.html image="images/system-test-code.png" width="50%" caption="System or end-to-end tests might include those which check how external software interacts to form a cohesive output with your production code." %}

- **System / End-to-End tests**: These check the software from a user’s perspective.
For scientific software, this often means running entire workflows or simulations to make sure that everything from data input to output runs smoothly.

There are also many other different types of tests and testing philosophies which can be found here: [https://en.wikipedia.org/wiki/Software_testing#Categorization](https://en.wikipedia.org/wiki/Software_testing#Categorization).

## Testing in Python

Testing in Python is often performed using the built-in [`unittest`](https://docs.python.org/3/library/unittest.html) module or [`pytest`](https://github.com/pytest-dev/pytest) package.
There is also an additional built-in module, [`doctest`](https://docs.python.org/3/library/doctest.html), which allows you to test whether statements run as expected within [docstrings](https://peps.python.org/pep-0257/#what-is-a-docstring).

[`assert` statements](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) are a common part of writing tests in Python.
We can use `assert` to determine the truthiness of certain output (see below for an example).

```python
# we can use the assert statements to determine
# the truthiness (or lack thereof) of values.
assert 1 == 1
# returns True
assert 1 == 0
# returns False
```

The following examples will be added to a demonstrational repository which can be found here: [https://github.com/CU-DBMI/demo-python-software-testing](https://github.com/CU-DBMI/demo-python-software-testing)

## Introduction to `pytest`

{% include figure.html image="images/pytest.png" width="30%" %}

`pytest` is one of the most popular testing frameworks in Python.
An advantage to using `pytest` is that it is widely used, includes many different [plugins](https://docs.pytest.org/en/stable/reference/plugin_list.html) to extend functionality, and is relatively uncomplicated.

### Getting started with `pytest`

Consider the following project tree structure representing directories and files which is common to `pytest` projects.
Note the `tests` directory, which includes code dedicated to testing the `package_name` package module.
`pytest` seeks to run test code with the prefix of `test_` under the `tests` directory. 

```text
example_project
├── pyproject.toml
├── src
│   └── package_name
│       └── package_module.py
└── tests
    └── test_package_module.py
```

Just in case, make sure you install `pytest` into the project's environment management:

```bash
# use pip to install pytest into an existing environment
pip install pytest

# or, add pytest to a poetry environment
poetry add pytest
```

Assume we have a simple function within `package_module.py` which helps us understand whether a given integer is an even number.

```python
def is_even(number: int) -> bool:
    """
    Determines if a number is even.

    An even number is divisible by 2 without a remainder.

    Args:
        number (int):
          The number to check.

    Returns:
        bool:
          True if the number is even, False if it is odd.
    """
    return number % 2 == 0
```

Next, we could create a simple unit test within `test_package_module.py` for the `is_even()` function.

```python
def test_is_even():
    # assert that 2 is detected as an even number
    assert is_even(2)
```

Once we have the test written, we can use the `pytest` command through our project environment 

```bash
# run the `pytest` command through your terminal
pytest

# or, run `pytest` through a poetry environment
poetry run pytest
```

`pytest` will automatically find all files starting with test_ and run any functions inside them that start with test_.
It also produces concise output, helping you pinpoint errors quickly.
See below for an example of what the output might look like (we can see that the single test passed).

```text
============== test session starts ===============
platform darwin -- Python 3.11.9, pytest-8.3.3,
pluggy-1.5.0
rootdir: /example_project
configfile: pyproject.toml
collected 1 item

tests/test_package_module.py .             [100%]

=============== 1 passed in 0.00s ================
```

### Additional `pytest` features

- __Using temporary directories__: `pytest` allows for the creation of [temporary directories](https://docs.pytest.org/en/stable/how-to/tmp_path.html) where test data can be stored for each test run in isolation. This pattern can be helpful for times where you may need to generate and store test data for use among multiple tests.
- __Fixtures__: Use [`pytest` fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.html) to set up any necessary preconditions for your tests (like loading test datasets).
- __Parameterization__: If you need to test multiple inputs on the same function, `pytest` allows you to [parameterize](https://docs.pytest.org/en/stable/how-to/parametrize.html) your tests, running the same test function with different values.

## Using `doctest` for documentation and testing

{% include figure.html image="images/doctest.png" width="30%" %}

`doctest` is another tool which can be used for testing.
It serves a dual purpose: it embeds tests directly in your documentation by using interactive examples in docstrings.
This can be a lightweight way to share testable functionality within the documentation for your code.
Be cautious however; `doctests` are not generally suitable for large or complex testing.

### Writing doctests

A [`doctest`](https://docs.python.org/3/library/doctest.html) is simply an example of using a function, placed in docstrings.
The general pattern follows Python interactive terminal input (denoted by `>>>`) followed by the expected standard output (which sometimes may be truncated when dealing with large numbers or strings).

The `Examples` section of the docstring below demonstrates what a doctest for our earlier function might look like.

```python
def is_even(number: int) -> bool:
    """
    Determines if a number is even.

    An even number is divisible by 2 without a remainder.

    Args:
        number (int):
            The number to check.

    Returns:
        bool:
            True if the number is even, False if it is odd.

    Examples:
        >>> is_even(2)
        True
        >>> is_even(3)
        False
    """
    return number % 2 == 0
```

You can run always run doctests by adding the following to the same module which includes that code.

```python
if __name__ == "__main__":
    import doctest
    # run doctests within module
    doctest.testmod()
```


You also can run doctests through `pytest` by using the `--doctest-modules` command flag.
This can be helpful for areas where we don't want to use the [`if __name__ == "__main__":` pattern](https://docs.python.org/3/library/__main__.html).

```bash
# run the `pytest` command through your terminal
pytest --doctest-modules

# or, run `pytest` through a poetry environment
poetry run pytest --doctest-modules
```

The output might look like this:

```text
============== test session starts ===============
platform darwin -- Python 3.11.9, pytest-8.3.3,
pluggy-1.5.0
rootdir: /example_project
configfile: pyproject.toml
collected 2 items

src/package_name/module.py .               [ 50%]
tests/test_package_module.py .             [100%]

=============== 2 passed in 0.01s ================
```

This ensures that the examples in your documentation are always accurate and tested as part of your development cycle.

## Using Hypothesis for testing

{% include figure.html image="images/hypothesis.png" width="30%" %}

Using [Hypothesis](https://github.com/HypothesisWorks/hypothesis) for testing is a powerful approach for validating the correctness of scientific software.
By employing the Hypothesis library, you can perform property-based testing that generates test cases based on the characteristics of your input data.
This method allows you to test your functions against a broad range of inputs, ensuring that edge cases and unexpected scenarios are adequately handled.

### What is property-based testing?

[Property-based testing](https://hypothesis.works/articles/what-is-property-based-testing/) focuses on verifying that certain properties hold true for a wide range of input values, rather than checking specific outputs for predetermined inputs.
This contrasts with traditional example-based testing, where you specify the exact inputs and outputs (which can take time to imagine or construct individually).

### Getting started with hypothesis

To begin using Hypothesis in your project, you first need to install the library:

```bash
# use pip to install hypothesis into an existing environment
pip install hypothesis

# or, add hypothesis to a poetry environment
poetry add hypothesis
```

Once installed, you can write tests that utilize its capabilities. 
With Hypothesis, you can write a test that asserts properties about even numbers. For instance, all even numbers should return True when passed to the is_even function:

```python
from hypothesis import given
from hypothesis.strategies import integers

@given(integers())
def test_is_even(number):
    if number % 2 == 0:
        assert is_even(number)
    else:
        assert not is_even(number)
```

### Using the Hypothesis ghostwriter

Hypothesis also includes [a "ghostwriter" CLI](https://hypothesis.readthedocs.io/en/latest/ghostwriter.html) which can infer how to write Hypothesis tests given an object from Python code.
This can help automate the process of writing your test code or provide inspiration for how to construct your Hypothesis tests.
_Caveat emptor_: please be sure to review any code generated by the Hypothesis ghostwriter (it may not capture useful tests or edge cases).

Given the example code from the above, we could ask the Hypothesis ghostwriter to construct a test for the `is_even()` function as follows:

```bash
# run the command from your activated Python environment
hypothesis write package_name.module.is_even

# or, run through a poetry environment
poetry run hypothesis write package_name.module.is_even
```

The output looks similar but not quite the same as the Hypothesis test we shared above.
Note that the test name implies and itself employs a technique called [fuzzing, or fuzz testing](https://en.wikipedia.org/wiki/Fuzzing), which is used to help determine where software might break.

```python
# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import package_name.module
from hypothesis import given, strategies as st


@given(number=st.integers())
def test_fuzz_is_even(number: int) -> None:
    package_name.module.is_even(number=number)
```

## Benefits of using Hypothesis

Below are just a few of the benefits you'll find with using Hypothesis:

- ___Discovering Edge Cases___: Hypothesis automatically generates diverse input scenarios, including edge cases that might be overlooked in example-based tests.
- ___Reduced Boilerplate Code___: You can focus on the properties of your functions rather than writing extensive examples for every possible case.
- ___Increased Confidence___: By validating the behavior of your code against a broader set of inputs, you can be more confident that your scientific software will behave correctly in practice.

## Best practices for scientific software testing

Now that you understand some testing tools, here are some best practices for testing scientific software:

- __Write tests early__: Incorporate testing from the start. 
This is crucial, especially when your software are prone to evolving.

- __Test small and test often__: Focus on unit tests that cover individual functions and methods.
Catching small errors early prevents larger problems down the line.

- __Use realistic test data__: When testing your functions, prioritize test data that reflects the real-world conditions where your software will be applied. Secondarily, use "mock" or synthetically created data when the real data are too large or complex to test quickly. For more on this topic, see ["Prefer Realism Over Isolation" from the Test Doubles chapter in the book Software Engineering at Google](https://abseil.io/resources/swe-book/html/ch13.html#prefer_realism_over_isolation).

- __Automate your tests__: Use tools like `pytest` and Continuous Integration (CI) services (e.g., GitHub Actions, GitLab CI) to run your tests automatically on every commit.
This ensures that every update is tested, and bugs are identified early.

- __Combine different tests approaches to help diversify your test coverage__: Both are essential in scientific software.
While unit tests help you pinpoint specific issues, integration tests validate that modules work correctly when combined.

## Conclusion

Testing is a vital part of developing scientific software. By using tools like `pytest`, `doctest`, and Hypothesis, you can automate the testing process and ensure your codebase remains robust.
Investing time in writing good tests upfront will save you countless hours in debugging and re-running experiments.

Remember, the correctness of your code is directly tied to the validity of your scientific results.
By adopting a solid testing strategy, you're taking a significant step toward ensuring reproducible, reliable, and impactful scientific research.

Now, you’re ready to ensure your scientific code is as solid as your research!

If interested, be sure to reference the related demonstrational repository with code from this blog post which can be found here: [https://github.com/CU-DBMI/demo-python-software-testing](https://github.com/CU-DBMI/demo-python-software-testing)

## Additional material

- Eisty, N. U., & Carver, J. C. (2022). Testing Research Software: A Survey. Empirical Software Engineering, 27(6), 138. [https://doi.org/10.1007/s10664-022-10184-9](https://doi.org/10.1007/s10664-022-10184-9)
- Kanewala, U., & Bieman, J. M. (2018). Testing Scientific Software: A Systematic Literature Review (arXiv:1804.01954). arXiv. [http://arxiv.org/abs/1804.01954](http://arxiv.org/abs/1804.01954)
- Bender, A. (2020) Testing Overview. Winters, T., Manshreck, T., & Wright, H. Software engineering at Google: Lessons learned from programming over time. [https://abseil.io/resources/swe-book/html/ch11.html](https://abseil.io/resources/swe-book/html/ch11.html)
- [CU-DBMI SET Blog Post: Uncovering Code Coverage: Ensuring Software Reliability with Comprehensive Testing](https://cu-dbmi.github.io/set-website/2024/07/28/Uncovering-Code-Coverage.html)
