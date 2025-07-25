# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.organization_update_dto import OrganizationUpdateDTO

class TestOrganizationUpdateDTO(unittest.TestCase):
    """OrganizationUpdateDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationUpdateDTO:
        """Test OrganizationUpdateDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationUpdateDTO`
        """
        model = OrganizationUpdateDTO()
        if include_optional:
            return OrganizationUpdateDTO(
                uri = '',
                rdf_type = '',
                name = '',
                parents = [
                    ''
                    ],
                groups = [
                    ''
                    ],
                facilities = [
                    ''
                    ],
                rdf_type_name = '',
                publication_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return OrganizationUpdateDTO(
                uri = '',
        )
        """

    def testOrganizationUpdateDTO(self):
        """Test OrganizationUpdateDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
