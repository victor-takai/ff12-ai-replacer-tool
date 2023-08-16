import os
import re
import json
import shutil
from ai import Action, TargetCondition, TargetType

def find_and_edit_files(input_folder, output_folder, target_filename, find_action, find_condition, find_target, action_replace, condition_replace, target_replace):
    print("find_action = ", find_action)
    print("find_condition = ", find_condition)
    print("find_target = ", find_target)
    print("action_replace = ", action_replace)
    print("condition_replace = ", condition_replace)
    print("target_replace = ", target_replace)
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

                edited_file, log_objects = edit_file(current_file, source_path, input_folder, output_folder, find_action, find_condition, find_target, action_replace, condition_replace, target_replace, log_objects)

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

def edit_file(file_content, source_path, input_folder, output_folder, find_action, find_condition, find_target, action_replace, condition_replace, target_replace, log_objects):
    edited_content = file_content

    entry_pattern = re.compile(r'"Action": ' + str(find_action.value) + r',\s*"Action Parameter": \d+,\s*"Flags": \d+,\s*"(\d)\. Case": {\s*"Target Type": ' + str(find_target.value) + r',\s*"Target Condition": ' + str(find_condition.value) + r',\s*"Parameter": \d+\s*}', re.DOTALL)
    
    matches = entry_pattern.finditer(edited_content)

    log_entries_by_script_group_entry = {}

    for match in matches:
        case_number = match.group(1)
        group_match = re.search(r'"Group (\d+)"', edited_content[:match.start()])
        if group_match:
            group_number = group_match.group(1)
        else:
            group_number = None
        
        script_match = re.search(r'"Script (\d+)"', edited_content[:match.start()])
        if script_match:
            script_number = script_match.group(1)
        else:
            script_number = None

        entry_match = re.search(r'"Entry (\d+)"', edited_content[:match.start()])
        if entry_match:
            entry_number = entry_match.group(1)
        else:
            entry_number = None

        start = match.start()
        end = match.end()
        
        replaced_content = match.group(0)
        replaced_content = replaced_content.replace(str(find_action.value), str(action_replace.value))
        replaced_content = replaced_content.replace(str(find_condition.value), str(condition_replace.value))
        replaced_content = replaced_content.replace(str(find_target.value), str(target_replace.value))
        
        edited_content = edited_content[:start] + replaced_content + edited_content[end:]

        log_entry = {
            "entry": f"Entry {entry_number}",
            "case": f"{case_number}. Case",
            "original_action": f"{find_action.value} ({find_action.name})",
            "original_condition_type": f"{find_condition.value} ({find_condition.name})",
            "original_target_type": f"{find_target.value} ({find_target.name})",
            "replaced_action": f"{action_replace.value} ({action_replace.name})",
            "replaced_condition_type": f"{condition_replace.value} ({condition_replace.name})",
            "replaced_target_type": f"{target_replace.value} ({target_replace.name})"
        }

        script_group_entry_key = (script_number, group_number, entry_number)
        if script_group_entry_key not in log_entries_by_script_group_entry:
            log_entries_by_script_group_entry[script_group_entry_key] = []
        log_entries_by_script_group_entry[script_group_entry_key].append(log_entry)

    log_objects = []
    for (script_number, group_number, entry_number), entries in log_entries_by_script_group_entry.items():
        log_group = {
            "group": f"Group {group_number}",
            "entries": entries
        }

        script_group_key = (script_number, group_number)
        found = False
        for script_group in log_objects:
            if script_group["script"] == f"Script {script_number}":
                script_group["groups"].append(log_group)
                found = True
                break
        if not found:
            log_objects.append({
                "path": source_path.replace(input_folder, output_folder),
                "script": f"Script {script_number}",
                "groups": [log_group]
            })

    return edited_content, log_objects

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
