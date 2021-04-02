import json
import sys
from langdetect import detect
from langdetect import detect_langs

json_file_list = sys.argv[1]

with open(json_file_list) as fp:
    for line in fp:
        total_count = 0
        outlink_count = 0
        te_count = 0
        # print(line)
        with open(line.strip()) as jsonfp:
            for json_line in jsonfp:
                total_count += 1
                curr_dict = json.loads(json_line.strip())
                # print(curr_dict)
                # quit()
                if len(curr_dict['outlinks']) != 0:
                    outlink_count += 1
                    # print(detect_langs(curr_dict['content']))
                    # quit()
                    try:
                        if 'te' in detect_langs(curr_dict['content']):
                            te_count += 1
                    except:
                        print(total_count, outlink_count, te_count)
                        # pass
                    # print(detect_langs(curr_dict['content']))
                    # print(curr_dict['content'], curr_dict['outlinks'])
        print(total_count, outlink_count, te_count)
        quit()