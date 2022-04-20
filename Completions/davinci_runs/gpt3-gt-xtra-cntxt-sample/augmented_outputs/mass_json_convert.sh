for problem in */; do
	for prompt in $problem*/; do
		python3 convert2json.py $prompt;
	done;
done
