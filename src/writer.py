"""
This module save the results to a JSON file.

Functions:
    save_results: saves data into a JSON file.
"""

import json



def save_results(file_name, data):
    """
    Save the results to a JSON file.

    Parameters:
        file_name (str): the name of file
        data (dict): the data to be saved into the file.

    Returns:
        None

    Function write data into file in JSON format and print
    a message to the console.
    """
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=3)
    print(f"Completed. Result saved in '{file_name}'.")