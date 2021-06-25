from src import initialize_bot
import yaml
if __name__ == "__main__":
    with open("config.yml", "ro") as f:
        config_file = yaml.load(f)
    initialize_bot(config=config_file)