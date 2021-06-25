from src import initialize_bot
import yaml


if __name__ == "__main__":
    with open("config.yml", "r") as f:
        config_file = yaml.load(f)
    initialize_bot()
