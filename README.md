## Freddy
Freddy is a multi-purpose discord bot, originally created in 2018. Made with Python  

### Installation
Requirements:
- Clone or download the repository https://github.com/devharry20/Freddy
- Create a `.env` file and fill it with the following contents

```
TOKEN='your bot token'
```
You will also need to edit [config.py](https://github.com/devharry20/Freddy/blob/master/freddy/utils/config.py) and change some of the settings  

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
  
  ![Help Command](https://i.gyazo.com/78fd070e14f090cd049ff6ef6b9161b9.png)
