# Virtual Environments
Student: Francisco Javier Torres Zenon
ID     : A01688757

## Installation checklist
To validate the installation of tools, access the following file.

## Activity
In this activity, you will verify that with the `requeriments-310.txt` file we have no issues in a virtual environment created in a `Python 3.10` version.

Previously we had this file `requirements-37.txt`
 But if we tried to install those libraries on Python 3.10 we get something like this:
    <details open>
        ...
    note: This error originates from a subprocess, and is likely not a problem with pip.
    error: subprocess-exited-with-error
    
    × pip subprocess to install build dependencies did not run successfully.
    │ exit code: 1
    ╰─> See above for output.
    
    note: This error originates from a subprocess, and is likely not a problem with pip.
    
    [notice] A new release of pip is available: 23.0.1 -> 23.2
    [notice] To update, run: pip install --upgrade pip
    
</details>    
    
    This means that the package installation was not successful.

Follow the instructions below to do the activity.
### Run the existing notebook
1. Clone the project `https://github.com/Pacozenon/mlopsP1.git` on your local computer.

2. Create a virtual environment with `Python 3.10`
    * Create venv
        ```
        python310 -m venv venv310
        ```

    * Activate the virtual environment (mac/linux)
        ```
        source venv310/bin/activate
        ```
    * Activate the virtual environment (windows)
        ```
        $ venv310/scripts/Activate.ps1
        ```

3. Install libraries
    Run the following command to install the other libraries.
    ```bash
    pip install -r session-3/requirements-37.txt
    ```
    Verify the installation with this command:
    ```bash
    pip freeze
    ```


5. Open the `mlopsp1/session-3/end_to_end_machine_learning_project.ipynb` notebook and click on `Run All`.  
Make sure to change the notebook kernel to `python310` version, and `Run All` cells.  
    If everything was ok, you should be able to see the last cell with this output:
    ```bash
    Predictions:	 [263527.   331884.02 221119.   ... 105722.   213199.   459125.66]

## Deliverable
The file is not going to be uploaded yet, so just keep it until the next session.




