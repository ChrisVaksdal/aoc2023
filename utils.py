import os
import requests

class NoInputException(Exception):
    pass

def getSessionCookie() -> str:
    """ Returns the session cookie from the environment variable. """
    return os.environ.get("AOC_SESSION")

def _downloadInput(day: int) -> bool:
    """ Downloads the input file for the given day and saves it in the numbered directory. 
        Returns True if the download was successful, False otherwise.
        Requires the AOC_SESSION environment variable to be set.
    """
    url = f"https://adventofcode.com/2023/day/{day}/input"
    cookies = {"session": getSessionCookie()}
    rsp = requests.get(url, cookies=cookies)
    if rsp.status_code == 200:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, str(day), "input.txt")
        with open(file_path, "w") as f:
            f.write(rsp.text)
        return True
    else:
        print(f"Failed to download input for day {day}")
        return False

def readInput(file="input.txt", day=None) -> list[str]:
    """ Reads the input file and returns a list of strings, one for each line. """
    dir_path = os.getcwd()
    if day != None:
        dir_path = os.path.join(dir_path, str(day))
    file_path = os.path.join(dir_path, file)
    try:
        with open(file_path, "r") as f:
            return f.read().split("\n")
    except FileNotFoundError:
        if file == "input.txt":
            if day == None:
                day = os.path.basename(dir_path)
            if(_downloadInput(int(day))):
                return readInput(file, day=day)
        raise NoInputException(f"Input file not found: '{file_path}'.")

def _create_folder_and_file(day: int) -> bool:
    """ Creates a folder for the given day and an empty input file. Returns True if the folder and file were created, False otherwise."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    day_path = os.path.join(dir_path, str(day))

    if not os.path.exists(day_path):
        os.makedirs(day_path)

    main_file_path = os.path.join(day_path, "main.py")

    if os.path.exists(main_file_path):
        return False
    
    with open(main_file_path, "w") as f:
        with open("template.py", "r") as template:
            f.write(template.read())

    test_file_path = os.path.join(day_path, "test.txt")
    if not os.path.exists(test_file_path):
        with open(test_file_path, "w") as f:
            f.write("")

    return True
        

def readTestInput(file="test.txt", day=None) -> list[str]:
    return readInput(file, day=day)
