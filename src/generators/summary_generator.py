class SummaryGenerator(object):
    """Generates a matrix representing a summary sheet of
    extracted NUnit test assembly report.
    """

    def __init__(self, assemblies: list):
        self._assemblies = assemblies

    def generate_matrix(self, verbose: bool = True) -> list:
        matrix = []
        if verbose:
            matrix.append(["Assembly name", "Number of fixtures", "Duration"])
            matrix.append([])

        for assembly in self._assemblies:
            matrix.append([assembly.name, assembly.fixtures_count(), assembly.duration])
        return matrix

    def get_name(self) -> str:
        return "Summary"
