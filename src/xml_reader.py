from nunit_test import NUnitTest
from nunit_test_fixture import NUnitTestFixture
from nunit_test_assembly import NUnitTestAssembly

import xml.etree.ElementTree as ET
import sys

# Retrieves all test assemblies from the input XML test results
# arg       : the NUnit report filename
# return    : the ElementTree list of found test assemblies
def get_assemblies(filename: str) -> list:
    try:
        tree = ET.parse(filename)
    except:
        print(filename, "is not a valid XML file")
        sys.exit(1)

    root = tree.getroot()

    # All 'test-suite' nodes of type 'Assembly'
    return root.findall(".//test-suite/[@type='Assembly']")

# Retrieves all test fixtures from the input test suite as an ElementTree node
# arg       : the ElementTree note of a test suite
# return    : the ElementTree list of found test fixtures
def get_fixtures(suite: "A test-suite node of type Assembly") -> list:
    # All 'test-suite' nodes of type 'TestFixture'
    return suite.findall(".//test-suite/[@type='TestFixture']")

# Retrieves all tests from the input text fixture as an ElementTree node
# arg       : the ElementTree note of a test fixture
# return    : the ElementTree list of found tests
def get_tests(fixture: "A test-suite node of type TestFixture") -> list:
    return fixture.findall(".//test-case")

# Builds a list of NUnitTest objects
# arg       : the ElementTree list of tests
# return    : the NUnitTest list
def build_nunit_tests(tests: list) -> list:
    nunit_tests = []
    for test in tests:
        test_name = test.attrib.get("name")
        test_order = tests.index(test) + 1
        # Durations are expressed in seconds in NUnit test report
        test_duration_ms = float(test.attrib.get("duration")) * 1000
        nunit_tests.append(NUnitTest(test_name, test_order, round(test_duration_ms)))
    return nunit_tests

# Builds a list of NUnitTestFixture objects
# arg       : the ElementTree list of test fixtures
# return    : the NUnitTestFixture list
def build_nunit_test_fixtures(fixtures: list) -> list:
    nunit_test_fixtures = []
    for fixture in fixtures:
        fixture_name = fixture.attrib.get("name")
        fixture_order = fixtures.index(fixture) + 1
        # Durations are expressed in seconds in NUnit test report
        fixture_duration = float(fixture.attrib.get("duration")) * 1000
        test_cases = build_nunit_tests(get_tests(fixture))
        nunit_test_fixtures.append(NUnitTestFixture(fixture_name, fixture_order, round(fixture_duration), test_cases))
    return nunit_test_fixtures

# Builds a list of NUnitTestAssembly objects
# arg       : the ElementTree list of test assemblies
# return    : the NUnitTestAssembly list
def build_nunit_test_assemblies(assemblies: list) -> list:
    nunit_test_assemblies = []
    for assembly in assemblies:
        assembly_name = assembly.attrib.get("name")
        # Durations are expressed in seconds in NUnit test report
        assembly_duration = float(assembly.attrib.get("duration")) * 1000
        fixtures = build_nunit_test_fixtures(get_fixtures(assembly))
        nunit_test_assemblies.append(NUnitTestAssembly(assembly_name, round(assembly_duration), fixtures))
    return nunit_test_assemblies

def main(argv: list):
    if len(argv) != 2:
        print(argv[0], 'usage: <xml filename>')
    else:
        assemblies = build_nunit_test_assemblies(get_assemblies(argv[1]))
        for assembly in assemblies:
            print(assembly)

if __name__ == "__main__":
   main(sys.argv)
