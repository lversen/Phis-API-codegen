# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.credential_dto import CredentialDTO

class TestCredentialDTO(unittest.TestCase):
    """CredentialDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CredentialDTO:
        """Test CredentialDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CredentialDTO`
        """
        model = CredentialDTO()
        if include_optional:
            return CredentialDTO(
                id = '',
                name = ''
            )
        else:
            return CredentialDTO(
        )
        """

    def testCredentialDTO(self):
        """Test CredentialDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
