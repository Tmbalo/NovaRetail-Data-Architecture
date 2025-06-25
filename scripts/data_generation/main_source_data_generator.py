import subprocess

## Run the customers and products gen script
subprocess.run(['python', 'scripts/data_generation/generate_source_master_data.py'])

## Run other data sources gen script
subprocess.run(['python', 'scripts/data_generation/generate_source_data.py'])