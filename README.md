# VSNotes Tag Checker

This program is designed to solve the issue of indexing not completing due to tag notation errors when using VSNotes. It checks if the files in the specified folder conform to the VSNotes tag format and prints out the filenames if there are any anomalies.

## Usage

1. **Install Python**:
   This program is written in Python. If you don't have Python installed, download and install it from the official Python website.

2. **Download the Program**:
   Download `tagcheck.py` and save it to a directory of your choice.

3. **Set Command Line Arguments in VSCode**:
   If you are using VSCode, you can set command line arguments using the `launch.json` file. Here is an example:

   ```json
   {
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Python: Current File",
               "type": "python",
               "request": "launch",
               "program": "${file}",
               "console": "integratedTerminal",
               "args": ["YOUR FOLDER PATH HERE"]
           }
       ]
   }
   ```

4. **Run the Program in VSCode**:
   Select the configuration (e.g., "Python: Current File") in the debug view and start debugging. This will pass the specified folder path as an argument to the script.

5. **Run the Program from Command Prompt or Terminal**:
   Open your command prompt or terminal and navigate to the directory where `vsnotetagcheck.py` is saved. Then execute the following command:

   ```sh
   python3 tagcheck.py <folder_path>
   ```
## Program Description
This program checks files based on the following rules:

1. There are exactly two '---' before the first line starting with '#'.
2. There is exactly one 'tags:' between the two '---'.
3. There are lines starting with '- ' between 'tags:' and the second '---', and all these lines have the same indentation.
4. Lines starting with '- ' must have visible characters after '- '.
If any file does not follow these rules, its filename will be printed out.

## Notes
- Empty files are not processed.
- Files and folders starting with '.' are skipped.

## License
This project is licensed under the MIT License. See the LICENSE file for details.