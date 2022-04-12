import configparser
import os
import sys
from numpy import promote_types
import openai
import json
import shutil



import random
import time

from datetime import datetime

old_print = print

def timestamped_print(*args, **kwargs):
  old_print(datetime.now(), *args, **kwargs)

print = timestamped_print


config = configparser.ConfigParser()
config.read('API_keys.config')

def random_number(tot_num):
    return random.randint(0,tot_num-1)

def set_api_key_rand():
    api_key_items = config.items( "keys" )
    api_keys = [key for en, key in config.items("keys")]
    openai.api_key = api_keys[random_number(len(api_keys))]



# openai.api_key = os.getenv("OPENAI_API_KEY")

TEMPERATURE = 0.5 #T
N_SOLUTIONS = 2 #k
ENGINE = "code-davinci-002"
MAX_TOKENS=4096
SLEEP_TIME_SECONDS = 5

def run_davinci(path, out_dir):
    with open(path) as f:
        prompt = f.read()

    input_prompt = f"\"\"\"\n{prompt}\n\"\"\""
    print(input_prompt)

    print("--------------------------")

    set_api_key_rand()


    response = openai.Completion.create(
        engine=ENGINE,
        prompt=input_prompt,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=N_SOLUTIONS
    )
    time.sleep(SLEEP_TIME_SECONDS)

    print(response)

    output = {"prompt":input_prompt, "solutions":[]}
    solution_set = set()

    for i in range(len(response["choices"])):
    # for choice in response["choices"]:
        choice = response["choices"][i]
        print(i, choice)



        finish_reason = choice["finish_reason"]
        print(f"REASON {finish_reason}")
        if(finish_reason == "stop"):
            if("text" in choice):
                solution_set.add(choice["text"])
            shutil.copyfile(path, f"{out_dir}/question.txt")
            prompt_file_folder = os.path.dirname(path)
            try:
                shutil.copyfile(f"{prompt_file_folder}/metadata.json", f"{out_dir}/metadata.json")
                shutil.copyfile(f"{prompt_file_folder}/solutions.json", f"{out_dir}/solutions.json")
                shutil.copyfile(f"{prompt_file_folder}/input_output.json", f"{out_dir}/input_output.json")
            except Exception as e:
                print(path, e)

            # shutil.copyfile(path, f"{out_dir}/solutions.json")
            # shutil.copyfile(path, f"{out_dir}/input_output.json")
            # with open(f"{out_dir}/gen_code_out_{i}.py", "w") as fp:
                # fp.write(choice["text"])
    
    output["solutions"].extend(solution_set)



    with open(f'{out_dir}/codex_solutions.json', 'w') as outfile:
        json.dump(output["solutions"], outfile)
    



if __name__ == "__main__":
    #Example: python3 ./test/0179/question.txt
    path = sys.argv[1] #test/sort-questions.txt_dir/4997/question.txt
    out_dir = sys.argv[2] #davinci_runs/test/sort-questions.txt_dir
    TEMPERATURE = float(sys.argv[3])
    N_SOLUTIONS = int(sys.argv[4])
    SLEEP_TIME_SECONDS = float(sys.argv[5])

    print(f"run_davinci.py {path} {out_dir} {TEMPERATURE} {N_SOLUTIONS}")

    # split_parts = prompt_file_path.split('/')
    # num = split_parts[2]
    
    # print(f"num: {num}")

    # out_dir = f"davinci_runs/{type_of_sample}/{num}"
    # os.makedirs(out_dir, exist_ok=True)

    sys.stdout = open(f'{out_dir}/out.log', 'w')
    run_davinci(path, out_dir)
    sys.stdout.close()