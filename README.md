## Freddy
Freddy is a multi-purpose discord bot, originally created in 2018. Made with Python

### Installation
Requirements:
- Clone or download the repository https://github.com/devharry20/Freddy
- Create a `.env` file and fill it with the following contents

```
TOKEN='your bot token'
```

### Running the project
#### Using docker (recommended)
```
$ docker-compose up
```

#### Without docker
Install poetry
```
$ pip install poetry
```
Install dependencies
```
$ poetry install
```
Run the bot
```
$ poetry run freddy
```