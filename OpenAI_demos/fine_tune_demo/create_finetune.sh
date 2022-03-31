#!/bin/bash
#usage ./create_finetune.sh "<base_model_name>"
#uses dummy.json as dummy input.
openai api fine_tunes.create -t dummy.json -m "$1"