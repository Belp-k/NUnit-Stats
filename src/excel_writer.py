import xlwt


class ExcelWriter(object):
    """Writer of an excel workbook from a list of NUnitTestAssembly.
    """

    def __init__(self, assemblies: list):
        self._assemblies = assemblies

    def __str__(self):
        return self.__class__.__name__

    def create_workbook(self, name: str):
        workbook = xlwt.Workbook()

        for assembly in self._assemblies:
            # Excel does not support sheet names greater than 31 characters
            sheet = workbook.add_sheet(assembly.name[:31])

            row_offset = 0
            for fixture in assembly.fixtures:
                for (j, test) in enumerate(fixture.tests):
                    sheet.write(row_offset + j, 0, fixture.name)
                    sheet.write(row_offset + j, 1, test.name)
                    sheet.write(row_offset + j, 2, test.duration)
                row_offset += fixture.tests_count()

        try:
            workbook.save(name)
            print("[{0}]: Generated workbook '{1}'".format(self, name))
        except:
            print("[{0}]: Failed to save workbook '{1}'!".format(self, name))
            raise
