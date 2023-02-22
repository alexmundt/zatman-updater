import configparser

def write_to_config(configfile, database):
    """ function that writes to configfile
    configfile:: string, filename to be written to
    database:: string

    The database string refers to the .xlsx file that should be loaded
    """
    config = configparser.ConfigParser()
    config["Previous Values"] = {"database": database}

    with open(configfile,'w') as file:
        config.write(file)

def load_from_config(configfile):
    """ function that reads the configfile and returns a dictionary with
    keys filename
    configfile:: string
    """
    config= configparser.ConfigParser()
    config.read(configfile)

    prev = config["Previous Values"]
    return prev

def generate_empty_config(configfile):
    """ function that generates an empty configfile if config has been lost
    or modified incorrectly
    configfile:: string, filename to be written to"""

    config = configparser.ConfigParser()
    config["Previous Values"] = {"database": ""}

    with open(configfile,'w') as file:
        config.write(file)
