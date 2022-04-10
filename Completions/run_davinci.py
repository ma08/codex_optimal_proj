import os
import sys
from numpy import promote_types
import openai
import json
import shutil
import numpy as np

openai.api_key = os.getenv("OPENAI_API_KEY")

ENGINE = "code-davinci-002"
MAX_TOKENS=4000

def run_davinci(path, out_dir, n_itr):
    with open(path) as f:
        prompt = f.read()

    input_prompt = f"\"\"\"\n{prompt}\n\"\"\""
    print(input_prompt)

    print("--------------------------")

    for itr in n_itr:
        TEMPERATURE = np.random.randint(0, 10)/10
        N_SOLUTIONS = np.random.randint(1, 100)

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
                if not os.path.exists(f"{out_dir}/question.txt"):
                    shutil.copyfile(path, f"{out_dir}/question.txt")
                prompt_file_folder = os.path.dirname(path)
                try:
                    if not os.path.exists(f"{out_dir}/metadata.json"):
                        shutil.copyfile(f"{prompt_file_folder}/metadata.json", f"{out_dir}/metadata.json")
                    if not os.path.exists(f"{out_dir}/solutions.json"):
                        shutil.copyfile(f"{prompt_file_folder}/solutions.json", f"{out_dir}/solutions.json")
                    if not os.path.exists(f"{out_dir}/input_output.json"):
                        shutil.copyfile(f"{prompt_file_folder}/input_output.json", f"{out_dir}/input_output.json")
                except Exception as e:
                    print(path, e)

                # shutil.copyfile(path, f"{out_dir}/solutions.json")
                # shutil.copyfile(path, f"{out_dir}/input_output.json")
                # with open(f"{out_dir}/gen_code_out_{i}.py", "w") as fp:
                    # fp.write(choice["text"])
        
        output["solutions"].extend(solution_set)


        pref = str(TEMPERATURE) + 'T1_' + str(N_SOLUTIONS) + 'k1_'
        if not os.path.exists(f"{out_dir}/{pref}codex_solutions.json"):
            with open(f'{out_dir}/{pref}codex_solutions.json', 'w') as outfile:
                json.dump(output["solutions"], outfile)
    


if __name__ == "__main__":
    #Example: python3 ./test/0179/question.txt
    path = sys.argv[1] #test/sort-questions.txt_dir/4997/question.txt
    out_dir = sys.argv[2] #davinci_runs/test/sort-questions.txt_dir
    n_itr = sys.argv[3] # number of times want to sample

    # split_parts = prompt_file_path.split('/')
    # num = split_parts[2]
    
    # print(f"num: {num}")

    # out_dir = f"davinci_runs/{type_of_sample}/{num}"
    # os.makedirs(out_dir, exist_ok=True)

    sys.stdout = open(f'{out_dir}/out.log', 'w')
    run_davinci(path, out_dir, n_itr)
    sys.stdout.close()
