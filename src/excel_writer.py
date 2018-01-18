import xlwt


class ExcelWriter(object):
    """Writer of an excel workbook from a list of NUnitTestAssembly.
    """

    def __init__(self, generators: list):
        self._generators = generators

    def __str__(self):
        return self.__class__.__name__

    def create_workbook(self, name: str):
        workbook = xlwt.Workbook()

        for generator in self._generators:
            # Excel does not support sheet names greater than 31 characters
            sheet = workbook.add_sheet(generator.get_name()[:31])

            for (i, line) in enumerate(generator.generate_matrix()):
                for (j, element) in enumerate(line):
                    sheet.write(i, j, element)

        try:
            workbook.save(name)
            print("[{0}]: Generated workbook '{1}'".format(self, name))
        except:
            print("[{0}]: Failed to save workbook '{1}'!".format(self, name))
            raise
