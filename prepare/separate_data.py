import time
import os
start_time = time.time()

script = 'python3 -m bytesep separate --source_type "vocals" --audio_path "data/data_raw" --output_path "data/data_separate"'

os.system(script)

print(time.time() - start_time)