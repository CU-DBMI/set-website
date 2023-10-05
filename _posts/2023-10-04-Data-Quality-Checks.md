---
title: "Tip of the Week: Data Quality Checks and Validation Testing"
author: dave-bunten
tags:
  - tip-of-the-week
  - software
  - Python
  - data-quality
  - data-development
  - data-testing
  - testing
  - analytics-engineering
---

# Tip of the Week: Data Quality Checks and Validation Testing

{% include tip-of-the-week-intro.html %}

<!-- excerpt start -->

<!-- excerpt end -->

Outline:

- Covering data quality tools and techniques to help decrease errors and increase development velocity.

- Data verification testing
  - [Great Expectations](https://github.com/great-expectations/great_expectations)
  - [Assertr](https://github.com/ropensci/assertr/)

- Data schema testing
  - [Pandera](https://github.com/unionai-oss/pandera)
  - [JSONschema](https://github.com/python-jsonschema/jsonschema)

- Data source testing ([link](https://en.wikipedia.org/wiki/Shift-left_testing))
  - [DVC](https://github.com/iterative/dvc)
  - [Liquibase](https://github.com/liquibase/liquibase)
    - [Database-as-code](https://speakerdeck.com/tastapod/arent-we-forgetting-someone)

__TLDR (too long, didn't read);__

## Data Quality Validation via Software Tests

```mermaid!
flowchart LR
    subgraph local ["Data Quality Validation"]
        direction LR

            input_data[("Input Data")]
            met_specification1{"Met\nspecs?"}
            process_data["Data processing"]
            met_specification2{"Met \nspecs?"}
            output_data[("Output Data")]
    end

    input_data --> met_specification1
    met_specification1 --> process_data
    process_data --> met_specification2
    met_specification2 --> output_data
```

_Diagram showing input, in-process data, and output data as a workflow._

Data orientated software development can benefit from a specialized focus on varying aspects of data quality.
We can use software-based testing techniques to validate certain qualities of the data in order to meet a declarative standard (where one doesn't need to guess or rediscover known issues).
These come in a number of forms and generally follow existing [software testing](https://en.wikipedia.org/wiki/Software_testing) approaches.
This article will cover just a few tools and techniques for addressing data quality validation testing.

## Data Quality Testing Concepts

### Hoare Triple

```mermaid!
flowchart LR
    subgraph local ["Data Workflow as Hoare Triple"]
        direction LR
            input_data[("Input Data\n(P - precondition)")]
            process_data["Data processing\n(C - command)"]
            output_data[("Output Data\n(Q - postcondition)")]
    end

    input_data --> process_data --> output_data
```

One concept we'll use to present these ideas is [_Hoare logic_](https://en.wikipedia.org/wiki/Hoare_logic), which is a system for reasoning on [software correctness](https://en.wikipedia.org/wiki/Correctness_(computer_science)).
Hoare logic includes the idea of a [Hoare triple](https://en.wikipedia.org/wiki/Hoare_logic#Hoare_triple) ($ {\displaystyle \{P\}C\{Q\}} $) where $ {\displaystyle \{P\}} $ is an assertion of precondition, $ {\displaystyle \ C} $ is a command, and $ {\displaystyle \{Q\}} $ is a postcondition assertion.
Software development using data often entails (sometimes assumed) assertions of precondition from data sources, a transformation or command which changes the data, and a (sometimes assumed) assertion of postcondition in a data output or result.

### Design by Contract

```mermaid!
flowchart LR
    subgraph local ["Data Testing through Design by Contract over Hoare Triple"]
        direction LR
        subgraph hoare_triple ["Hoare Triple"]
            direction LR
            input_data[("Input Data\n(P - precondition)")]
            
            process_data["Data processing\n(C - command)"]
            
            output_data[("Output Data\n(Q - postcondition)")]
        end
        subgraph dbc ["Design by Contract"]
            direction LR
            met_specification1{"Met\nspecs?"}
            contract1(["Contract(s)"])
            met_specification2{"Met \nspecs?"}
            contract2(["Contract(s)"])
        end
    end

    input_data --> met_specification1
    met_specification1 --> process_data
    process_data --> met_specification2
    met_specification2 --> output_data
    contract1 --> met_specification1
    contract2 --> met_specification2

```

Hoare logic and Software correctness help describe [Design by contract (DbC)](https://en.wikipedia.org/wiki/Design_by_contract), a software approach involving the formal specification of "contracts" which help ensure we meet our intended goals.
DbC helps describe how to create assertions when proceeding through Hoare triplet states for data.
These concepts provide a framework for thinking about the tools mentioned below.

## Data Condition Verification

```mermaid!
flowchart LR

```

We often need to verify a certain conditions surrounding data in order to ensure it meets minimum standards.
The word "condition" is used here to group together loose or very specific qualities of the data.
These conditions often are implied by software which will eventually use the data, which can emit warnings or errors when they find the data does not meet these standards.
___We can avoid these challenges by creating contracts for our data to verify the conditions of the result before it reaches later stages.___

Examples of these conditions might include:

- The dataset has no null values.
- The dataset has no more than 3 columns.
- The dataset has a column called `numbers` which includes numbers in the range of 0-10.

### Data Condition Verification - Great Expectations

```python
"""
Example of using Great Expectations
Referenced with modifications from: 
https://docs.greatexpectations.io/docs/tutorials/quickstart/
"""
import great_expectations as gx

# get gx DataContext
# see: https://docs.greatexpectations.io/docs/terms/data_context
context = gx.get_context()

# set a context data source 
# see: https://docs.greatexpectations.io/docs/terms/datasource
validator = context.sources.pandas_default.read_csv(
    "https://raw.githubusercontent.com/great-expectations/gx_tutorials/main/data/yellow_tripdata_sample_2019-01.csv"
)

# add and save expectations 
# see: https://docs.greatexpectations.io/docs/terms/expectation
validator.expect_column_values_to_not_be_null("pickup_datetime")
validator.expect_column_values_to_be_between("passenger_count", auto=True)
validator.save_expectation_suite()

# checkpoint the context with the validator
# see: https://docs.greatexpectations.io/docs/terms/checkpoint
checkpoint = context.add_or_update_checkpoint(
    name="my_quickstart_checkpoint",
    validator=validator,
)

# gather checkpoint expectation results
checkpoint_result = checkpoint.run()

# show the checkpoint expectation results
context.view_validation_result(checkpoint_result)
```

[Great Expectations](https://github.com/great-expectations/great_expectations) provides data condtion contract verification features through the use of ["expectations"](https://greatexpectations.io/expectations/) about the data involved.
These expectations act as a standardized way to define and validate the condition of the data in the same way across different datasets or projects.
See the above example for a quick code reference of how these work.

{% include figure.html image="images/text-vs-book.png" caption="How are a page with some text and a book different?"  %}
