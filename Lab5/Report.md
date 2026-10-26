# Lab 5 Review Questions

## 1. If you stack parametrize with 3 values and 4 values, how many tests run?

When I stack two parametrize decorators with 3 and 4 values, pytest generates a cross-product of both parameter sets, resulting in 12 total test runs ($3 \times 4 = 12$).

## 2. Why add custom IDs to parameterized cases?

I add custom IDs to make failure messages immediately readable during test runs. A descriptive ID like `[free]` instantly identifies the specific scenario that failed, whereas a generic default like `[case2]` gives no context.

## 3. What is the difference between @pytest.mark.parametrize on a test and fixture(params=...) on a fixture?

I use `@pytest.mark.parametrize` to affect only the single test function it decorates. In contrast, a parametrized fixture affects every test that uses it, meaning adding a new parameter value to the fixture automatically expands test coverage across the entire test suite.

## 4. What advantage does data-driven testing give a non-programmer on the QA team?

Data-driven testing allows non-programmers on my QA team to add new test cases simply by editing a CSV or JSON file in a spreadsheet, enabling them to expand test coverage without writing any Python code.