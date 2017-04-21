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

from scap.model.oval_defs_5.VariableType import VariableType
import logging

logger = logging.getLogger(__name__)
class ExternalVariableElement(VariableType):
    MODEL_MAP = {
        'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5',
        'tag_name': 'external_variable',
        'elements': {
            # TODO: minOccurs="0" maxOccurs="unbounded"
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}possible_value': {'append': 'possible_values', 'class': 'PossibleValueType', 'min': 0, 'max': None},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}possible_restriction': {'append': 'possible_restrictions', 'class': 'PossibleRestrictionType', 'min': 0, 'max': None},
        },
        'element_order': [],
    }
