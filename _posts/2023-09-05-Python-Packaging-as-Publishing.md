---
title: "Tip of the Week: Python Packaging as Publishing"
author: dave-bunten
tags:
  - tip-of-the-week
  - software
  - Python
  - packaging
  - publishing
  - software-design
  - understandability
  - environment-management
---

# Tip of the Week: Python Packaging as Publishing

{% include tip-of-the-week-intro.html %}

<!-- excerpt start -->

Python packaging is the craft of preparing for and reaching distribution of your Python work to wider audiences. Following conventions for packaging help your software work become more understandable, trustworthy, and connected (to others and their work). Taking advantage of common packaging practices also strengthens our collective superpowers: collaboration. This post will cover preparation aspects of packaging, readying software work for wider distribution.

<!-- excerpt end -->

__TLDR (too long, didn't read);__

Use Pythonic packaging tools and techniques to help avoid [code decay](https://en.wikipedia.org/wiki/Software_rot) and unwanted [code smells](https://en.wikipedia.org/wiki/Code_smell) and increase your development velocity. Increase understanding with unsurprising directory structures like those exhibited in [`pypa/sampleproject`](https://github.com/pypa/sampleproject) or [`scientific-python/cookie`](https://github.com/scientific-python/cookie). Enhance trust by being authentic on source control systems like GitHub ([by customizing your profile](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/about-your-profile)), staying up to date with the [latest supported versions of Python](https://devguide.python.org/versions/), and using security linting tools like [`PyCQA/bandit`](https://github.com/PyCQA/bandit) through [visible + automated GitHub Actions ✅ checks](https://cu-dbmi.github.io/set-website/2023/03/15/Automate-Software-Workflows-with-Github-Actions.html). Connect your projects to others using [`CITATION.cff` files](https://citation-file-format.github.io/), [`CONTRIBUTING.md` files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors), and using environment + packaging tools like [`poetry`](https://python-poetry.org/docs/) to help others reproduce the same results from your code.

## Why practice packaging?

{% include figure.html image="images/text-vs-book.png" caption="How are a page with some text and a book different?"  %}

The practice of Python packaging efforts is similar to that of publishing a book. Consider how a bag of text is different from a book. How and _why_ are these things different?

- A book has commonly understood sequencing of content (i.e. copyright page, then title page, then body content pages...).
- A book often cites references and acknowledges other work explicitly.
- A book undergoes a manufacturing process which allows the text to be received in many places the same way.

{% include figure.html image="images/python-packaging-to-audience.png" caption="Code undergoing packaging to achieve understanding, trust, and connection for an audience."  %}

These can be thought of metaphors when it comes to packaging in Python. Books have a smell which sometimes comes from how it was stored, treated, or maintained. While there are pleasant book smells, they might also smell soggy from being left in the rain or stored without maintenance for too long. Just like books, software can sometimes have negative [code smells](https://en.wikipedia.org/wiki/Code_smell) indicating a lack of care or less sustainable condition. Following good packaging practices helps to avoid unwanted code smells while increasing development velocity, maintainability of software through understandability, trustworthiness of the content, and connection to other projects.

{% capture inner_source_alert %}
Note: these techniques can also work just as well for [inner source](https://en.wikipedia.org/wiki/Inner_source) collaboration (private or proprietary development within organizations)! Don't hesitate to use these on projects which may not be public facing in order to make development and maintenance easier (if only for you).
{% endcapture %}

{%
  include alert.html
  type="tip"
  content=inner_source_alert
%}

{% capture python_packages_info %}

__"Wait, what are Python packages?"__

```text
my_package/
│   __init__.py
│   module_a.py
│   module_b.py
```

A Python __package__ is a collection of modules (`.py` files) that usually include an "initialization file" `__init__.py`. This post will cover the craft of __packaging__ which can include one or many _packages_.
{% endcapture %}

{%
  include alert.html
  type="help"
  content=python_packages_info
%}

## Understanding: common directory structures

```bash
project_directory
├── README.md
├── LICENSE.txt
├── pyproject.toml
├── docs
│   └── source
│       └── index.md
├── src
│   └── package_name
│       └── __init__.py
│       └── module_a.py
└── tests
    └── __init__.py
    └── test_module_a.py
```

Python Packaging today generally assumes a specific directory design.
Following this convention generally improves the __understanding__ of your code. We'll cover each of these below.

### Project root files

```bash
project_directory
├── README.md
├── LICENSE.txt
├── pyproject.toml
│ ...
```

- The __`README.md` file__ is a [markdown](https://en.wikipedia.org/wiki/Markdown) file with documentation including project goals and other short notes about installation, development, or usage. The `README.md` file is akin to a book jacket blurb which quickly tells the audience what the book will be about.
- The __`LICENSE.txt` file__ is a text file which indicates licensing details for the project. It often includes information about how it may be used and protects the authors in disputes. The `LICENSE.txt` file can be thought of like a book's copyright page. See [https://choosealicense.com/](https://choosealicense.com/) for more details on selecting an open source license.
- The __`pyproject.toml` file__ is a Python-specific [TOML](https://en.wikipedia.org/wiki/TOML) file which helps organize how the project is used and built for wider distribution. The `pyproject.toml` file is similar to a book's table of contents, index, and printing or production specification.

### Project sub-directories

```bash
project_directory
│ ...
├── docs
│   └── source
│       └── index.md
├── src
│   └── package_name
│       └── __init__.py
│       └── module_a.py
└── tests
    └── __init__.py
    └── test_module_a.py
```

- The __`docs` directory__ is used for in-depth documentation and related documentation build code (for example, when building documentation websites, aka "docsites"). The `docs` directory includes information similar to a book's "study guide", providing content surrounding how to best make use of and understand the content found within.
- The __`src` directory__  includes primary source code for use in the project. Python projects generally use a nested package directory with modules and sub-packages. The `src` directory is like a book's body or general content (perhaps thinking of modules as chapters or sections of related ideas).
- The __`tests` directory__ includes testing code for validating functionality of code found in the `src` directory. The above follows [pytest](https://docs.pytest.org/) conventions. The `tests` directory is for code which acts like a book's early reviewers or editors, making sure that if you change things in `src` the impacts remain as expected.

### Common directory structure examples

The Python directory structure described above can be witnessed in the wild from the following resources. These can serve as a great resource for starting or adjusting your own work.

- [`pypa/sampleproject`](https://github.com/pypa/sampleproject)
- [`scientific-python/cookie`](https://github.com/scientific-python/cookie)
- [`microsoft/python-package-template`](https://github.com/microsoft/python-package-template)

## Trust: building audience confidence

{% include figure.html image="images/package-audience-trust.png" caption="How much does your audience trust your work?."  %}

Building an understandable body of content helps tremendously with audience trust. What else can we do to enhance project trust? The following elements can help improve an audience's trust in packaged Python work.

### Source control authenticity

{% include figure.html image="images/source-control-authenticity.png" caption="Comparing the difference between a generic or anonymous user and one with greater authenticity."  %}

Be authentic! Fill out your profile to help your audience know the author and why you do what you do. See here for [GitHub's documentation on filling out your profile](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/about-your-profile). Doing this may seem irrelevant but can go a long way to making technical work more relatable.

- Add a profile picture of yourself or something fun.
- Set your profile description to information which is both professionally accurate and unique to you.
- Show or link to work which you feel may be relevant or exciting to those in your audience.

### Staying up to date with supported Python releases

{% include figure.html image="images/python-version-status.png" caption="Major Python releases and their support status."  %}

Use Python versions which are supported (this changes over time).
Python versions which are end-of-life may be difficult to support and are a sign of [code decay](https://en.wikipedia.org/wiki/Software_rot) for projects. Specify the version of Python which is compatiable with your project by using environment specifications such as `pyproject.toml` files and related packaging tools (more on this below).

- See here for [updated information on Python version status](https://devguide.python.org/versions/).
- Staying up to date with supported releases oftentimes can result in performance or other similar benefits (later versions usually include improvements!).

### Security linting and visible checks with GitHub Actions

{% include figure.html image="images/package-magnifying-glass.png" caption="Make an effort to inspect your package for known security issues."  %}

Use security vulnerability linters to help prevent undesirable or risky processing for your audience. Doing this both practical to avoid issues and conveys that you care about those using your package!

- [`PyCQA/bandit``](https://github.com/PyCQA/bandit): checks Python code
- [`pyupio/safety``](https://github.com/pyupio/safety): checks Python dependencies
- [`gitleaks`](https://github.com/gitleaks/gitleaks): checks for sensitive passwords, keys, or tokens

{% include figure.html image="images/gh-actions-checkmark.png" caption="The green checkmark from successful GitHub Actions runs can offer a sense of reassurance to your audience."  %}

Combining GitHub actions with security linters and tests from your software validation suite can add an observable ✅ for your project.
This provides the audience with a sense that you're transparently testing and sharing results of those tests.

- See [GitHub's documentation on this topic for more information](https://docs.github.com/en/actions).
- See also [the DBMI Software Engineering Team's blog post: "Automate Software Workflows with Github Actions"](https://cu-dbmi.github.io/set-website/2023/03/15/Automate-Software-Workflows-with-Github-Actions.html)

## Connection: personal and inter-package relationships

{% include figure.html image="images/package-connections.png" caption="How does your package connect with other work and people?"  %}

Understandability and trust set the stage for your project's __connection__ to other people and projects. What can we do to facilitate connection with our project? Use the following techniques to help enhance your project's connection to others and their work.

### Acknowledging authors and referenced work with CITATION.cff

{% include figure.html image="images/citation-cff-icon.png" %}

Add a __`CITATION.cff`__ file to your project root in order to describe project relationships and acknowledgements in a standardized way. The [CFF format](https://citation-file-format.github.io/) is also [GitHub compatible](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files), making it easier to cite your project.

- This is similar to a book's credits, acknowledgements, dedication, and author information sections.
- See here for a [`CITATION.cff` file generator (and updater)](https://citation-file-format.github.io/cff-initializer-javascript/#/).

### Reaching collaborators using CONTRIBUTING.md

{% include figure.html image="images/contributing-file-with-handshake.png" caption="CONTRIBUTING.md documents can help you collaborate with others."  %}

Provide a __`CONTRIBUTING.md`__ file to your project root so as to make clear support details, development guidance, code of conduct, and overall documentation surrounding how the project is governed.

- See GitHub's documentation on ["Setting guidelines for repository contributors"](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- See opensource.guide's section on ["Writing your contributing guidelines"](https://opensource.guide/starting-a-project/#writing-your-contributing-guidelines)

### Environment management reproducibility as connected project reality

{% include figure.html image="images/environment-management-tooling.png" caption="Environment and packaging managers can help you connect with your audience."  %}

Code without an environment specification is difficult to run in a consistent way. This can lead to "works on my machine" scenarios where different things happen for different people, reducing the chance that people can connect with a shared reality for how your code should be used.

> __"But why do we have to switch the way we do things?"__
> _We've always been switching approaches (software approaches evolve over time)!_ A brief history of Python environment and packaging tooling:
>
> 1. __`distutils`, `easy_install` + `setup.py`__ <br>(primarily used during 1990's - early 2000's)
> 1. __`pip`, `setup.py` + `requirements.txt`__ <br>(primarily used during late 2000's - early 2010's)
> 1. __`poetry` + `pyproject.toml`__ <br>(began use around late 2010's - ongoing)

#### Using Python `poetry` for environment and packaging management

{% include figure.html image="images/poetry-icon.png" %}

[Poetry](https://github.com/python-poetry/poetry) is one Pythonic environment and packaging manager which can help increase reproducibility using `pyproject.toml` files. It's one of many other alternatives such as [`hatch`](https://hatch.pypa.io/latest/) and [`pipenv`](https://pipenv.pypa.io/en/latest/).

##### `poetry` directory structure template use

```bash
user@machine % poetry new --name=package_name --src .
Created package package_name in .

user@machine % tree .
.
├── README.md
├── pyproject.toml
├── src
│   └── package_name
│       └── __init__.py
└── tests
    └── __init__.py
```

After installation, Poetry gives us the ability to initialize a directory structure similar to what we presented earlier by using the [`poetry new ...` command](https://python-poetry.org/docs/cli/#new). If you'd like a more interactive version of the same, use the [`poetry init` command](https://python-poetry.org/docs/cli/#init) to fill out various sections of your project with detailed information.

##### `poetry` format for project `pyproject.toml`

```toml
# pyproject.toml
[tool.poetry]
name = "package-name"
version = "0.1.0"
description = ""
authors = ["username <email@address>"]
readme = "README.md"
packages = [{include = "package_name", from = "src"}]

[tool.poetry.dependencies]
python = "^3.9"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Using the `poetry new ...` command also initializes the content of our [`pyproject.toml` file with opinionated details](https://python-poetry.org/docs/pyproject#the-pyprojecttoml-file) (following the recommendation from earlier in the article regarding declared Python version specification).

##### `poetry` dependency management

```bash
user@machine % poetry add pandas

Creating virtualenv package-name-1STl06GY-py3.9 in /pypoetry/virtualenvs
Using version ^2.1.0 for pandas

...

Writing lock file
```

We can add dependencies directly using the [`poetry add ...` command](https://python-poetry.org/docs/cli/#add). This command also provides the possibility of using a `group` flag (for example `poetry add pytest --group testing`) to help organize and distinguish multiple sets of dependencies.

- A local virtual environment is managed for us automatically.
- [A `poetry.lock` file](https://python-poetry.org/docs/libraries/#lock-file) is written when the dependencies are installed to help ensure the version you installed today will be what's used on other machines.
- The `poetry.lock` file helps ensure reproducibility when dealing with dependency version ranges (where otherwise we may end up using different versions which match the dependency ranges but observe different results).

##### Running Python from the context of `poetry` environments

```bash
% poetry run python -c "import pandas; print(pandas.__version__)"

2.1.0
```

We can invoke the virtual environment directly using the [`poetry run ...` command](https://python-poetry.org/docs/cli/#run).

- This allows us to quickly run code through the context of the project's environment.
- Poetry can automatically switch between multiple environments based on the local directory structure.
- We can also the environment as a "shell" (similar to virtualenv's `activate`) with the [`poetry shell` command](https://python-poetry.org/docs/cli/#shell) which enables us to leverage a dynamic session in the context of the `poetry` environment.

##### Building source code with `poetry`

```bash
% pip install git+https://github.com/project/package_name
```

Even if we don't reach wider distribution on PyPI or elsewhere, source code managed by `pyproject.toml` and `poetry` can be used for "manual" distribution (with reproducible results) from GitHub repositories. When we're ready to distribute pre-built packages on other networks we can also use the following:

```bash
% poetry build

Building package-name (0.1.0)
  - Building sdist
  - Built package_name-0.1.0.tar.gz
  - Building wheel
  - Built package_name-0.1.0-py3-none-any.whl
```

Poetry readies source-code and pre-compiled versions of our code for distribution platforms like PyPI by using the [`poetry build ...` command](https://python-poetry.org/docs/cli/#build). We'll cover more on these files and distribution steps with a later post!
