from nunit_xml_reader import NUnitXmlReader
from excel_writer import ExcelWriter

from optparse import OptionParser
import sys


def check_options(options: "Parsed options") -> bool:
    expected_options = [options.report, options.filename]
    if any(elem is None for elem in expected_options):
        print("Missing options")
        return False
    else:
        return True


def main():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-i",
                      "--input",
                      dest="report",
                      help="NUnit XML report file name")
    parser.add_option("-o",
                      "--output",
                      dest="filename",
                      help="Generated Excel file name")

    (options, args) = parser.parse_args()
    if check_options(options):
        reader = NUnitXmlReader(options.report)
        assemblies = reader.build_nunit_test_assemblies()
        writer = ExcelWriter(assemblies)
        writer.create_workbook(options.filename)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
