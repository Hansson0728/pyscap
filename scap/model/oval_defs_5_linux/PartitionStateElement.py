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
class PartitionStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'partition_state',
        'elements': [
            {'tag_name': 'mount_point', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'device', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'uuid', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'fs_type', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'mount_options', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0, 'max': 1},
            {'tag_name': 'total_space', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'space_used', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
            {'tag_name': 'space_left', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0, 'max': 1},
        ],
    }
