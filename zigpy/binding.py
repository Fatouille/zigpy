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


LOGGER = logging.getLogger(__name__)
BindingListType = List[zigpy.zdo.types.Binding]
REQUEST_DELAY = (1.0, 1.5)


class Bind:
    def __init__(self, binding: zigpy.zdo.types.Binding, device: DeviceType):
        self._device = device
        self._binding = binding

    @property
    def device(self) -> zigpy.typing.DeviceType:
        return self._device

    @property
    def binding(self) -> zigpy.zdo.types.Binding:
        return self._binding


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

    def __getitem__(self, *args, **kwargs) -> Bind:
        """Get item method."""
        return self.get_binding.__getitem__(*args, **kwargs)

    def __setitem__(self, *args, **kwargs) -> None:
        """Set item method."""
        return self.get_binding.__setitem__(*args, **kwargs)

    def __len__(self) -> int:
        """Len item method."""
        return self.get_binding.__len__()

    def __iter__(self) -> Iterator:
        """Iter item method."""
        return self.get_binding.__iter__()

    async def get_status(self):

        idx = 0

        while True:
            status, rsp = await self._device.zdo.Mgmt_Bind_req(idx, tries=3, delay=1)
            if status != zigpy.zdo.types.Status.SUCCESS:
                self.debug("does not support 'Mgmt_Bind_req'")
                return
            return status

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
