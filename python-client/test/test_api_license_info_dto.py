# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.api_license_info_dto import ApiLicenseInfoDTO

class TestApiLicenseInfoDTO(unittest.TestCase):
    """ApiLicenseInfoDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiLicenseInfoDTO:
        """Test ApiLicenseInfoDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiLicenseInfoDTO`
        """
        model = ApiLicenseInfoDTO()
        if include_optional:
            return ApiLicenseInfoDTO(
                name = 'GNU Affero General Public License v3',
                url = 'https://www.gnu.org/licenses/agpl-3.0.fr.html'
            )
        else:
            return ApiLicenseInfoDTO(
        )
        """

    def testApiLicenseInfoDTO(self):
        """Test ApiLicenseInfoDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
