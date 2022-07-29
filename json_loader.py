import json
import sys

def main(path):
    foo = open(path)
    data = json.load(foo) #dictionary
    print((data["report_view"][0]["children"][0]).keys())




if __name__ == '__main__' :
    path = sys.argv[1]
    main(path)