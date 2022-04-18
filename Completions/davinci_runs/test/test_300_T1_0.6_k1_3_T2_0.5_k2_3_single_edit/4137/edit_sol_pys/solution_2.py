from datetime import datetime
import re

if __name__ == "__main__":
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
