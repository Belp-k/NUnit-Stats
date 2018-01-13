import xml.etree.ElementTree as ET
import sys

# Retrieves all test fixtures from the input XML test results
# arg       : the NUnit report filename
# return    : the ElementTree list of found test fixtures
def get_all_fixtures(filename: str) -> list:
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # All 'test-suite' nodes of type 'TestFixture'
    return root.findall(".//test-suite/[@type='TestFixture']")

def main(argv: list):
    if len(argv) != 2:
        print(argv[0], 'usage: <xml filename>')
    else:
        all_fixtures = get_all_fixtures(argv[1])
        for fixture in all_fixtures:
            print(fixture.attrib.get("name"), fixture.attrib.get("duration"))

if __name__ == "__main__":
   main(sys.argv)
