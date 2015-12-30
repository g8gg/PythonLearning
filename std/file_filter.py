import getopt
import sys
from itertools import filterfalse
import fileinput


def usage():
    print(
            """Try file_filter.py -h [--help]
            usage: python file_filter.py -k keyword_file -s source_file -o filtered_file
                   python file_filter.py --keyword=keyword_file --source=source_file --output=filtered_file
            Options and arguments (and corresponding environment variables):
            -k, --keyword=       special keyword file and one word per line will be acceptable
            -s  --source=        special source file to filter
            -o  --output=        special output file and save content filtered only
            """
    )


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:k:s:i", ["help", "output=", "keyword=", "source="])
        # print(sys.argv[0])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    interactive_mode = False
    keyword_file = None
    source_file = None
    output_file = None
    for opt, value in opts:
        if opt == "-i":
            interactive_mode = True
        elif opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-k", "--keyword"):
            keyword_file = value
            print(keyword_file)
        elif opt in ("-s", "--source"):
            source_file = value
            print(source_file)
        elif opt in ("-o", "--output"):
            output_file = value
            print(output_file)
        else:
            assert False, "unhandled option"
            # ...

    # with fileinput.input(files=(keyword_file),openhook=fileinput.hook_encoded("utf8")) as f:
    #     for line in f:
    #         print(line)
    keyword_arr = []
    with open(keyword_file, mode='r', encoding='utf8') as kf, \
            open(source_file, mode='r', encoding='utf8') as sf, \
            open(output_file, mode='w+', encoding='utf8') as of:
        for line in kf:
            keyword_arr.append(line.rstrip())
        for sline in sf:
            for keyword in keyword_arr:
                sline = sline.replace(keyword, '')
            sline.replace(' ', '')
            sline.replace('  ', '')
            sline = sline.replace(chr(32), '')
            print(sline, end='', file=of)


# lines = [line.rstrip() for line in open(keyword_file, mode='r', encoding='utf8')]
# print(lines)
if __name__ == "__main__":
    main()
