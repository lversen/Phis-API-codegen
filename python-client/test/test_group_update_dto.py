# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.group_update_dto import GroupUpdateDTO

class TestGroupUpdateDTO(unittest.TestCase):
    """GroupUpdateDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupUpdateDTO:
        """Test GroupUpdateDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupUpdateDTO`
        """
        model = GroupUpdateDTO()
        if include_optional:
            return GroupUpdateDTO(
                uri = 'http://opensilex.dev/groups#Experiment_manager',
                rdf_type = '',
                rdf_type_name = '',
                name = 'Experiment manager',
                description = 'Group for all experiments managers',
                user_profiles = [
                    openapi_client.models.group_user_profile_dto.GroupUserProfileDTO(
                        uri = 'http://opensilex.dev/groups#Experiment_manager', 
                        rdf_type = '', 
                        rdf_type_name = '', 
                        profile_uri = '', 
                        profile_name = '', 
                        user_uri = '', 
                        user_name = '', 
                        publication_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_updated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                publication_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return GroupUpdateDTO(
                uri = 'http://opensilex.dev/groups#Experiment_manager',
                name = 'Experiment manager',
                description = 'Group for all experiments managers',
        )
        """

    def testGroupUpdateDTO(self):
        """Test GroupUpdateDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
