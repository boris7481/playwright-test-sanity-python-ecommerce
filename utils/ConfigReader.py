from pathlib import Path
import configparser

config = configparser.ConfigParser()

path_config_ini = (
    Path(__file__).resolve().parent.parent / "configurations" / "config.ini"
)
config.read(path_config_ini)


class ReadConfig:
    @staticmethod
    def get_property(key):
        return config.get("QA", key)
