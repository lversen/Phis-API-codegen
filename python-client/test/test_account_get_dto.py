# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.account_get_dto import AccountGetDTO

class TestAccountGetDTO(unittest.TestCase):
    """AccountGetDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountGetDTO:
        """Test AccountGetDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountGetDTO`
        """
        model = AccountGetDTO()
        if include_optional:
            return AccountGetDTO(
                uri = 'http://opensilex.dev/users#jean.michel.inrae',
                email = 'jean.michel@example.com',
                admin = False,
                language = 'en',
                enable = True,
                favorites = [
                    ''
                    ],
                linked_person = 'http://opensilex.dev/person#Jean.Michel.mistea',
                person_first_name = '',
                person_last_name = ''
            )
        else:
            return AccountGetDTO(
        )
        """

    def testAccountGetDTO(self):
        """Test AccountGetDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
