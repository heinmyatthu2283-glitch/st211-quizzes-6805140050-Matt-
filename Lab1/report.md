# Review Questions

## 1. What naming rule must a test function follow for pytest to find it?

Test functions must start with test_ (for example, def test_addition()). Additionally, test files must either start with test_ or end with _test.py (for example, test_first.py or first_test.py).

## 2. What does the AAA pattern stand for?

The AAA pattern stands for Arrange, Act, and Assert.

Arrange involves setting up the test data, variables, and initial conditions required for the test.

Act involves calling the function or executing the specific code block being tested.

Assert involves checking and verifying that the actual result produced matches the expected outcome.

## 3. How do you test that a function correctly raises an exception?

I use the with pytest.raises(...) context manager provided by pytest. You pass the expected exception class (such as ValueError) into pytest.raises(), and optionally supply a match parameter to check for specific error message strings (such as with pytest.raises(ValueError, match="Cannot divide by zero"):).