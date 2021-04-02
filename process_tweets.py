import json
import sys

json_file_list = sys.argv[1]

with open(json_file_list) as fp:
    for line in fp:
        print(line)
        with open(line.strip()) as jsonfp:
            for json_line in jsonfp:
                curr_dict = json.loads(json_line.strip())
                # print(curr_dict)
                # quit()
                if len(curr_dict['outlinks']) != 0:
                    print(curr_dict['content'], curr_dict['outlinks'])
        quit()