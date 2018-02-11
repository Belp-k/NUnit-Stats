def compute_ratio(total: float, element: float) -> float:
    return (element * 100.0) / total


class RatioGenerator(object):
    """Generates a matrix containing the fixtures durations to
    assembly duration ratio, and the tests durations to
    fixture duration ratio.
    """

    def __init__(self, assembly: "A NUnitTestAssembly"):
        self._assembly = assembly

    def generate_matrix(self, verbose: bool = True) -> list:
        matrix = []

        if verbose:
            matrix.append(["Fixture name", "Test name", "Test ratio", "Fixture ratio"])
            matrix.append([])

        assembly_fixtures_dur = self._assembly.fixtures_durations()
        for fixture in self._assembly.fixtures:
            fixture_duration_ratio = compute_ratio(assembly_fixtures_dur, fixture.duration)
            line = [fixture.name, "", "", "%.2f" % fixture_duration_ratio]
            matrix.append(line)

            fixture_tests_dur = fixture.tests_durations()
            for test in fixture.tests:
                test_duration_ratio = compute_ratio(fixture_tests_dur, test.duration)
                line = [fixture.name, test.name, "%.2f" % test_duration_ratio, "%.2f" % fixture_duration_ratio]
                matrix.append(line)

        return matrix

    def get_name(self) -> str:
        return "Ratio " + self._assembly.name
