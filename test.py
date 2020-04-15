# test program

from junit_xml import TestSuite, TestCase

test_cases = [TestCase('Test1', 'some.class.name', 123.345, 'I am stdout!', 'I am stderr!')]

ts = TestSuite("my test suite", test_cases)

# pretty printing is on by default but can be disabled using prettyprint=False
print(TestSuite.to_xml_string([ts]))

with open('test_result.xml', 'w') as f:
    TestSuite.to_file(f, [ts], prettyprint=True)
