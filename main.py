import os
import re
import json
import shutil
from ai import Action, TargetCondition, TargetType

script_pattern = re.compile(r'"Script (\d+)"')
group_pattern = re.compile(r'"Group (\d+)"')
entry_pattern = re.compile(r'"Entry (\d+)"')

def find_and_edit_files(input_folder, output_folder, target_filename, find_action, find_condition, find_target, action_replace, condition_replace, target_replace):
    # print("find_action = ", find_action)
    # print("find_condition = ", find_condition)
    # print("find_target = ", find_target)
    # print("action_replace = ", action_replace)
    # print("condition_replace = ", condition_replace)
    # print("target_replace = ", target_replace)
    log_objects = []
    
    for folder_path, _, filenames in os.walk(input_folder):
        for file_name in filenames:
            source_path = os.path.join(folder_path, file_name)

            relative_path = os.path.relpath(source_path, input_folder)
            output_path = os.path.join(output_folder, relative_path)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            if file_name == target_filename:
                with open(source_path, 'r', encoding='utf-8') as file:
                    current_file = file.read()

                edited_file, log_objects = edit_file(relative_path, current_file, find_action, find_condition, find_target, action_replace, condition_replace, target_replace, log_objects)
                log_objects = generate_log_structure(log_objects)

                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(edited_file)
            else:
                shutil.copy(source_path, output_path)

        # Check if the folder is empty and copy it
        if not filenames and not os.path.samefile(folder_path, output_folder):
            output_dir = os.path.join(output_folder, os.path.relpath(folder_path, input_folder))
            os.makedirs(output_dir, exist_ok=True)

    log_json_path = os.path.join(output_folder, "log.json")
    with open(log_json_path, 'w', encoding='utf-8') as log_file:
        json.dump(log_objects, log_file, indent=4)

    print(f"Log written to {log_json_path}")

def edit_file(relative_path, file_content, find_action, find_condition, find_target, action_replace, condition_replace, target_replace, log_objects):
    edited_content = file_content

    entry_pattern = re.compile(r'"Action": ' + str(find_action.value) + r',\s*"Action Parameter": \d+,\s*"Flags": \d+,\s*"(\d)\. Case": {\s*"Target Type": ' + str(find_target.value) + r',\s*"Target Condition": ' + str(find_condition.value) + r',\s*"Parameter": \d+\s*}', re.DOTALL)
    
    matches = entry_pattern.finditer(file_content)

    for match in matches:
        start = match.start()
        end = match.end()

        case_number = match.group(1)

        # Searches for the Entry X in which the X. Case was found
        entry_matches = list(re.finditer(r'"Entry (\d+)"', file_content[:start]))
        if entry_matches:
            entry_match = entry_matches[-1]
            entry_number = entry_match.group(1)
                
            # Searches for the Group X in which the Entry X was found
            group_matches = list(re.finditer(r'"Group (\d+)"', file_content[:entry_match.start()]))
            if group_matches:
                group_match = group_matches[-1]
                group_number = group_match.group(1)

                # Searches for the Script X in which the Group X was found
                script_matches = list(re.finditer(r'"Script (\d+)"', file_content[:group_match.start()]))
                if script_matches:
                    script_number = script_matches[-1].group(1)
                else:
                    script_number = None

            else:
                group_number = None
                script_number = None

        else:
            entry_number = None
            group_number = None
            script_number = None
     
        replaced_content = match.group(0)
        replaced_content = replaced_content.replace(str(find_action.value), str(action_replace.value))
        replaced_content = replaced_content.replace(str(find_condition.value), str(condition_replace.value))
        replaced_content = replaced_content.replace(str(find_target.value), str(target_replace.value))
        
        edited_content = edited_content[:start] + replaced_content + edited_content[end:]

        log_entry = {
            "path": relative_path,
            "script": f"Script {script_number}",
            "group": f"Group {group_number}",
            "entry": f"Entry {entry_number}",
            "case": f"{case_number}. Case",
            "original_action": f"{find_action.value} ({find_action.name})",
            "original_condition_type": f"{find_condition.value} ({find_condition.name})",
            "original_target_type": f"{find_target.value} ({find_target.name})",
            "replaced_action": f"{action_replace.value} ({action_replace.name})",
            "replaced_condition_type": f"{condition_replace.value} ({condition_replace.name})",
            "replaced_target_type": f"{target_replace.value} ({target_replace.name})"
        }

        log_objects.append(log_entry)
     
    return edited_content, log_objects

def generate_log_structure(log_objects):
    paths = {}

    for log_entry in log_objects:
        path = log_entry["path"]
        script_name = log_entry["script"]
        group_name = log_entry["group"]
        entry_name = log_entry["entry"]

        if path not in paths:
            paths[path] = {}

        if script_name not in paths[path]:
            paths[path][script_name] = {}

        if group_name not in paths[path][script_name]:
            paths[path][script_name][group_name] = []

        paths[path][script_name][group_name].append({
            "entry": entry_name,
            "case": log_entry["case"],
            "original_action": log_entry["original_action"],
            "original_condition_type": log_entry["original_condition_type"],
            "original_target_type": log_entry["original_target_type"],
            "replaced_action": log_entry["replaced_action"],
            "replaced_condition_type": log_entry["replaced_condition_type"],
            "replaced_target_type": log_entry["replaced_target_type"]
        })

    result = []
    for path, scripts in paths.items():
        path_entry = {
            "path": path,
            "scripts": []
        }
        for script_name, groups in scripts.items():
            script = {
                "script": script_name,
                "groups": []
            }
            for group_name, entries in groups.items():
                group = {
                    "group": group_name,
                    "entries": entries
                }
                script["groups"].append(group)
            path_entry["scripts"].append(script)
        result.append(path_entry)

    return result

if __name__ == "__main__":
    input_folder = "unpacked" # Replace with the actual root folder path
    output_folder = "edited" # Replace with the output folder path
    target_filename = "section_003.json"
    find_action = Action.ADD_AUGMENT_EVASION_BOOST
    find_condition = TargetCondition.AUGMENT_NOT_EQUALS_EVASION_BOOST
    find_target = TargetType.SELF
    action_replace = Action.ADD_AUGMENT_UNUSED
    condition_replace = TargetCondition.AUGMENT_NOT_EQUALS_UNUSED
    target_replace = TargetType.SELF

    find_and_edit_files(input_folder, output_folder, target_filename, find_action, find_condition, find_target, action_replace, condition_replace, target_replace)
