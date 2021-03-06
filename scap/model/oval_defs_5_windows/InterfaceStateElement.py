# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

from scap.model.oval_defs_5.StateType import StateType
import logging

logger = logging.getLogger(__name__)
class InterfaceStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'interface_state',
        'elements': [
            {'tag_name': 'name', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'index', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0},
            {'tag_name': 'type', 'class': 'EntityStateInterfaceTypeType', 'min': 0},
            {'tag_name': 'hardware_addr', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'inet_addr', 'class': 'oval_defs_5.EntityStateIPAddressStringType', 'min': 0},
            {'tag_name': 'broadcast_addr', 'class': 'oval_defs_5.EntityStateIPAddressStringType', 'min': 0},
            {'tag_name': 'netmask', 'class': 'oval_defs_5.EntityStateIPAddressStringType', 'min': 0},
            {'tag_name': 'addr_type', 'class': 'EntityStateAddrTypeType', 'min': 0},
        ],
    }
