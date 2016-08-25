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
class SeLinuxSecurityContextObjectElement(ObjectType):
    MODEL_MAP = {
        'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux',
        'tag_name': 'selinuxsecuritycontext_object',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}set': {'class': 'SetElement'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}behaviors': {'class': 'FileBehaviors', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}filepath': {'class': 'oval_defs_5.EntityObjectStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}path': {'class': 'oval_defs_5.EntityObjectStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}filename': {'class': 'oval_defs_5.EntityObjectStringType', 'nillable': True},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}pid': {'class': 'oval_defs_5.EntityObjectIntType', 'nillable': True},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}filter': {'class': 'FilterElement', 'min': 0, 'max': None},
        }
    }