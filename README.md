About
---

Welcome to "let's explore pytest", which includes several pytest
examples. pytest is a testing framework that can be used to test Python code,
amongst other things, and lives at www.pytest.org. Python 3 is used exclusively
in this repository, though pytest can test Python 2 software.

These examples assume you are familiar with your shell or commandline, and are
able to set up your environment appropriately.

Environment
---

You will need (the versions we are using are in parentheses):

 - Python 3 (3.6.2)

 - pytest (3.2.1)

 - pytest-mock (1.6.0)

 - pytest-xdist (1.17.1)

The conda environment file `conda_environment.yml` is provided, which all
examples are designed to use.

Table of contents
---

Each example contains multiple `pytest` Python scripts.

 1. *Introductory examples*
    - Introduces pytest.
    - pytest reports failing tests, and has informative output.
    - pytest searches for tests automatically.

 2. *Fixtures, parameterisation, and parallelisation* (requires example 1)
    - Fixtures (decorated with `@pytest.fixture()`) are blocks of functionality
      that allow tests to be written in a modular way.
    - Fixtures are run when the test is run, and their output is passed to the
      test.
    - Fixtures can be used to parameterise tests, reducing code
      duplication. Each test is run individually of the others.
    - Parameterised tests run well in parallel (but be careful when testing
      software that itself runs in parallel!)

 3. *Testing software in isolation using mocking* (requires example 2)
