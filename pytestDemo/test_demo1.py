# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should bbe wrapped in methos only
# Method name should be very sensible as we may use regex for running only specific test cases
# -k used for specifing some method names
# -v gives us verbose output, metadata
# -s logs in output
# Use tags (@test.mark.smoke) and then run with -m

import pytest

@pytest.mark.skip
def test_firstProgram():
    print("Hello from pytest!")

@pytest.mark.xfail
def test_secondProgram():
    msg = "hell0"
    assert msg == "hi", "Test case failed due to mismatch of strings"
