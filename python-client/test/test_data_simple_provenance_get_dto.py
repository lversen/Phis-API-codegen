# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.data_simple_provenance_get_dto import DataSimpleProvenanceGetDTO

class TestDataSimpleProvenanceGetDTO(unittest.TestCase):
    """DataSimpleProvenanceGetDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataSimpleProvenanceGetDTO:
        """Test DataSimpleProvenanceGetDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataSimpleProvenanceGetDTO`
        """
        model = DataSimpleProvenanceGetDTO()
        if include_optional:
            return DataSimpleProvenanceGetDTO(
                uri = '',
                rdf_type = '',
                name = ''
            )
        else:
            return DataSimpleProvenanceGetDTO(
        )
        """

    def testDataSimpleProvenanceGetDTO(self):
        """Test DataSimpleProvenanceGetDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
