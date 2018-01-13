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

def main(argv: list):
    if len(argv) != 2:
        print(argv[0], 'usage: <xml filename>')
    else:
        all_fixtures = get_all_fixtures(argv[1])
        for fixture in all_fixtures:
            print("Fixture name = {0} - Duration = {1}".format(fixture.attrib.get("name"), fixture.attrib.get("duration")))
            test_cases = get_test_cases(fixture)
            for test_case in test_cases:
                print("\tTest name = {0} - Duration = {1}".format(test_case.attrib.get("name"), test_case.attrib.get("duration")))

if __name__ == "__main__":
   main(sys.argv)
