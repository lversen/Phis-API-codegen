# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.faidarev1_study_list_response import Faidarev1StudyListResponse

class TestFaidarev1StudyListResponse(unittest.TestCase):
    """Faidarev1StudyListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Faidarev1StudyListResponse:
        """Test Faidarev1StudyListResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Faidarev1StudyListResponse`
        """
        model = Faidarev1StudyListResponse()
        if include_optional:
            return Faidarev1StudyListResponse(
                metadata = openapi_client.models.metadata_dto.MetadataDTO(
                    pagination = openapi_client.models.pagination_dto.PaginationDTO(
                        page_size = 56, 
                        current_page = 56, 
                        total_count = 56, 
                        total_pages = 56, 
                        limit_count = 56, 
                        has_next_page = True, ), 
                    status = [
                        openapi_client.models.status_dto.StatusDTO(
                            message = '', 
                            translation_key = '', 
                            translation_values = {
                                'key' : ''
                                }, 
                            level = 'ERROR', )
                        ], 
                    datafiles = [
                        ''
                        ], ),
                result = openapi_client.models.brapi_data_response_part_list_faidarev1_study_dto.BrapiDataResponsePartListFaidarev1StudyDTO(
                    data = [
                        openapi_client.models.faidarev1_study_dto.Faidarev1StudyDTO(
                            active = '', 
                            additional_info = {
                                'key' : ''
                                }, 
                            documentation_url = '', 
                            end_date = '', 
                            location_db_id = '', 
                            location_name = '', 
                            last_update = openapi_client.models.faidarev1_last_update_dto.Faidarev1LastUpdateDTO(
                                timestamp = '', 
                                version = '', ), 
                            name = '', 
                            program_db_id = '', 
                            program_name = '', 
                            start_date = '', 
                            study_type = '', 
                            study_db_id = '', 
                            study_name = '', 
                            trial_db_id = '', 
                            trial_name = '', 
                            trial_db_ids = [
                                ''
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
                            data_links = [
                                openapi_client.models.faidarev1_data_link_dto.Faidarev1DataLinkDTO(
                                    data_link_name = '', 
                                    name = '', 
                                    type = '', 
                                    url = '', )
                                ], 
                            study_description = '', 
                            seasons = [
                                ''
                                ], 
                            observation_variable_db_ids = [
                                ''
                                ], 
                            germplasm_db_ids = [
                                ''
                                ], )
                        ], )
            )
        else:
            return Faidarev1StudyListResponse(
        )
        """

    def testFaidarev1StudyListResponse(self):
        """Test Faidarev1StudyListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
