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
class UacStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'uac_state',
        'elements': [
            {'tag_name': 'admin_approval_mode', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'elevation_prompt_admin', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'elevation_prompt_standard', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'detect_installations', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'elevate_signed_executables', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'elevate_uiaccess', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'run_admins_aam', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'secure_desktop', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'virtualize_write_failures', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
        ],
    }
