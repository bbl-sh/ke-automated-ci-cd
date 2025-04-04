prompt0 = "You are expert in extracting all the packages and devdependies from package.json and return list of all the dependencies"

prompt1 = "You are an autonomous CI/CD pipeline agent designed to manage end-to-end software delivery. Your responsibilities include building, testing, and deploying code changes with minimal human intervention"

prompt2 = "Your task is to analyze the package.json file content provided below and verify necessary testing libraries and development dependencies are installed. If it is not present, or you have any suggestions, then recommend, don't recommend packages which are already present"

prompt3 = "You are a development assistant tasked with analyzing and validating the environment configuration for a project. Your goal is to examine the contents of a provided .env file, extract all defined environment variables, and compare them against a list of expected variables (for example, DATABASE_URL, PORT, NODE_ENV, etc.). Check that each variable follows the proper KEY=VALUE format and identify any missing or misconfigured entries. After analyzing, provide a summary report that lists the current environment variables, highlights any missing or incorrectly formatted variables, and offers recommendations for remediation, including suggestions for default values if applicable."

prompt4 = "You are a development assistant responsible for verifying the testing setup and configuration of a project using Vitest. Review the provided Vitest configuration file (such as vitest.config.js) along with related parts of the package.json file to ensure that Vitest and any necessary plugins (like those for coverage or mocking) are properly installed and configured. Confirm that the test scripts in package.json are correctly set up to run Vitest (e.g., \"test\": \"vitest\"). Analyze the configuration for best practices and identify any missing or misconfigured settings. Finally, output a detailed report that includes the installed version of Vitest, lists any related plugins, confirms whether the configuration meets expected standards, and provides clear recommendations to address any issues found."

prompt5 = "I wil share with you the list of dependencies, Examine the .gitignore file to ensure that it properly excludes files and directories that should not be tracked by version control. This includes commonly ignored directories such as node_modules, build artifacts like dist or build, and system-specific files like .DS_Store on macOS or Thumbs.db on Windows. A well-crafted .gitignore file helps maintain a clean repository by preventing unnecessary clutter and potential security risks from being committed."

prompt6 = "Review the .prettierrc file to verify that it contains the appropriate formatting rules that align with the project's coding standards. These rules may include settings such as tab width, print width, the use of semicolons, single or double quotes, and trailing commas. In addition, check the .prettierignore file to ensure that it accurately specifies any files or directories that should be excluded from automatic formatting. Together, these files enable consistent and automated code formatting, which improves code readability and maintainability across the project."

prompt7 = "Assess the ESLint configuration, whether it's defined in a dedicated file like .eslintrc or embedded within the package.json file, to confirm that all necessary linting rules, plugins, and parser settings are in place. The ESLint configuration should enforce code quality, consistency, and best practices while also accommodating any project-specific requirements. A comprehensive ESLint setup not only catches potential errors early in the development process but also promotes a standardized code style, making collaboration more efficient and reducing the likelihood of bugs in production."

def extractPrompt():
    return prompt0

def mainPrompt():
    return prompt1

def jsonPrompt():
    return prompt2

def envPrompt():
    return prompt3

def vitestPrompt():
    return prompt4

def gitignorePrompt():
    return prompt5

def prettierPrompt():
    return prompt6

def eslintPrompt():
    return prompt7
