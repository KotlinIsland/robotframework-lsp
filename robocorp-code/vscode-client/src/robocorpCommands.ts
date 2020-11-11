// Warning: Don't edit file (autogenerated from python -m dev codegen).

export const ROBOCORP_GET_LANGUAGE_SERVER_PYTHON = "robocorp.getLanguageServerPython";  // Get a python executable suitable to start the language server
export const ROBOCORP_GET_PLUGINS_DIR = "robocorp.getPluginsDir";  // Get the directory for plugins
export const ROBOCORP_CREATE_ROBOT = "robocorp.createRobot";  // Create Robot
export const ROBOCORP_LIST_ROBOT_TEMPLATES_INTERNAL = "robocorp.listRobotTemplates.internal";  // Provides a list with the available robot templates
export const ROBOCORP_CREATE_ROBOT_INTERNAL = "robocorp.createRobot.internal";  // Actually calls rcc to create the robot
export const ROBOCORP_UPLOAD_ROBOT_TO_CLOUD = "robocorp.uploadRobotToCloud";  // Upload Robot to the Robocorp Cloud
export const ROBOCORP_LOCAL_LIST_ROBOTS_INTERNAL = "robocorp.localListRobots.internal";  // Lists the activities currently available in the workspace
export const ROBOCORP_IS_LOGIN_NEEDED_INTERNAL = "robocorp.isLoginNeeded.internal";  // Checks if the user is already logged in
export const ROBOCORP_CLOUD_LOGIN = "robocorp.cloudLogin";  // Log in Robocorp Cloud
export const ROBOCORP_CLOUD_LOGIN_INTERNAL = "robocorp.cloudLogin.internal";  // Log in Robocorp Cloud (receives credentials)
export const ROBOCORP_CLOUD_LIST_WORKSPACES_INTERNAL = "robocorp.cloudListWorkspaces.internal";  // Lists the workspaces available for the user (in the Robocorp Cloud)
export const ROBOCORP_UPLOAD_TO_NEW_ROBOT_INTERNAL = "robocorp.uploadToNewRobot.internal";  // Uploads a Robot as a new Robot in the Robocorp Cloud
export const ROBOCORP_UPLOAD_TO_EXISTING_ROBOT_INTERNAL = "robocorp.uploadToExistingRobot.internal";  // Uploads a Robot as an existing Robot in the Robocorp Cloud
export const ROBOCORP_RUN_IN_RCC_INTERNAL = "robocorp.runInRcc.internal";  // Runs a custom command in RCC
export const ROBOCORP_RUN_ROBOT_RCC = "robocorp.runRobotRcc";  // Run Robot
export const ROBOCORP_DEBUG_ROBOT_RCC = "robocorp.debugRobotRcc";  // Debug Robot
export const ROBOCORP_SAVE_IN_DISK_LRU = "robocorp.saveInDiskLRU";  // Saves some data in an LRU in the disk
export const ROBOCORP_LOAD_FROM_DISK_LRU = "robocorp.loadFromDiskLRU";  // Loads some LRU data from the disk
export const ROBOCORP_COMPUTE_ROBOT_LAUNCH_FROM_ROBOCORP_CODE_LAUNCH = "robocorp.computeRobotLaunchFromRobocorpCodeLaunch";  // Computes a robot launch debug configuration based on the robocorp code launch debug configuration
export const ROBOCORP_SET_PYTHON_INTERPRETER = "robocorp.setPythonInterpreter";  // Set the Python extension pythonPath based on the robot.yaml
export const ROBOCORP_RESOLVE_INTERPRETER = "robocorp.resolveInterpreter";  // Resolves the interpreter to be used given a path.