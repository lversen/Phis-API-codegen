# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.faidarev1_scale_dto import Faidarev1ScaleDTO

class TestFaidarev1ScaleDTO(unittest.TestCase):
    """Faidarev1ScaleDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Faidarev1ScaleDTO:
        """Test Faidarev1ScaleDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Faidarev1ScaleDTO`
        """
        model = Faidarev1ScaleDTO()
        if include_optional:
            return Faidarev1ScaleDTO(
                data_type = '',
                decimal_places = '',
                scale_db_id = '',
                name = '',
                valid_values = '',
                xref = ''
            )
        else:
            return Faidarev1ScaleDTO(
        )
        """

    def testFaidarev1ScaleDTO(self):
        """Test Faidarev1ScaleDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
