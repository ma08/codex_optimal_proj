import os
import openai
import json
import sys
import datetime
from datetime import datetime
import random
import time
import numpy as np

old_print = print

def timestamped_print(*args, **kwargs):
  old_print(datetime.now(), *args, **kwargs)

print = timestamped_print


openai.api_key = os.getenv("OPENAI_API_KEY")

"""
API_KEYS = ["key1", "key2", "key3"]
def random_number():
    return random.randint(0,2)

def set_api_key_rand():
    openai.api_key = API_KEYS[random_number()]
"""

EDIT_ENGINE = "code-davinci-edit-001"

# TEMPERATURE = 0.3
# N_SOLUTIONS = 2

# EDIT_OPERATIONS = ["fix spelling mistakes", "fix syntax error", "cleanup code"]
EDIT_OPERATIONS = ["fix spelling mistakes", "fix syntax errors"] # PROBABLY NEED TO AUTOMATE THIS PART AS WELL, BUT NEED TO DISCUSS PROCESS IN MORE DETAIL...


"""
input_code: string containing input python file that is input to the edit/insert codex API
operation:  string containing The edit/insert operation described in natural language

returns output_codes

output_codes: list of strings containing the code after application of operation
"""
def run_edit(input_code, operation, temp, k):

    # set_api_key_rand()

    response = openai.Edit.create(
        engine= EDIT_ENGINE,
        input=input_code,
        instruction=operation,
        temperature=temp,
        n=k
    )
    time.sleep(2)

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
def run_edit_multiple_op(input_code, operations, temp, k):

    states = [input_code]
    num_operations = 0

    current_input_set = {input_code}
    print(f"num operations {len(operations)}")
    for operation in operations:
        current_output_set = set()

        print(f"size on input set {len(current_input_set)}")
        for code in current_input_set:
            gen_codes = run_edit(code, operation, temp, k)
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
def run(file_name,out_dir=".",n_itr):
    with open(file_name,"r") as input_fp:
        data = json.load(input_fp)

        for itr in n_itr:
            # can later change values of TEMPERATURE and N_SOLUTIONS
            TEMPERATURE = np.random.randint(0, 10)/10
            N_SOLUTIONS = np.random.randint(1, 100)
            # would sample different edit operations here (ultimately put in array format) as well, but need to discuss further on automating selection of edit operations, as mentioned in beginning of file

            output = {"solutions":[]}

            total_output_set = set()
            for solution in data:
                outputs = run_edit_multiple_op(solution, EDIT_OPERATIONS, TEMPERATURE, N_SOLUTIONS)
                total_output_set.update(outputs)

            output["solutions"].extend(total_output_set)

            # json_output = json.dumps(output)

            # File naming format: <edit params><completion params>_codex_solutions.json
            pref = 'edit_' + str(TEMPERATURE) + 'T_' + str(N_SOLUTIONS) + 'k_init_'
            if not os.path.exists(f"{out_dir}/{pref}{file_name}"):
                with open(f'{out_dir}/{pref}{file_name}', 'w') as outfile:
                    json.dump(output["solutions"], outfile)
            
                fold_name = pref + file_name[:-4] + "_pys" # removes .json extension
                save_strings_to_py_file(output["solutions"], f"{out_dir}/{fold_name}")





if __name__ == "__main__":

    #python3 run_edit_module.py example_output.json 100
    input_file_name = sys.argv[1]
    out_dir = os.path.dirname(input_file_name)
    n_itr = sys.argv[2]

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
    run(input_file_name,out_dir=out_dir,n_itr)
    sys.stdout.close()

