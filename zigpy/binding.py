import asyncio
import functools
import logging
import random
import time
from typing import Iterator, List, Optional

import zigpy.exceptions
import zigpy.types
from zigpy.typing import DeviceType
import zigpy.util
import zigpy.zdo.types
import zigpy.application


LOGGER = logging.getLogger(__name__)
BindingListType = List[zigpy.zdo.types.Binding]
REQUEST_DELAY = (1.0, 1.5)


class RequestBinding:
    def __init__(self, src_address
                 , src_endPoint
                 , cluster_id
                 , dst_address
                 , device):
        self._src_address = src_address
        self._src_end_point = src_endPoint
        self._cluster_id = cluster_id
        self._dst_address = dst_address
        self._binding: BindingListType = []
        self._device = device

    async def scan(self):

        idx = 0

        while True:
            status, rsp = await self._device.zdo.Mgmt_Bind_req(idx, tries=3, delay=1)
            if status != zigpy.zdo.types.Status.SUCCESS:
                self.debug("does not support 'Mgmt_Bind_req'")
                return
            """
            app = zigpy.application.ControllerApplication
            cluster = "i don't know how to get the cluster of the device"

            dst_address = app.get_dst_address(cluster)

            return status, dst_address
            """

    @property
    def get_binding(self):
        return self._binding

    def get_src_address(self):
        return self._src_address

    def get_src_endpoint(self):
        return self._src_end_point

    def get_cluster_id(self):
        return self._cluster_id

    def get_dst_address(self):
        return self._dst_address
