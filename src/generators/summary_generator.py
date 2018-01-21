class SummaryGenerator(object):
    """Generates a matrix representing a summary sheet of
    extracted NUnit test assembly report.
    """

    def __init__(self, assemblies: list):
        self._assemblies = assemblies

    def generate_matrix(self):
        matrix = [["Assembly name", "Number of fixtures", "Duration"], []]
        for assembly in self._assemblies:
            matrix.append([assembly.name, assembly.fixtures_count(), assembly.duration])
        return matrix

    def get_name(self):
        return "Summary"
