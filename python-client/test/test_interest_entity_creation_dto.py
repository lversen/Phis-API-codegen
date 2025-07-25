# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.interest_entity_creation_dto import InterestEntityCreationDTO

class TestInterestEntityCreationDTO(unittest.TestCase):
    """InterestEntityCreationDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InterestEntityCreationDTO:
        """Test InterestEntityCreationDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InterestEntityCreationDTO`
        """
        model = InterestEntityCreationDTO()
        if include_optional:
            return InterestEntityCreationDTO(
                uri = 'http://opensilex.dev/set/variables/entity_of_interest/Plot',
                name = 'Plot',
                description = 'The entity of interest which characterizes a plot',
                exact_match = [
                    ''
                    ],
                close_match = [
                    ''
                    ],
                broad_match = [
                    ''
                    ],
                narrow_match = [
                    ''
                    ]
            )
        else:
            return InterestEntityCreationDTO(
        )
        """

    def testInterestEntityCreationDTO(self):
        """Test InterestEntityCreationDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
