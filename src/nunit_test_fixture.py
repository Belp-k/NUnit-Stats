from nunit_test import NUnitTest

class NUnitTestFixture(object):
    """Representation of a NUnitTest test fixture.

    Attributes:
        name: A string representation of the fixture name.
        order: An integer indicating the fixture order inside the test suite.
        duration: An integer indicating the fixture execution duration in milliseconds.
        tests: A list of NUnitTest composing the fixture.
    """

    def __init__(self, name: str, order: int, duration: int, tests: list):
        self.name = name
        self.order = order
        self.duration = duration
        self.tests = tests

    def __repr__(self):
        return "NUnitTestFixture({0}, {1}, {2}, {3})".format(self.name, self.order, self.duration, self.tests)

    def __str__(self):
        s = "NUnit Test Fixture {0} #{1} of duration {2}ms".format(self.name, self.order, self.duration)
        for test in self.tests:
            s += "\n\t+ {0}".format(test)
        return s
