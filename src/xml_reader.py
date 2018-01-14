from nunit_test import NUnitTest
from nunit_test_fixture import NUnitTestFixture

import xml.etree.ElementTree as ET
import sys

# Retrieves all test fixtures from the input XML test results
# arg       : the NUnit report filename
# return    : the ElementTree list of found test fixtures
def get_all_fixtures(filename: str) -> list:
    try:
        tree = ET.parse(filename)
    except:
        print(filename, "is not a valid XML file")
        sys.exit(1)

    root = tree.getroot()

    # All 'test-suite' nodes of type 'TestFixture'
    return root.findall(".//test-suite/[@type='TestFixture']")

# Retrieves all test cases from the input text fixture as an ElementTree
# arg       : the ElementTree note of a test fixture
# return    : the ElementTree list of found test cases
def get_test_cases(fixture: "A test-suite node of type TestFixture") -> list:
    return fixture.findall(".//test-case")

# Builds a list of NUnitTest objects
# arg       : the ElementTree list of test cases
# return    : the NUnitTest list
def build_test_cases(test_cases: list) -> list:
    nunit_tests = []
    for test_case in test_cases:
        test_name = test_case.attrib.get("name")
        test_order = test_cases.index(test_case) + 1
        # Durations are expressed in seconds in NUnit test report
        test_duration_ms = float(test_case.attrib.get("duration")) * 1000
        nunit_tests.append(NUnitTest(test_name, test_order, round(test_duration_ms)))
    return nunit_tests

# Builds a list of NUnitTestFixture objects
# arg       : the ElementTree list of test fixtures
# return    : the NUnitTestFixture list
def build_test_fixtures(test_fixtures: list) -> list:
    nunit_test_fixtures = []
    for fixture in test_fixtures:
        fixture_name = fixture.attrib.get("name")
        fixture_order = test_fixtures.index(fixture) + 1
        # Durations are expressed in seconds in NUnit test report
        fixture_duration = float(fixture.attrib.get("duration")) * 1000
        test_cases = build_test_cases(get_test_cases(fixture))
        nunit_test_fixtures.append(NUnitTestFixture(fixture_name, fixture_order, round(fixture_duration), test_cases))
    return nunit_test_fixtures

def main(argv: list):
    if len(argv) != 2:
        print(argv[0], 'usage: <xml filename>')
    else:
        all_fixtures = build_test_fixtures(get_all_fixtures(argv[1]))
        for fixture in all_fixtures:
            print(fixture)

if __name__ == "__main__":
   main(sys.argv)
