# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.br_apiv1_documentation_link_dto import BrAPIv1DocumentationLinkDTO

class TestBrAPIv1DocumentationLinkDTO(unittest.TestCase):
    """BrAPIv1DocumentationLinkDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrAPIv1DocumentationLinkDTO:
        """Test BrAPIv1DocumentationLinkDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrAPIv1DocumentationLinkDTO`
        """
        model = BrAPIv1DocumentationLinkDTO()
        if include_optional:
            return BrAPIv1DocumentationLinkDTO(
                type = '',
                url = ''
            )
        else:
            return BrAPIv1DocumentationLinkDTO(
        )
        """

    def testBrAPIv1DocumentationLinkDTO(self):
        """Test BrAPIv1DocumentationLinkDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
