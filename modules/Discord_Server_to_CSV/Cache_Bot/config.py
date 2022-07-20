import os

def Config():
    config={
            "token":'OTY3Mjc0MjAzNjUwODYzMTA0.YmN6TQ.XKsFaC4PtW7GkBFXnTtYJC0OKoE',
            "command_pref":"!!",
            "permissions":8,
            "output_url" : f'{os.path.dirname(os.path.realpath(__name__))}/Output_CSVs'
            }
    return config

