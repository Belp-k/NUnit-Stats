from nunit_xml_reader import NUnitXmlReader
from csv_writer import CSVWriter
from excel_writer import ExcelWriter
from generators.summary_generator import SummaryGenerator
from generators.tests_list_generator import TestsListGenerator

from optparse import OptionParser
import sys


# Checks the consistency of the given options
# arg       : The OptionParser from given options
# return    : True if the options are consistent, False otherwise
def check_options(options: "Parsed options") -> bool:
    expected_options = [options.report, options.filename]
    if any(elem is None for elem in expected_options):
        print("Missing options")
        return False
    else:
        return True


# Removes the extension from the output file name
# arg       : The OptionParser from given options
def clean_filename(options: "Parsed options"):
    if options.filename.lower().endswith((".xls", ".xlsx", ".csv")):
        options.filename = '.'.join(options.filename.split('.')[:-1])


# Produces the list of NUnitTestAssembly from the input NUnit test report
# arg       : The NUnit test report filename
# return    : The list of NUnitTestAssembly
def read_assemblies(nunit_report: str) -> list:
    reader = NUnitXmlReader(nunit_report)
    print("[NUnit-Stats]: Parsed NUnit test report '{0}'".format(nunit_report))

    assemblies = reader.build_nunit_test_assemblies()

    nb_of_assemblies = len(assemblies)
    separator = "\n\t- "
    assemblies_names = separator.join([a.name for a in assemblies])
    print("[NUnit-Stats]: Extracted {0} NUnit test assemblies:{1}{2}".format(nb_of_assemblies,
                                                                             separator,
                                                                             assemblies_names))

    return assemblies


# Creates the list of generators necessary to build the report
# arg       : The list of NUnitTestAssembly, from which the report is produced
# return    : The list of generators
def create_generators(assemblies: list) -> list:
    generators = [TestsListGenerator(a) for a in assemblies]
    generators.insert(0, SummaryGenerator(assemblies))

    return generators


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
    parser.add_option("-l",
                      "--light",
                      dest="light",
                      default=False,
                      action="store_true",
                      help="Activate light report generation (CSV files instead of Excel workbook)")

    (options, args) = parser.parse_args()

    # Exit if missing of invalid options
    if not check_options(options):
        parser.print_help()
        sys.exit(1)

    # Read NUnitTestAssembly from input report
    assemblies = read_assemblies(options.report)

    # Create the necessary generators
    generators = create_generators(assemblies)

    # Generate the appropriate report
    writer = CSVWriter(generators) if options.light else ExcelWriter(generators)
    clean_filename(options)
    writer.generate_report(options.filename)

    print("[NUnit-Stats]: Bye")


if __name__ == "__main__":
    main()
