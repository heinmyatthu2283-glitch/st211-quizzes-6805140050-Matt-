# Lab 2 Review Questions

## 1. Why must tests be independent of each other?

I ensure my tests are independent of each other so that the execution or outcome of one test never impacts another. By isolating my tests from shared state or side effects, I can run them in any order without risking cascade failures where a single broken test causes unrelated tests to fail. This approach makes my test suite far more reliable, easier to debug, and suitable for parallel execution.

## 2. A function accepts scores 0-100. What boundary values should you test?

When testing a score range from 0 to 100, I test values directly at the extreme ends of the valid range as well as those immediately outside of it. Specifically, I test the valid lower boundary (0), the valid upper boundary (100), values just inside the valid limits (1 and 99), and invalid boundary values just outside the allowed range (-1 and 101).

## 3. What is the difference between positive and negative testing?

In positive testing, I verify that the system behaves correctly when given valid inputs and executed under standard operational scenarios. In negative testing, I check how the system handles invalid, unexpected, or out-of-bounds inputs to ensure it fails gracefully, returns appropriate error messages, or raises expected exceptions without crashing.