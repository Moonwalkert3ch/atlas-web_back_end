#!/usr/bin/env python3
"""Class to check the githuborgclient functions"""
import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json
import utils
import requests
import client


class TestGithubOrgClient(unittest.TestCase):
    """Class that implements the test_org method"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('utils.get_json', return_value={"url": "https://api.github.com/orgs/"})
    def test_org(self, org_name, mock_get):
        """Tests that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        result = client.org
        expected_url = f"https://api.github.com/orgs/{org_name}"

        mock_get.assert_called_once_with(expected_url)
        self.assertEqual(result, mock_get.return_value)
