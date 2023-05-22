#!/usr/bin/env python3
"""
In a new test_client.py file, declare the
TestGithubOrgClient(unittest.TestCase) class
and implement the test_org method.
"""
from typing import Dict
import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from utils import get_json
from unittest.mock import patch, Mock, PropertyMock
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    client class test
    """
    @parameterized.expand([
        (google, get_json("https://api.github.com/orgs/{}".format(google))),
        (abc, get_json("https://api.github.com/orgs/{}".format(abc))),
    ])
    @patch.object('client.get_json')
    def test_org(self, org_name, excepted):
        """
        org method test
        """
        assert GithubOrgClient.org is get_json
        self.assertEqual(GithubOrgClient(org_name).org, excepted)

    @parameterized.expand([
        ("strick", {"repos_url": "https://strickrepos.com"})
    ])
    def test_public_repos_url(self, name, repos):
        """
        public_repos_url test
        """
        with patch('GithubOrgClient.org',
                   new_callable=PropertyMock) as matcher:
            matcher.return_value = repos["repos_url"]
            myclass = GithubOrgClient(name)
            self.assertEqual(myclass._public_repos_url(),
                             repos.get("repos_url"))
            matcher.assert_called_once_with()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, excepted):
        """
        has license
        """
        myclass = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(myclass, excepted)


@parameterized_class(
    (org_payload, repos_payload, expected_repos, apache2_repos),
    TEST_PAYLOAD
    )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    integration test for GithubOrgClient
    """

    def setUpClass(self):
        """setupclass"""
        requests = Mock()
        with patch('requests.get', side_effect=KeyError) as get_patcher:
            url = org_payload
            requests.get(url).json()
    
    def tearDownClass(self):
        """teardownclass"""
        self.setUpClass.get_patcher.stop()
