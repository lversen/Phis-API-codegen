# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.faidarev1_trial_dto import Faidarev1TrialDTO

class TestFaidarev1TrialDTO(unittest.TestCase):
    """Faidarev1TrialDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Faidarev1TrialDTO:
        """Test Faidarev1TrialDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Faidarev1TrialDTO`
        """
        model = Faidarev1TrialDTO()
        if include_optional:
            return Faidarev1TrialDTO(
                active = True,
                additional_info = openapi_client.models.faidarev1_trial_additional_info_dto.Faidarev1TrialAdditionalInfoDTO(
                    short_name = '', 
                    description = '', 
                    financial_funding = '', 
                    related_projects = [
                        ''
                        ], 
                    coordinators = [
                        openapi_client.models.faidarev1_contact_dto.Faidarev1ContactDTO(
                            contact_db_id = '', 
                            email = '', 
                            institution_name = '', 
                            name = '', 
                            orcid = '', 
                            type = '', )
                        ], ),
                documentation_url = '',
                end_date = '',
                start_date = '',
                trial_name = '',
                trial_db_id = '',
                trial_type = '',
                dataset_authorship = openapi_client.models.faidarev1_dataset_authorship_dto.Faidarev1DatasetAuthorshipDTO(
                    license = '', 
                    dataset_pui = '', ),
                studies = [
                    openapi_client.models.faidarev1_study_summary_dto.Faidarev1StudySummaryDTO(
                        location_db_id = '', 
                        study_db_id = '', 
                        location_name = '', 
                        study_name = '', )
                    ],
                contacts = [
                    openapi_client.models.faidarev1_contact_dto.Faidarev1ContactDTO(
                        contact_db_id = '', 
                        email = '', 
                        institution_name = '', 
                        name = '', 
                        orcid = '', 
                        type = '', )
                    ],
                program_db_id = '',
                program_name = ''
            )
        else:
            return Faidarev1TrialDTO(
        )
        """

    def testFaidarev1TrialDTO(self):
        """Test Faidarev1TrialDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
