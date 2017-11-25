Fixtures
---

In the previous example, we found that pytest collects tests intelligently, but
we require a mechanism for defining a series of similar tests. Firstly however,
we refactor `binary_converter.py` into `binary_converter_single.py`, which will
be used as the basis for discussion in this example. The `testCase` dictionary
defines the parameters for the test, including the input and the output we
expect to result.

The `binary_converter_single.py` is refactored into the
`binary_converter_fixture.py` example, which introduces the concept of
fixtures. The `testCase` dictionary is taken out of the `test_my_converter`
function, and is defined as a function itself. The `pytest.fixture()`
decorator is applied to it (using `@` notation).

Fixtures are gathered along with tests when pytest imports a library, and are
run when a test function, in this case `test_my_converter`, includes them as an
argument (note that `test_my_converter` did not take an argument in
`binary_converter_single`). The `test_my_converter` function is then run, with
`testCase` defined by the return value of the fixture. Basically, pytest's
logic is as follows:

 1. Identifies `test_my_converter` as a test to run.

 2. Runs all fixtures required by `test_my_converter`, in this case `testCase`.

 3. Runs `test_my_converter` using the output of `testCase`.

 4. `integer_to_binary` is called by `test_my_converter`, because
    `integer_to_binary` is the function we are testing.

 5. pytest then reports the results.

Try running the test for yourself with `pytest binary_converter_fixture.py`.

For more on fixtures, visit pytest's excellent documentation at www.pytest.org,
or continue following these examples.

Test parameterisation
---

Fixtures are used to parameterise tests in `binary_converter_multiple`, which
defines a series of similar tests. The `params` keyword for the
`pytest.fixture` decorator determines the different parameters the test case is
called with. In this case, three different tests are defined with three
different parameter sets. pytest will call this fixture three times with each
parameter, and will run each test that depends on this fixture once for each
fixture value. (If you were to define a test that used multiple fixtures, lets
say one with two parameters and one with four parameters, that test would run
eight times to satisfy every parameter combination).

Here's the output (with `--verbose`):

```
$ pytest binary_converter_multiple.py --verbose
============================= test session starts =============================
<snip>
collected 3 items

binary_converter_multiple.py::test_my_converter[testCase0] PASSED
binary_converter_multiple.py::test_my_converter[testCase1] FAILED
binary_converter_multiple.py::test_my_converter[testCase2] PASSED

================================== FAILURES ===================================
________________________ test_my_converter[testCase1] _________________________

testCase = {'expectedResult': '0', 'input': 5}

    def test_my_converter(testCase):
>       assert integer_to_binary(testCase["input"]) == testCase["expectedResult"]
E       assert '101' == '0'
E         - 101
E         + 0

binary_converter_multiple.py:22: AssertionError
===================== 1 failed, 2 passed in 0.05 seconds ======================
```

From the output, it is clear that three tests have been generated from the
three parameter sets defined in the fixture. Note that, though the second test
failed, the other tests still ran! This is useful information for diagnosing
problems in code. If you really want pytest to fail fast, you can still achieve
this using `--exitfirst`:

```
$ pytest binary_converter_multiple.py --verbose --exitfirst
============================= test session starts =============================
<snip>
collected 3 items

binary_converter_multiple.py::test_my_converter[testCase0] PASSED
binary_converter_multiple.py::test_my_converter[testCase1] FAILED

================================== FAILURES ===================================
________________________ test_my_converter[testCase1] _________________________

testCase = {'expectedResult': '0', 'input': 5}

    def test_my_converter(testCase):
>       assert integer_to_binary(testCase["input"]) == testCase["expectedResult"]
E       assert '101' == '0'
E         - 101
E         + 0

binary_converter_multiple.py:22: AssertionError
!!!!!!!!!!!!!!!!!!! Interrupted: stopping after 1 failures !!!!!!!!!!!!!!!!!!!!
===================== 1 failed, 1 passed in 0.11 seconds ======================
```

Running tests in parallel
---

Running three tests is a pretty quick job, but running many tests one at a time
can severely slow execution. The `xdist` pytest plugin allows tests to be
distributed to other cores on your computer, or to other computers on a
network, resulting in a faster test execution (usually). As a simple example,
calling pytest with the `-n auto` flag and argument will cause pytest to search
for available cores on your computer, and distribute tests to each of
them. (You can also use a number instead of `auto` if you know better).

You should be wary of the "gotchas" involved with parallel testing, as the
software you are testing may also run in parallel, adding to the competition
for compute resources, resulting in overall slower test performance. There is
no free lunch.
