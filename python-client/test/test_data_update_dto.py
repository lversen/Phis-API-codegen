# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.data_update_dto import DataUpdateDTO

class TestDataUpdateDTO(unittest.TestCase):
    """DataUpdateDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataUpdateDTO:
        """Test DataUpdateDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataUpdateDTO`
        """
        model = DataUpdateDTO()
        if include_optional:
            return DataUpdateDTO(
                uri = 'http://opensilex.dev/id/data/1598857852858',
                var_date = '2020-08-21T00:00:00+01:00',
                timezone = '',
                target = 'http://plot01',
                variable = 'http://opensilex.dev/variable#variable.2020-08-21_11-21-23entity6_method6_quality6_unit6',
                value = 8.6,
                confidence = 0.5,
                provenance = openapi_client.models.data_provenance_model.DataProvenanceModel(
                    uri = 'http://opensilex.dev/id/provenance/provenancelabel', 
                    prov_used = [
                        openapi_client.models.prov_entity_model.ProvEntityModel(
                            uri = '', 
                            rdf_type = '', )
                        ], 
                    prov_was_associated_with = [
                        openapi_client.models.prov_entity_model.ProvEntityModel(
                            uri = '', 
                            rdf_type = '', )
                        ], 
                    settings = {
                        'key' : None
                        }, 
                    experiments = [
                        ''
                        ], ),
                metadata = { "LabelView" : "side90",
"paramA" : "90"},
                raw_data = [
                    None
                    ]
            )
        else:
            return DataUpdateDTO(
                uri = 'http://opensilex.dev/id/data/1598857852858',
                var_date = '2020-08-21T00:00:00+01:00',
                variable = 'http://opensilex.dev/variable#variable.2020-08-21_11-21-23entity6_method6_quality6_unit6',
                value = 8.6,
                provenance = openapi_client.models.data_provenance_model.DataProvenanceModel(
                    uri = 'http://opensilex.dev/id/provenance/provenancelabel', 
                    prov_used = [
                        openapi_client.models.prov_entity_model.ProvEntityModel(
                            uri = '', 
                            rdf_type = '', )
                        ], 
                    prov_was_associated_with = [
                        openapi_client.models.prov_entity_model.ProvEntityModel(
                            uri = '', 
                            rdf_type = '', )
                        ], 
                    settings = {
                        'key' : None
                        }, 
                    experiments = [
                        ''
                        ], ),
        )
        """

    def testDataUpdateDTO(self):
        """Test DataUpdateDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
