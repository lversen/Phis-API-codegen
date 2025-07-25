# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.4.7-rdg
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.device_get_dto import DeviceGetDTO

class TestDeviceGetDTO(unittest.TestCase):
    """DeviceGetDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceGetDTO:
        """Test DeviceGetDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceGetDTO`
        """
        model = DeviceGetDTO()
        if include_optional:
            return DeviceGetDTO(
                uri = '',
                rdf_type = 'http://www.opensilex.org/vocabulary/oeso#SensingDevice',
                rdf_type_name = '',
                name = 'Sensor_01',
                brand = 'Campbell',
                constructor_model = 'CS655',
                serial_number = '123456',
                person_in_charge = 'http://opensilex.dev/person#Firstname.Lastname',
                start_up = 'Wed Dec 12 01:00:00 CET 2018',
                removal = 'Sat Dec 12 01:00:00 CET 2020',
                relations = [
                    openapi_client.models.rdf_object_relation_dto.RDFObjectRelationDTO(
                        property = '', 
                        value = '', 
                        inverse = True, )
                    ],
                description = 'description',
                publisher = openapi_client.models.user_get_dto.UserGetDTO(
                    uri = 'http://opensilex.dev/users#jean.michel.inrae', 
                    email = 'jean.michel@example.com', 
                    language = 'en', 
                    admin = False, 
                    first_name = 'Jean', 
                    last_name = 'Michel', 
                    linked_person = 'http://opensilex.dev/person#Jean.Michel.mistea', 
                    enable = True, 
                    favorites = test, ),
                publication_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return DeviceGetDTO(
                name = 'Sensor_01',
        )
        """

    def testDeviceGetDTO(self):
        """Test DeviceGetDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
