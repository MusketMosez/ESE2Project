import json
from re import match

from db_api_doc_res import DbApiDocRes
from json_handler import get_example_json, get_schema

VERBOSE = True
BASE_URL = "base.url/db/api"


def get_pp_json(json_dict):
    """
    Converts json to a pretty printable string.
    :param json_dict: the json as a dictionary
    :return: formatted json as a string
    """
    # from pprint import pformat
    # return pformat(schema, width=300, compact=False)
    return json.dumps(json_dict, indent=3)


def create_cat_doc(category) -> list:
    """
    Generates documentation for all requests in one category.
    :param category: the category of the requests
    :return: formatted mD docs as a string
    """
    res = DbApiDocRes()
    cat_doc = []
    cat_doc += "<ul>\n"
    for request, details in res.cats[category].items():
        cat_doc += "<li> %s\n" % request
        cat_doc += "<details><blockquote>\n"
        cat_doc += "<ul>\n"
        cat_doc += "<li> status: %s\n" % (details["status"].lower())
        cat_doc += "<li> url: %s/%s\n" % (BASE_URL, request)
        if details["status"] != "UNDESIGNED":
            if details["request"] == "GET":
                cat_doc += "<li> request method: GET\n"
                cat_doc += "<li> parameters: <code>%s</code>\n" % ", ".join(details["params"])
                cat_doc += "<li> example json response:\n<pre><code>"
                cat_doc += json.dumps(get_example_json("%s.json" % request, res), indent=3)
                cat_doc += "\n</code></pre>\n"
                cat_doc += "<li> response json schema:\n<pre><code>"
                cat_doc += get_pp_json(get_schema(request))
                cat_doc += "\n</code></pre>\n"
            elif details["request"] == "POST":
                cat_doc += "<li>request method: POST"
                cat_doc += "<li> example json request:\n<pre><code>"
                cat_doc += json.dumps(get_example_json("%s.json" % request, res), indent=3)
                cat_doc += "\n</code></pre>\n"
                cat_doc += "<li> request json schema:\n<pre><code>"
                cat_doc += get_pp_json(get_schema(request))
                cat_doc += "\n</code></pre>\n"
                if "response" in details:
                    cat_doc += "<li> response parameters: %s\n" % ", ".join(details["response"])
        cat_doc += "</ul>\n"
        cat_doc += "</blockquote></details>\n"
    cat_doc += "</ul>\n"
    return cat_doc


def generate_doc() -> None:
    """
    Autogenerates documentation fro the DB API, given json schemas exist and dummy data is created.
    """
    with open("db_api_doc_template.md", "r") as template, open("db_api_doc.md", "w+") as doc:
        for line in template:
            # Check for lines with <!---request_name-->
            cat_match = match(r'.*<!---([\w]*)-->.*', line)
            if cat_match:
                cat_doc = create_cat_doc(cat_match.group(1))
                doc.writelines(cat_doc)
            else:
                doc.write(line)


if __name__ == '__main__':
    generate_doc()
