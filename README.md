# LyreBot: A Discord Mimicy Machine
## Description:

A discord bot capable of mimicing users within the channel. 
TODO: expand this

## Usage:
TODO: make this usable


## Project structure:
```
.
├── environment.yml
├── main.py
├── README.md
└── src
    ├── bot.py
    ├── data
    ├── fine_tune.py
    ├── inference.py
    ├── __init__.py
    ├── models
    └── scraper.py
```
The bot consists of the following modules:\
* `main.py`: script used to launch LyreBot (handles all other scripts).
* `bot.py`: the core functionality that juggles scraping, tuning, and inference.
* `fine_tune.py`: fine-tunes a model weights based on a users prior messages
* `inference.py`: generates a response in the voice of the specified user.

Additionally, two folders exist that are specific to your instanc: `models` contains models tuned to individual users 
and `data` contains scraped messages. (todo: encrypt saved messages)
