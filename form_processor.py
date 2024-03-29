#!/usr/bin/env python
#
# HTML Form Processing Script
# By Brandon Smith (brandon.smith@studiobebop.net)
#
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def parse_forms(page_url, soup):
    forms = []
    for form in soup.findAll("form"):
        form_action = form["action"]
        if not form_action.startswith("http"):
            form_action = urljoin(page_url, form_action)
        form_data = {}

        # Get input tags
        for input in form.findAll("input"):
            if not input.has_attr("name") or input.has_attr("onclick"):
                continue
            if input.has_attr("type") and input["type"] == "checkbox":
                continue
            input_name = input["name"]
            if input.has_attr("value"):
                input_value = input["value"]
            else:
                input_value = ""
            form_data[input_name] = input_value

        # Get select statements
        for select in form.findAll("select"):
            options = []
            select_name = select["name"]
            for option in select.findAll("option"):
                options.append(option["value"])
            form_data[select_name] = options

        # Get textareas
        for textarea in form.findAll("textarea"):
            textarea_name = textarea["name"]
            form_data[textarea_name] = ""

        form = {"action": form_action, "inputs": form_data}
        forms.append(form)

    return forms
