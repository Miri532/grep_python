from bs4 import BeautifulSoup
import requests
import sys


def print_formatted(location, line):
    print(location + ": " + line)


def search_in_lines_and_print(location, word_to_search, lines, is_reverse, is_case_sensitive):
    if is_case_sensitive:
        for line in lines:
            if word_to_search in line and not is_reverse:
                print_formatted(location, line)
            elif word_to_search not in line and is_reverse:
                print_formatted(location, line)
    # case insensitive
    elif not is_case_sensitive:
        for line in lines:
            if word_to_search.lower() in line.lower() and not is_reverse:
                print_formatted(location, line)
            elif word_to_search.lower() not in line.lower() and is_reverse:
                print_formatted(location, line)


def search_in_file(word_to_search, location, is_reverse, is_case_sensitive):
    """
    search a word in a file
    :param word_to_search:
    :param location: file to search in
    :param is_reverse: do reverse search if true  or regular search otherwise
    :param is_case_sensitive: do case sensitive search if true or case insensitive search otherwise
    :return:
    """
    try:
        f = open(location, "r")
        search_in_lines_and_print(location, word_to_search, f.readlines(), is_reverse, is_case_sensitive)
        f.close()
    except IOError:
        print("no file by the name, skipping this file" + location)


def search_in_web_page(word_to_search, location, is_reverse, is_case_sensitive):
    """
    search a word in a webpage
    :param word_to_search:
    :param location: url to search in
    :param is_reverse: do reverse search if true  or regular search otherwise
    :param is_case_sensitive: do case sensitive search if true or case insensitive search otherwise
    """
    try:
        page = requests.get(location)
        soup = BeautifulSoup(page.text, 'html.parser')
        output = soup.get_text()

        search_in_lines_and_print(location, word_to_search, output.splitlines(), is_reverse, is_case_sensitive)
    except requests.exceptions.RequestException as err:
        print("error: skipping this url ", err)


def print_usage_and_exit():
    print("usage: -v(optional) -i(optional) <word_to search> <search_list>")
    exit(0)


def main():
    params = sys.argv
    word_to_search = ""
    where_to_search = ""
    is_reverse = False
    is_case_sensitive = True
    if len(params) == 3:
        # regular search & case sensitive
        word_to_search = params[1]
        where_to_search = params[2]

    elif len(params) == 5:
        # reverse search & case insensitive
        if params[1] == '-v' and params[2] == '-i':
            is_reverse = True
            is_case_sensitive = False

        elif params[2] == '-v' and params[1] == '-i':
            is_reverse = True
            is_case_sensitive = False
        else:
            print_usage_and_exit()
        word_to_search = params[3]
        where_to_search = params[4]

    elif len(params) == 4:
        # reverse search || case insensitive
        if params[1] == '-v':
            is_reverse = True
        elif params[1] == '-i':
            is_case_sensitive = False
        else:
            print_usage_and_exit()
        word_to_search = params[2]
        where_to_search = params[3]

    else:
        print_usage_and_exit()

    where_to_search_list = where_to_search.split(",")
    for location in where_to_search_list:
        location_list = location.split(":", 1)
        if location_list[0] == "file":
            search_in_file(word_to_search, location_list[1], is_reverse, is_case_sensitive)
        if location_list[0] == "url":
            search_in_web_page(word_to_search, location_list[1], is_reverse, is_case_sensitive)


if __name__ == '__main__':
    main()
