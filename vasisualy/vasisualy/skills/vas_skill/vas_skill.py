import os
import sys
from pathlib import Path
import json
from vasisualy.utils import tmp
from fuzzywuzzy import fuzz
class Skill:
    '''Родительский класс для всех "новых" и сторонних навыков.
    :param name: название навыка. Должно быть как название директории, содержащей навык (string).
    :param use_settings: определяет использует ли навык собственные настройки (boolean)
    '''
    tmpdir = tmp
    def __init__(self, name, user_message, use_settings=False, loop=False):
        self.name = name
        self.root = os.path.dirname(os.path.abspath(sys.modules[self.__module__].__file__))  
        self.use_settings = use_settings
        self.loop = loop
        if use_settings:
            self.settings_path = f"{str(Path(self.root))}/{name}.json"
    def run_loop(self):
        if self.loop:
            with open(f"{self.tmpdir}/.skill_lock", 'w') as f:
                f.write(self.name)
    def exit_loop(self):
        if self.loop:
            if os.path.exists(f"{self.tmpdir}/.skill_lock"):
                os.remove(f"{self.tmpdir}/.skill_lock")
    def _get_triggers(self):
        with open(f"{str(Path(self.root))}/{self.name}.trigger") as file:
            triggers = []
            for line in file:
                if "e:" in line:
                    continue
                elif line != "\n":
                    triggers.append(line.replace("\n", ''))
        return triggers
    def _get_exit_triggers(self):
        with open(f"{str(Path(self.root))}/{self.name}.trigger") as file:
            triggers_exit = []
            for line in file:
                if line[:2] == "e:" and line != '\n':
                    triggers_exit.append(line.replace('\n', '').replace("e:", ''))
        return triggers_exit
    @staticmethod
    def _is_triggered(user_message, triggers):
        for trigger in triggers:
            if fuzz.partial_ratio(user_message, trigger) > 75:
                triggered = True
                break
            else:
                triggered = False
        return triggered
    def _is_triggered_to_exit(self, user_message, triggers):
        if self.loop:
            for trigger in triggers:
                if fuzz.partial_ratio(user_message, trigger) > 90:
                    triggered = True
                    break
                else:
                    triggered = False
            return triggered
        else:
            return False
    def _get_settings(self):
        if self.use_settings:
            with open(self.settings_path, "r") as file:
                settings = json.load(file)
            return settings
    def set_parameter(self, parameter, value):
        if self.use_settings:
            settings = self._get_settings()
            settings[parameter] = value
            with open(self.settings_path, "w") as file:
                json.dump(settings, file)
    def get_temp_dir(self):
        return f"{self.tmpdir}/{self.name}"