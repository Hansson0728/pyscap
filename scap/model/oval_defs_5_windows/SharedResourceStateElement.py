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
class SharedResourceStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'sharedresource_state',
        'elements': [
            {'tag_name': 'netname', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'shared_type', 'class': 'EntityStateSharedResourceTypeType', 'min': 0},
            {'tag_name': 'max_uses', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0},
            {'tag_name': 'current_uses', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0},
            {'tag_name': 'local_path', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'access_read_permission', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'access_write_permission', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'access_create_permission', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'access_exec_permission', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'access_delete_permission', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'access_atrib_permission', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'access_perm_permission', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'access_all_permission', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
        ],
    }
