import os

def Config():
    config={
            "token":'token',
            "command_pref":"!!",
            "permissions":8,
            "output_url" : f'{os.path.dirname(os.path.realpath(__name__))}/Output_CSVs'
            }
    return config

