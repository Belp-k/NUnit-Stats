class NUnitTest(object):
    """Representation of a NUnitTest test.

    Attributes:
        name: A string representation of the test name.
        order: An integer indicating the test order inside the test fixture.
        duration: An integer indicating the test execution duration in milliseconds.
    """

    def __init__(self, name: str, order: int, duration: int):
        self.name = name
        self.order = order
        self.duration = duration

    def __repr__(self):
        return "NUnitTest({0}, {1}, {2})".format(self.name, self.order, self.duration)

    def __str__(self):
        return "NUnit Test {0} #{1} of duration {2}ms".format(self.name, self.order, self.duration)