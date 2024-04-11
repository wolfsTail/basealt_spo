"""
This module provides functionalities to fetch binary package data 
from API endpoint.
"""
import requests


class PackageFetcher:
        """
        Fetch binary package data from API.

        Parameters:
            branch (str): The name of the branch to fetch binary packages for.

        Returns:
            dict: A dict containing the binary package data.
            None: If request to API fails or returns bad response.
        """

        API_URL = "https://rdb.altlinux.org/api/export/branch_binary_packages/"

        @classmethod
        def get_binary_packages(cls, branch_name):
            """
            Fetch binary package data from API.

            Parameters:
                branch (str): The name of the branch to fetch binary packages for.
                
        Returns:
            dict: A dict containing the binary package data.
            None: If request to API fails or returns bad response.
            """
            url = cls.API_URL + branch_name
            response = requests.get(url)

            if response.status_code == 200:
                  return response.json()

            return None               
