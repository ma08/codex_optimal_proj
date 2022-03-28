import os
import sys
from numpy import promote_types
import openai
import shutil

openai.api_key = os.getenv("OPENAI_API_KEY")

def run_davinci(path, num, outdir):
    with open(path) as f:
        prompt = f.read()

    input_prompt = f"\"\"\"\n{prompt}\n\"\"\""
    print(input_prompt)

    print("--------------------------")

    response = openai.Completion.create(
    engine="code-davinci-002",
    prompt=input_prompt,
    temperature=0,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    print(response)

    for choice in response["choices"]:
        finish_reason = choice["finish_reason"]
        print(f"REASON {finish_reason}")
        if(finish_reason == "stop"):
            shutil.copyfile(prompt_file_path, f"{out_dir}/question.txt")
            with open(f"{out_dir}/gen_code_out.py", "w") as fp:
                fp.write(choice["text"])


if __name__ == "__main__":
    # prompt_file_path = sys.argv[1]
    prompt_file_path = "search-questions.txt_dir/0201/question.txt"
    num = prompt_file_path.split("/")[1]
    out_dir =f"davinci_runs/{num}"
    os.mkdir(out_dir)
    sys.stdout = open(f'{out_dir}/out.log', 'w')
    run_davinci(prompt_file_path, num, out_dir)
    sys.stdout.close()