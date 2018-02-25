import subprocess
import os


BASH_PATH = os.environ['PROTECTOR_BASH_PATH']
SCRIPT_PATH = os.environ['PROTECTOR_SCRIPT_PATH']


class ScriptRunner():


    def run():

        output = subprocess.check_output([BASH_PATH, SCRIPT_PATH])
        return output

