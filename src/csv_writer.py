import csv


class CSVWriter(object):
    """Writer of csv files from a list of generators.
    """

    def __init__(self, generators: list):
        self._generators = generators

    def __str__(self):
        return self.__class__.__name__

    def generate_report(self, name: str):
        for generator in self._generators:
            filename = name + "_" + generator.get_name() + ".csv"
            with open(filename, "w", newline="") as csvfile:
                writer = csv.writer(csvfile, delimiter=";")
                for line in generator.generate_matrix(False):
                    writer.writerow(line)
                print("[{0}]: Generated csv file '{1}'".format(self, filename))
