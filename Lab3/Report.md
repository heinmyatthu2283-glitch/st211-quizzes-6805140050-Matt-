# Lab Review Questions

## 1. Why use pytest.approx when comparing floats?

I use `pytest.approx` when comparing floating-point numbers because floating-point arithmetic in computers often produces tiny rounding errors due to binary representation limitations. Comparing floats directly with standard equality operators can cause tests to fail unexpectedly over infinitesimal differences like `0.1 + 0.2 != 0.3`. By using `pytest.approx`, I can compare floating-point values within a reasonable tolerance threshold, ensuring my assertions pass reliably.

## 2. What is the difference between skip and xfail?

I use `@pytest.mark.skip` when I want pytest to ignore a test entirely without executing it, typically because the test is irrelevant to the current environment, platform, or dependencies. In contrast, I use `@pytest.mark.xfail` when I expect a test to fail because a bug is known or a feature is still under development; pytest actually runs an `xfail` test and flags it as an expected failure if it fails, or raises an unexpected pass (`XPASS`) if it unexpectedly succeeds.

## 3. What does --strict-markers protect against?

I use the `--strict-markers` flag to protect against typos in custom marker names. Without this flag, if I accidentally misspell a custom marker decorator on a test, pytest silently ignores the typo and treats it as an unregistered marker without warning. Enabling `--strict-markers` forces pytest to raise an immediate error during test collection whenever an unconfigured marker is encountered, preventing unregistered or misspelled markers from causing tests to be skipped unintentionally.