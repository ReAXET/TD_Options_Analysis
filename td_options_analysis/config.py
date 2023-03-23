import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="td_options_analysis",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="td_options_analysis_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from td_options_analysis.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export td_options_analysis_KEY=value
export td_options_analysis_KEY="@int 42"
export td_options_analysis_KEY="@jinja {{ this.db.uri }}"
export td_options_analysis_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
td_options_analysis_ENV=production td_options_analysis run
```

Read more on https://dynaconf.com
"""
