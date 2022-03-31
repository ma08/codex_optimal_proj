# Files and folders
- `test` and `train` are subsets extracted from APPS dataset
- `davinci_runs` is the target folder to store the Completions results for different experiments. 
- `run_davinci.py` Calls OpenAI davinci-002 engine API and obtains generated Python code. It takes two commandline arguments. Example `python3 run_davinci.py <./test/0179/question.txt> <davinci_runs/test/overlap.txt_dir/0179>` (path to prompt file and path to output directory)
- `mass_davinci_run.sh` runs davinci engine on all the input prompts available based on parameters such as test/train, limit (right now being set in code)
