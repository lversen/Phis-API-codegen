# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.menu_item_dto import MenuItemDTO

class TestMenuItemDTO(unittest.TestCase):
    """MenuItemDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MenuItemDTO:
        """Test MenuItemDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MenuItemDTO`
        """
        model = MenuItemDTO()
        if include_optional:
            return MenuItemDTO(
                id = 'users',
                label = 'Users',
                children = [
                    openapi_client.models.menu_item_dto.MenuItemDTO(
                        id = 'users', 
                        label = 'Users', 
                        children = [
                            openapi_client.models.menu_item_dto.MenuItemDTO(
                                id = 'users', 
                                label = 'Users', 
                                children = [
                                    
                                    ], 
                                route = openapi_client.models.route_dto.RouteDTO(
                                    path = '/users', 
                                    component = 'opensilex.AccountList', 
                                    credentials = [
                                        ''
                                        ], 
                                    icon = 'ik#ik-target', 
                                    title = 'component.menu.scientificObjects', 
                                    description = 'ScientificObjectList.description', 
                                    rdf_type = 'vocabulary:ScientificObject', ), )
                            ], 
                        route = openapi_client.models.route_dto.RouteDTO(
                            path = '/users', 
                            component = 'opensilex.AccountList', 
                            icon = 'ik#ik-target', 
                            title = 'component.menu.scientificObjects', 
                            description = 'ScientificObjectList.description', 
                            rdf_type = 'vocabulary:ScientificObject', ), )
                    ],
                route = openapi_client.models.route_dto.RouteDTO(
                    path = '/users', 
                    component = 'opensilex.AccountList', 
                    credentials = [
                        ''
                        ], 
                    icon = 'ik#ik-target', 
                    title = 'component.menu.scientificObjects', 
                    description = 'ScientificObjectList.description', 
                    rdf_type = 'vocabulary:ScientificObject', )
            )
        else:
            return MenuItemDTO(
                id = 'users',
                label = 'Users',
                children = [
                    openapi_client.models.menu_item_dto.MenuItemDTO(
                        id = 'users', 
                        label = 'Users', 
                        children = [
                            openapi_client.models.menu_item_dto.MenuItemDTO(
                                id = 'users', 
                                label = 'Users', 
                                children = [
                                    
                                    ], 
                                route = openapi_client.models.route_dto.RouteDTO(
                                    path = '/users', 
                                    component = 'opensilex.AccountList', 
                                    credentials = [
                                        ''
                                        ], 
                                    icon = 'ik#ik-target', 
                                    title = 'component.menu.scientificObjects', 
                                    description = 'ScientificObjectList.description', 
                                    rdf_type = 'vocabulary:ScientificObject', ), )
                            ], 
                        route = openapi_client.models.route_dto.RouteDTO(
                            path = '/users', 
                            component = 'opensilex.AccountList', 
                            icon = 'ik#ik-target', 
                            title = 'component.menu.scientificObjects', 
                            description = 'ScientificObjectList.description', 
                            rdf_type = 'vocabulary:ScientificObject', ), )
                    ],
        )
        """

    def testMenuItemDTO(self):
        """Test MenuItemDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
