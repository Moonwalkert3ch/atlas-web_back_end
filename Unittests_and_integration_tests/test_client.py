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
   @patch('client.get_json', Mock())
    def test_org(self, org_name, mock_get_json):
        """Tests that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        result = client.org
        expected_url = f"https://api.github.com/orgs/{org_name}"

        mock_get_json.assert_called_once_with(expected_url)
        self.assertIsNotNone(result)

    def test_public_repos_url(self):
        """ test that _public_repos_url works """
        expected = "www.yes.com"
        payload = {"repos_url": expected}
        payload_mock = 'client.GithubOrgClient.org'
        with patch(payload_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("x")
            self.assertEqual(cli._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Tests that public_repos returns the correct list of repos"""
        expected_repos_url = "https://api.github.com/orgs/test_org/repos"
        mock_repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = mock_repos_payload

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = expected_repos_url

            client = GithubOrgClient("test_org")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(expected_repos_url)
