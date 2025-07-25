# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.factor_creation_dto import FactorCreationDTO

class TestFactorCreationDTO(unittest.TestCase):
    """FactorCreationDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FactorCreationDTO:
        """Test FactorCreationDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FactorCreationDTO`
        """
        model = FactorCreationDTO()
        if include_optional:
            return FactorCreationDTO(
                uri = 'http://opensilex.dev/set/factors#irrigation',
                name = 'Irrigation',
                category = 'http://aims.fao.org/aos/agrovoc/c_5b384c25',
                description = 'Experimental factor about water exposure',
                levels = [
                    openapi_client.models.factor_level_creation_dto.FactorLevelCreationDTO(
                        uri = 'http://opensilex.dev/set/factors#irrigation.ww', 
                        name = 'WW', 
                        description = 'Well watered', )
                    ],
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
                    ],
                experiment = ''
            )
        else:
            return FactorCreationDTO(
                name = 'Irrigation',
                levels = [
                    openapi_client.models.factor_level_creation_dto.FactorLevelCreationDTO(
                        uri = 'http://opensilex.dev/set/factors#irrigation.ww', 
                        name = 'WW', 
                        description = 'Well watered', )
                    ],
        )
        """

    def testFactorCreationDTO(self):
        """Test FactorCreationDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
