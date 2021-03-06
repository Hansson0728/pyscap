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

from scap.model.oval_defs_5.ObjectType import ObjectType
import logging

logger = logging.getLogger(__name__)

class CmdletObjectElement(ObjectType):
    MODEL_MAP = {
        'tag_name': 'cmdlet_object',
        'elements': [
            {'xmlns': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'set', 'class': 'oval_defs_5.SetElement', 'min': 0},
            {'tag_name': 'module_name', 'class': 'oval_defs_5.EntityObjectStringType', 'nillable': True, 'min': 1, 'max': 1},
            {'tag_name': 'module_id', 'class': 'EntityObjectGUIDType', 'nillable': True, 'min': 1, 'max': 1},
            {'tag_name': 'module_version', 'class': 'EntityObjectVersionType', 'nillable': True, 'min': 1, 'max': 1},
            {'tag_name': 'verb', 'class': 'EntityObjectCmdletVerbType', 'nillable': True, 'min': 1, 'max': 1},
            {'tag_name': 'noun', 'class': 'oval_defs_5.EntityObjectStringType', 'nillable': True, 'min': 1, 'max': 1},
            {'tag_name': 'parameters', 'class': 'oval_defs_5.EntityObjectRecordType', 'nillable': True},
            {'tag_name': 'select', 'class': 'oval_defs_5.EntityObjectRecordType', 'nillable': True},
            {'xmlns': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'filter', 'class': 'oval_defs_5.FilterElement', 'min': 0, 'max': None},
        ],
    }
