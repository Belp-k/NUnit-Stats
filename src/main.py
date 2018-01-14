from nunit_xml_reader import NUnitXmlReader

import sys

def main(argv: list):
    if len(argv) != 2:
        print(argv[0], 'usage: <xml filename>')
    else:
        reader = NUnitXmlReader(argv[1])
        assemblies = reader.build_nunit_test_assemblies()
        for assembly in assemblies:
            print(assembly)

if __name__ == "__main__":
   main(sys.argv)