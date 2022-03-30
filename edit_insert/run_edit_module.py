import os
import openai
import json
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")
EDIT_ENGINE = "code-davinci-edit-001"

TEMPERATURE = 0.5
N_SOLUTIONS = 2

# EDIT_OPERATIONS = ["fix spelling mistakes", "fix syntax error", "cleanup code"]
EDIT_OPERATIONS = ["fix spelling mistakes", "fix syntax errors"]


"""
input_code: string containing input python file that is input to the edit/insert codex API
operation:  string containing The edit/insert operation described in natural language

returns output_codes

output_codes: list of strings containing the code after application of operation
"""
def run_edit(input_code, operation):

    response = openai.Edit.create(
        engine= EDIT_ENGINE,
        input=input_code,
        instruction=operation,
        temperature=TEMPERATURE,
        n=N_SOLUTIONS
    )

    print(input_code, operation, response)

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

def save_strings_to_py_file(solution_strings, folder_name="solution_pys"):
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
def run(file_name):
    with open(file_name,"r") as input_fp:
        data = json.load(input_fp)

        output = {"prompt":data["prompt"], "solutions":[]}

        total_output_set = set()
        for solution in data["solutions"]:
            outputs = run_edit_multiple_op(solution, EDIT_OPERATIONS)
            total_output_set.update(outputs)

        output["solutions"].extend(total_output_set)

        # json_output = json.dumps(output)

        with open('run_edit_output.json', 'w') as outfile:
            json.dump(output, outfile)
        
        save_strings_to_py_file(output["solutions"])





if __name__ == "__main__":

    #python3 run_edit_module.py example_output.json
    input_file_name = sys.argv[1]

    with open(input_file_name,"r") as input_fp:
        data = json.load(input_fp)

        with open('example_prompt.txt', 'w') as outfile:
            json.dump(data["prompt"], outfile)
        
        save_strings_to_py_file(data["solutions"], "example_outputs")
    exit()

        # with open('example_prompt.txt', 'w') as outfile:
            # json.dump(data["prompt"], outfile)

        

    sys.stdout = open(f'./out.log', 'w')
    run(input_file_name)
    sys.stdout.close()







