class NUnitTestAssembly(object):
    """Representation of a NUnit tests assembly.

    Attributes:
        name: A string representation of the test assembly name.
        duration: An integer indicating the assembly tests' execution duration in milliseconds.
        fixtures: A list of NUnitTestFixture composing the assembly.
    """

    def __init__(self, name: str, duration: int, fixtures: list):
        self.name = name
        self.duration = duration
        self.fixtures = fixtures

    def __repr__(self):
        return "NUnitTestAssembly({0}, {1}, {2})".format(self.name, self.duration, self.fixtures)

    def __str__(self):
        s = "NUnit Test Assembly {0} of duration {1}ms".format(self.name, self.duration)
        for fixtures in self.fixtures:
            s += "\n- {0}".format(fixtures)
        return s
