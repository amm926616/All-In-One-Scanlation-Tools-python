import json, os, platform

os_name = platform.system()

roaming_path = ""
if os_name == "Windows": 
	# Set the path to the Roaming folder
	roaming_path = os.getenv('APPDATA')
elif os_name == "Linux":
	config_path = os.path.expanduser("~") + "/.config/EasyPaste-python/"
	if not os.path.exists(config_path):
		os.makedirs(config_path)
	roaming_path = config_path

# Create the directory if it doesn't exist
directory = os.path.join(roaming_path, 'aios')
if not os.path.exists(directory):
    os.makedirs(directory)

# Set the path to the JSON file
json_file_path = os.path.join(directory, 'aios_info.json')

def edit_values(key, value):
	with open(json_file_path, 'r') as f:
		data = json.load(f)
	data[key] = value

	with open(json_file_path, 'w') as f:
		json.dump(data, f)

def read_values():
	with open(json_file_path, 'r') as f:
		data = json.load(f)
		return data

def initial_info_setup():
	if not os.path.exists(json_file_path):
		with open(json_file_path, 'w') as f:
			original_info = {"sub_state":"HAVENTPAIDFORTHEPROGRAMYET", "expired_time":"0"}
			json.dump(original_info, f)