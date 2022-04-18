

import os
import sys
import json


def print_json(data):
    print(json.dumps(data, indent=4))


def get_data(stage):
    with open(os.path.join(sys.path[0], 'data.json')) as data_file:
        data = json.load(data_file)
    return data[stage]


def get_input():
    return input()


def get_stage(data, input_data):
    return data[input_data]


def get_stage_data(data, stage):
    return data[stage]


def get_stage_type(stage_data):
    return stage_data['type']


def get_stage_text(stage_data):
    return stage_data['text']


def get_stage_options(stage_data):
    return stage_data['options']


def print_stage_text(text):
    print(text)


def print_stage_options(options):
    print(options)


def get_option_data(data, stage, option_number):
    return data[stage]['options'][option_number]


def get_option_text(option_data):
    return option_data['text']


def get_option_next_stage(option_data):
    return option_data['next_stage']


def get_option_item(option_data):
    return option_data['item']


def get_option_item_text(option_data):
    return option_data['item_text']


def print_option_text(text):
    print(text)


def get_option_number(input_data):
    return int(input_data)


def get_option(stage_options, option_number):
    return stage_options[option_number]


def get_option_next_stage(option):
    return option['next_stage']


def get_option_item(option):
    return option['item']


def get_option_item_text(option):
    return option['item_text']


def print_option_text(text):
    print(text)


def get_option_number(input_data):
    return int(input_data)


def get_option(stage_options, option_number):
    return stage_options[option_number]


def get_option_next_stage(option):
    return option['next_stage']


def get_option_item(option):
    return option['item']


def get_option_item_text(option):
    return option['item_text']


def print_option_text(text):
    print(text)


def get_option_number(input_data):
    return int(input_data)


def get_option(stage_options, option_number):
    return stage_options[option_number]


def get_option_next_stage(option):
    return option['next_stage']


def get_option_item(option):
    return option['item']


def get_option_item_text(option):
    return option['item_text']


def print_option_text(text):
    print(text)


def get_option_number(input_data):
    return int(input_data)


def get_option(stage_options, option_number):
    return stage_options[option_number]


def get_option_next_stage(option):
    return option['next_stage']


def get_option_item(option):
    return option['item']


def get_option_item_text(option):
    return option['item_text']


def print_option_text(text):
    print(text)


def get_option_number(input_data):
    return int(input_data)


def get_option(stage_options, option_number):
    return stage_options[option_number]


def get_option_next_stage(option):
    return option['next_stage']


def get_option_item(option):
    return option['item']


def get_option_item_text(option):
    return option['item_text']


def print_option_text(text):
    print(text)


def get_option_number(input_data):
    return int(input_data)


def get_option(stage_options, option_number):
    return stage_options[option_number]


def get_option_next_stage(option):
    return option['next_stage']


def get_option_item(option):
    return option['item']


def get_option_item_text(option):
    return option['item_text']


def print_option_text(text):
    print(text)


def get_option_number(input_data):
    return int(input_data)


def get_option(stage_options, option_number):
    return stage_options[option_number]


def get_option_next_stage(option):
    return option['next_stage']


def get_option_item(option):
    return option['item']


def get_option_item_text(option):
    return option['item_text']


def print_option_text(text):
    print(text)


def get_option_number(input_data):
    return int(input_data)


def get_option(stage_options, option_number):
    return stage_options[option_number]


def get_option_next_stage(option):
    return option['next_stage']


def get_option_item(option):
    return option['item']


def get_option_item_text(option):
    return option['item_text']


def print_option_text(text):
    print(text)


def get_option_number(input_data):
    return int(input_data)


def get_option(stage_options, option_number):
    return stage_options[option_number]


def get_option_next_stage(option):
    return option['next_stage']


def get_option_item(option):
    return option['item']


def get_option_item_text(option):
    return option['item_text']


def print_option_text(text):
    print(text)


def get_option_number(input_data):
    return int(input_data)


def get_option(stage_options, option_number):
    return stage_options[option_number]


def get_option_next_stage(option):
    return option['next_stage
