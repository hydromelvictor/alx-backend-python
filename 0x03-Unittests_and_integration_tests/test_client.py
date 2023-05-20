#!/usr/bin/env python3
"""
In a new test_client.py file, declare the
TestGithubOrgClient(unittest.TestCase) class
and implement the test_org method.
"""
from typing import Dict
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json
from unittest.mock import patch, Mock, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
    client class test
    """
    @parameterized.expand([
        (google, get_json("https://api.github.com/orgs/{}".format(google))),
        (abc, get_json("https://api.github.com/orgs/{}".format(abc))),
    ])
    @patch.object(GithubOrgClient, 'org')
    def test_org(self, org_name, excepted):
        """
        org method test
        """
        assert GithubOrgClient.org is get_json
        self.assertEqual(GithubOrgClient(org_name).org(), excepted)

    def test_public_repos_url(self):
        """
        public_repos_url test
        """
        with patch('GithubOrgClient.org',
                   new_callable=PropertyMock) as matcher:
            matcher.return_value = Dict()
            myclass = GithubOrgClient("google")
            self.assertEqual(myclass._public_repos_url(), myclass.org())

    @patch('GithubOrgClient.org')
    def test_public_repos(self):
        """
        public_repos test
        """
        pass
