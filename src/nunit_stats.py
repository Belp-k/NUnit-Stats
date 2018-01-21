from nunit_xml_reader import NUnitXmlReader
from excel_writer import ExcelWriter
from generators.summary_generator import SummaryGenerator
from generators.tests_list_generator import TestsListGenerator

from optparse import OptionParser
import sys


def check_options(options: "Parsed options") -> bool:
    expected_options = [options.report, options.filename]
    if any(elem is None for elem in expected_options):
        print("Missing options")
        return False
    else:
        return True


def clean_filename(options: "Parsed options"):
    if options.filename.lower().endswith((".xls", ".xlsx", ".csv")):
        options.filename = '.'.join(options.filename.split('.')[:-1])


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
                      help="Generated Excel file name without extension")

    (options, args) = parser.parse_args()
    if check_options(options):
        reader = NUnitXmlReader(options.report)
        print("[NUnit-Stats]: Parsed NUnit test report '{0}'".format(options.report))

        assemblies = reader.build_nunit_test_assemblies()
        nb_of_assemblies = len(assemblies)
        separator = "\n\t- "
        assemblies_names = separator.join([a.name for a in assemblies])
        print("[NUnit-Stats]: Extracted {0} NUnit test assemblies:{1}{2}".format(nb_of_assemblies,
                                                                                 separator,
                                                                                 assemblies_names))

        generators = [TestsListGenerator(a) for a in assemblies]
        generators.insert(0, SummaryGenerator(assemblies))
        writer = ExcelWriter(generators)
        clean_filename(options)
        writer.create_workbook(options.filename)

        print("[NUnit-Stats]: Bye")
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
