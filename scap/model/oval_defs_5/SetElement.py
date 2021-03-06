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

from scap.Model import Model
from scap.model.oval_defs_5.SetOperatorEnumeration import SET_OPERATOR_ENUMERATION
import logging

logger = logging.getLogger(__name__)
class SetElement(Model):
    MODEL_MAP = {
        'tag_name': 'set',
        'elements': [
            # TODO: either set element or object_reference (+ optional filter)
            {'tag_name': 'set', 'class': 'SetElement', 'min': 0, 'max': 2},
            {'tag_name': 'object_reference', 'append': 'object_references', 'type': 'oval_common_5.ObjectIDPattern', 'min': 0, 'max': 2},
            {'tag_name': 'filter', 'class': 'FilterElement', 'min': 0, 'max': None},
        ],
        'attributes': {
            'set_operator': {'enum': SET_OPERATOR_ENUMERATION, 'default': 'UNION'},
        }
    }
