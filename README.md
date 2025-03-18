# assignment-2
## BMI Calculator: A TDD and boundary testing exercise

### Instructions:

#### Run application (without environment):
To run the application without building the environment,
1. (on Windows) simply download the `bmi_calculator.exe` file from this repository.
2. Start a cli such as `powershell` or `cmd`. (Win + R, "cmd")
3. Navigate to the downloaded executable in the cli using `cd`. (`cd Downloads`)
4. Run the executable. (`bmi_calculator.exe --weight <weight_lb> --height <height_in>`)

#### Building the environment
1. Start a cli such as `powershell` or `cmd`. (Win + R, "cmd")
2. Run the following commands:
    ```
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe   -o .\miniconda.exe
    start /wait "" .\miniconda.exe /S
    del .\miniconda.exe
    ```
3. Navigate to the downloaded repository from the command prompt.
4. Setup the environment
    ```
    conda env create -f environment.yml
    ```
5. Activate the environment
    ```
    conda activate assignment-2
    ```

#### Run source code (with environment):
1. Start a cli such as `powershell` or `cmd`. (Win + R, "cmd")
2. Navigate to the downloaded repository from the command prompt.
3. Activate the environment
    ```
    conda activate assignment-2
    ```
4. Run the application
    ```
    python bmi_calculator.py --weight <weight_lb> --height <height_in>
    ```

#### Run unit tests (with environment):
1. Start a cli such as `powershell` or `cmd`. (Win + R, "cmd")
2. Navigate to the downloaded repository from the command prompt.
3. Activate the environment
    ```
    conda activate assignment-2
    ```
4. Run the unit tests
    ```
    pytest
    ```
