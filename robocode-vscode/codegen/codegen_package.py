import os.path

from commands import (
    get_activation_events_for_json,
    get_commands_for_json,
    get_keybindings_for_json,
    COMMANDS,
)
from settings import get_settings_for_json, SETTINGS


def convert_case_to_constant(name):
    import re

    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return (
        re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
        .replace(".", "_")
        .replace("-", "_")
        .upper()
    )


def convert_case_to_camel(name):
    import re

    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return (
        re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
        .replace(".", "_")
        .replace("-", "_")
        .upper()
    )


def get_json_contents():
    base_package_contents = {
        "name": "robocode-vscode",
        "displayName": "Robocode VSCode",
        "description": "Extension for Robocode in VSCode",
        "author": "Fabio Zadrozny",
        "homepage": "https://github.com/robocorp/robotframework-lsp/blob/master/robocode-vscode/README.md",
        "repository": {
            "type": "git",
            "url": "https://github.com/robocorp/robotframework-lsp.git",
        },
        "license": "Apache 2.0",
        "version": "0.0.1",
        "icon": "images/icon.png",
        "publisher": "robocorptech",
        "engines": {"vscode": "^1.43.0"},
        "categories": [],
        "activationEvents": get_activation_events_for_json(),
        "contributes": {
            "configuration": {
                "title": "Robocode VSCode Language Server Configuration",
                "type": "object",
                "properties": get_settings_for_json(),
            },
            "languages": [],
            "grammars": [],
            "debuggers": [],
            "keybindings": get_keybindings_for_json(),
            "commands": get_commands_for_json(),
        },
        "main": "./vscode-client/out/extension",
        "scripts": {
            "vscode:prepublish": "cd vscode-client && npm run compile && cd ..",
            "compile": "cd vscode-client && tsc -p ./ && cd ..",
            "watch": "cd vscode-client && tsc -watch -p ./ && cd ..",
            "postinstall": "node ./node_modules/vscode/bin/install",
        },
        "devDependencies": {
            "typescript": "^3.6.4",
            "vscode": "1.1.37",
            "@types/node": "^6.0.40",
            "@types/mocha": "^2.2.32",
        },
        "dependencies": {"vscode-languageclient": "^6.1.3", "path-exists": "^4.0.0"},
    }
    return base_package_contents


def write_to_package_json():
    import json

    json_contents = get_json_contents()
    as_str = json.dumps(json_contents, indent=4)
    root = os.path.dirname(os.path.dirname(__file__))
    package_json_location = os.path.join(root, "package.json")
    with open(package_json_location, "w") as stream:
        stream.write(as_str)
    print("Written: %s" % (package_json_location,))


root_dir = os.path.dirname(os.path.dirname(__file__))
vscode_src_dir = os.path.join(root_dir, "vscode-client", "src")


def write_js_commands():
    commands_ts_file = os.path.join(vscode_src_dir, "robocodeCommands.ts")

    command_constants = []

    for contributed_command in COMMANDS:
        command_id = contributed_command.name
        command_name = convert_case_to_constant(command_id)
        command_constants.append(
            'export const %s = "%s";  // %s'
            % (command_name, command_id, contributed_command.title)
        )

    with open(commands_ts_file, "w") as stream:
        stream.write(
            "// Warning: Don't edit file (autogenerated from python -m dev codegen).\n\n"
            + "\n".join(command_constants)
        )
    print("Written: %s" % (commands_ts_file,))


def write_js_settings():
    settings_ts_file = os.path.join(vscode_src_dir, "robocodeSettings.ts")
    settings_template = [
        """// Warning: Don't edit file (autogenerated from python -m dev codegen).

import { WorkspaceConfiguration, workspace } from "vscode";

export function get<T>(key: string): T | undefined {
    var dot = key.lastIndexOf('.');
    var section = key.substring(0, dot);
    var name = key.substring(dot + 1);
    return workspace.getConfiguration(section).get(name);
}
"""
    ]

    setting_constant_template = 'export const %s = "%s";'

    # Create the constants
    for setting in SETTINGS:
        # : :type setting: Setting
        settings_template.append(
            setting_constant_template
            % (convert_case_to_constant(setting.name), setting.name)
        )

    getter_template = """
export function get%s(): %s {
    let key = %s;
    return get<%s>(key);
}
"""
    # Create the getters
    for setting in SETTINGS:
        js_type = setting.js_type or setting.setting_type
        if js_type == "array":
            raise AssertionError("Expected js_type for array.")
        name = "_".join(setting.name.split(".")[1:])
        name = name.title().replace(" ", "").replace("_", "").replace("-", "")
        settings_template.append(
            getter_template
            % (name, js_type, convert_case_to_constant(setting.name), js_type)
        )

    with open(settings_ts_file, "w") as stream:
        stream.write("\n".join(settings_template))

    print("Written: %s" % (settings_ts_file,))


def main():
    write_to_package_json()
    write_js_commands()
    write_js_settings()


if __name__ == "__main__":
    main()
