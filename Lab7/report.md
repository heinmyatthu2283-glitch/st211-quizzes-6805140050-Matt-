# Lab 7 — Code Coverage and Quality Metrics

**Name:** Than Htike Aung  
**Student ID:** 6805140050  
**Course:** 192-211 Automated Software Testing

## Objective

The objective of this lab was to use `pytest-cov` to measure statement and branch coverage, identify gaps in testing, and enforce a minimum coverage threshold.

## Results

| Exercise | Result | Observation |
| --- | --- | --- |
| Initial shipping tests | 2 passed, 73% statement coverage | The terminal and HTML reports showed 3 missing statements out of 11. |
| Complete shipping tests | 5 passed, 100% coverage | New tests covered invalid weights, the heavy-package surcharge, and free-shipping eligibility. |
| Initial access tests | 2 passed, 100% coverage | Both outcomes of the `if` statement ran. Two combinations of user role and active status still needed testing. |
| Complete access tests | 4 passed, 100% coverage | The tests verified all four combinations of role and active status. |
| Minimum coverage check | 70.59% coverage against an 80% minimum | Both starter tests passed, but the command failed because coverage was below the threshold. |
| Coverage exclusion | `utils.py` printed `42` and reported 2 statements at 100% coverage | `# pragma: no cover` excluded the `if __name__ == "__main__"` block. |
| Weak assertion demo | 1 passed, 59% coverage | The test called `calculate_shipping(10)`, and `assert True` passed regardless of the returned price. |

## Review Questions

### 1. What is the difference between line coverage and branch coverage?

Line coverage measures which executable statements ran. Branch coverage checks whether each possible outcome of a decision was taken, such as both the true and false outcomes of an `if` statement.

### 2. Why can a test achieve coverage while testing nothing?

Coverage records which code ran. In `test_misleading.py`, calling `calculate_shipping(10)` earned coverage, but the test never verified that the returned price was `20`.

### 3. What does `--cov-fail-under` do, and why is it useful in CI?

`--cov-fail-under` makes the test command fail when coverage falls below a specified percentage, even if every test passes. In continuous integration, this lets the team enforce a minimum coverage requirement automatically.

## Conclusion

Coverage reports helped me locate untested shipping logic. The access exercise showed that adding tests for two more input combinations improved the test suite even though the coverage stayed at 100%. Meaningful assertions are what verify that the code produces the expected result.