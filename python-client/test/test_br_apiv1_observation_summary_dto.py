# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.br_apiv1_observation_summary_dto import BrAPIv1ObservationSummaryDTO

class TestBrAPIv1ObservationSummaryDTO(unittest.TestCase):
    """BrAPIv1ObservationSummaryDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrAPIv1ObservationSummaryDTO:
        """Test BrAPIv1ObservationSummaryDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrAPIv1ObservationSummaryDTO`
        """
        model = BrAPIv1ObservationSummaryDTO()
        if include_optional:
            return BrAPIv1ObservationSummaryDTO(
                collector = '',
                observation_db_id = '',
                observation_time_stamp = '',
                observation_variable_db_id = '',
                observation_variable_name = '',
                season = openapi_client.models.br_apiv1_season_dto.BrAPIv1SeasonDTO(
                    season = '', 
                    season_db_id = '', 
                    year = '', ),
                value = ''
            )
        else:
            return BrAPIv1ObservationSummaryDTO(
        )
        """

    def testBrAPIv1ObservationSummaryDTO(self):
        """Test BrAPIv1ObservationSummaryDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
