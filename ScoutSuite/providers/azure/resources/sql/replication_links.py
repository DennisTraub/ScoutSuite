# -*- coding: utf-8 -*-

from ..resources import AzureSimpleResources


class ReplicationLinks(AzureSimpleResources):

    def __init__(self, resource_group_name, server_name, database_name, facade):
        self.resource_group_name = resource_group_name
        self.server_name = server_name
        self.database_name = database_name
        self.facade = facade

    # TODO: make it really async.
    async def get_resources_from_api(self):
        return list(self.facade.replication_links.list_by_database(
            self.resource_group_name, self.server_name, self.database_name))

    def parse_resource(self, links):
        self.update({
            'replication_configured': len(links) > 0
        })
