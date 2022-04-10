import os
import openai
import json
import sys
import datetime
from datetime import datetime
import random
import time
import configparser

old_print = print

def timestamped_print(*args, **kwargs):
  old_print(datetime.now(), *args, **kwargs)

print = timestamped_print

config = configparser.ConfigParser()
config.read('API_keys.config')

def random_number():
    return random.randint(0,2)

def set_api_key_rand():
    api_key_items = config.items( "keys" )
    api_keys = [key for en, key in config.items("keys")]
    openai.api_key = api_keys[random_number()]


#openai.api_key = os.getenv("OPENAI_API_KEY")

"""
API_KEYS = ["key1", "key2", "key3"]
def random_number():
    return random.randint(0,2)

def set_api_key_rand():
    openai.api_key = API_KEYS[random_number()]
"""

EDIT_ENGINE = "code-davinci-edit-001"

TEMPERATURE = 0.3
N_SOLUTIONS = 2

# EDIT_OPERATIONS = ["fix spelling mistakes", "fix syntax error", "cleanup code"]
EDIT_OPERATIONS = ["fix spelling mistakes", "fix syntax errors"]
SLEEP_TIME_SECONDS = 4


"""
input_code: string containing input python file that is input to the edit/insert codex API
operation:  string containing The edit/insert operation described in natural language

returns output_codes

output_codes: list of strings containing the code after application of operation
"""
def run_edit(input_code, operation):

    set_api_key_rand()

    response = openai.Edit.create(
        engine= EDIT_ENGINE,
        input=input_code,
        instruction=operation,
        temperature=TEMPERATURE,
        n=N_SOLUTIONS
    )
    time.sleep(SLEEP_TIME_SECONDS)

    print(operation, response)

    #check for failure?
    output_codes = []
    for choice in response["choices"]:

        if "text" in choice:
            generated_code = choice["text"]
            output_codes.append(generated_code)
        else:
            print("NO RESULT")
            print(choice)

    return output_codes








"""
input_code: string containing input python file to be edited/inserted

operations: list of strings - edit/insert operations described in natural language applied sequentially
            Example: ["fix spelling mistakes", "fix syntax error", "beautify code"]

returns final_outputs

final_outputs: states of code after application of last operation

Should we save intermediary states?

"""
def run_edit_multiple_op(input_code, operations):

    states = [input_code]
    num_operations = 0

    current_input_set = {input_code}
    print(f"num operations {len(operations)}")
    for operation in operations:
        current_output_set = set()

        print(f"size on input set {len(current_input_set)}")
        for code in current_input_set:
            gen_codes = run_edit(code, operation)
            print(operation, len(gen_codes), gen_codes)
            current_output_set.update(gen_codes)

        print(f"size on output set {len(current_output_set)}")
        
        current_input_set = current_output_set
    
    final_outputs = current_input_set

    return final_outputs

def save_strings_to_py_file(solution_strings, folder_name="edit_sol_pys"):
    os.makedirs(folder_name, exist_ok=True)

    # os.chdir(folder_name)
    all_files = os.listdir(folder_name)
    for f in all_files:
        os.remove(f)
    
    for i in range(len(solution_strings)):
        with open(f"{folder_name}/solution_{i}.py", "w") as fp:
            fp.write(solution_strings[i])



"""
file_name: file name of json file that is output of codex-davinci-002 with natural language prompt as input
They are multiple outputs for a single input depending upon k
The file has outputs for multiple prompts
"""
def run(file_name,out_dir="."):
    with open(file_name,"r") as input_fp:
        data = json.load(input_fp)

        output = {"solutions":[]}

        total_output_set = set()
        for solution in data:
            outputs = run_edit_multiple_op(solution, EDIT_OPERATIONS)
            total_output_set.update(outputs)

        output["solutions"].extend(total_output_set)

        # json_output = json.dumps(output)


        with open(f'{out_dir}/codex_edit_solutions.json', 'w') as outfile:
            json.dump(output["solutions"], outfile)
        
        save_strings_to_py_file(output["solutions"], f"{out_dir}/edit_sol_pys")





if __name__ == "__main__":

    #python3 run_edit_module.py example_output.json
    input_file_name = sys.argv[1]
    out_dir = os.path.dirname(input_file_name)
    out_dir = sys.argv[2]

    #The following code is to save the example prompt and outputs
    """
    with open(input_file_name,"r") as input_fp:
        data = json.load(input_fp)

        with open('example_prompt.txt', 'w') as outfile:
            json.dump(data["prompt"], outfile)
        
        save_strings_to_py_file(data["solutions"], "example_outputs")
    exit()
    """


        

    sys.stdout = open(f'{out_dir}/edit_out.log', 'w')
    run(input_file_name,out_dir=out_dir)
    sys.stdout.close()







