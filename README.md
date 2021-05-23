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
#### Current state of commands    
![Help Command](https://i.gyazo.com/3f1288b84d515c3197870b0f1d11765d.png)
