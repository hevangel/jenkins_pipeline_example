import argparse
import random
from datetime import datetime
import platform
from junit_xml import TestSuite, TestCase
"""
dummy test to generate fake Junit XML report
"""

def main():
    parser = argparse.ArgumentParser(description='dummy test')
    parser.add_argument('-classes', type=int, default=5, help='number of classes')
    parser.add_argument('-testcases', type=int, default=10, help='number of testcases')
    parser.add_argument('-pass_rate', type=int, default=75, help='pass rate')
    parser.add_argument('-error_rate', type=int, default=20, help='error rate')
    parser.add_argument('-failure_rate', type=int, default=10, help='failure rate')
    parser.add_argument('-skip_rate', type=int, default=10, help='skip rate')
    parser.add_argument('-outputfile', type=str, default='test_results.xml', help='output file')
    parser.add_argument('-print', action='store_true', help='print the test results')
    args = parser.parse_args()

    ts = TestSuite(name='my test suite', hostname=platform.node(), timestamp=datetime.now())
    for i in range(args.classes):
        for j in range(args.testcases):
            tc = TestCase(classname=f"myclass{i}",
                          name=f"mytest{j}",
                          elapsed_sec=random.randint(100, 1000),
                          stdout = "stdout output",
                          stderr = "stderr output")
            if random.randint(0, 100) < args.pass_rate:
                if random.randint(0, 100) < args.error_rate:
                    tc.add_error_info(message=f"error {i} {j}", output="error output message", error_type="ERR1")
                elif random.randint(0, 100) < args.failure_rate:
                    tc.add_failure_info(message=f"failure {i} {j}", output="failure output message", failure_type="FAIL1")
                elif random.randint(0, 100) < args.skip_rate:
                    tc.add_skipped_info(message=f"skipped {i} {j}", output="skipped output message")
            ts.test_cases.append(tc)

    # pretty printing is on by default but can be disabled using prettyprint=False
    if args.print:
        print(TestSuite.to_xml_string([ts]))

    with open(args.outputfile, 'w') as f:
        TestSuite.to_file(f, [ts], prettyprint=True)

if __name__ == "__main__":
    # execute only if run as a script
    main()
