from nunit_xml_reader import NUnitXmlReader
from excel_writer import ExcelWriter

import sys


def main(argv: list):
    if len(argv) != 3:
        print(argv[0], 'usage: <input xml filename> <output xls filename>')
    else:
        reader = NUnitXmlReader(argv[1])
        assemblies = reader.build_nunit_test_assemblies()
        writer = ExcelWriter(assemblies)
        writer.create_workbook(argv[2])


if __name__ == "__main__":
    main(sys.argv)
