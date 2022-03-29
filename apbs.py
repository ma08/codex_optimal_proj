import glob
import logging
import random
import fnmatch
import numpy as np
import gc
import os
import io

from tqdm import tqdm

import json


def write_json(dataroot, problem_dirs):
  with open('json_data.json', 'w') as outfile:
    for problem_name in tqdm(problem_dirs):
      question_fname = os.path.join(dataroot, problem_name, "question.txt")
      sols_fname = os.path.join(dataroot, problem_name, "solutions.json")
      #outfile.write(json_string)
      # Read the question description
      with open(question_fname, 'r') as f:
        question_str = f.read()
        # Read all the solutions
        with open(sols_fname, 'r') as f:
          sols_str_list = json.load(f)
          for sol_str in sols_str_list:
            # sol_str = reindent_code(sol_str)

            string="{\"prompt\": \""+question_str+"\", \"completion\" : \""+sol_str+"\"} \n"
            outfile.write(string)



problem_dirs=os.listdir("./APPS_subdataset/train/sort-questions.txt_dir")
data_root="./APPS_subdataset/train/sort-questions.txt_dir"
write_json(data_root,problem_dirs)
