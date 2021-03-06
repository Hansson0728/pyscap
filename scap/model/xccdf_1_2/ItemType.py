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
import logging

logger = logging.getLogger(__name__)
class ItemType(Model):
    MODEL_MAP = {
        # abstract
        'attributes': {
            'abstract': {'type': 'Boolean', 'default': False},
            'cluster-id': {'type': 'NCName'},
            'extends': {'type': 'NCName'},
            'hidden': {'type': 'Boolean', 'default': False},
            'prohibitChanges': {'type': 'Boolean', 'default': False},
            'Id': {'type': 'ID'},
        },
        'elements': [
            {'tag_name': 'status', 'class': 'StatusType', 'append': 'statuses', 'min': 0, 'max': None},
            {'tag_name': 'dc-status', 'class': 'DCStatusType', 'append': 'dc_statuses', 'min': 0, 'max': None},
            {'tag_name': 'version', 'class': 'VersionType', 'min': 0, 'max': 1},
            {'tag_name': 'title', 'append': 'titles', 'class': 'TextWithSubType', 'min': 0, 'max': None},
            {'tag_name': 'description', 'append': 'descriptions', 'min': 0, 'max': None, 'class': 'HTMLTextWithSubType'},
            {'tag_name': 'warning', 'class': 'WarningType', 'min': 0, 'max': None, 'type': 'String', 'append': 'warnings'},
            {'tag_name': 'question', 'append': 'questions', 'class': 'TextType', 'min': 0, 'max': None},
            {'tag_name': 'reference', 'append': 'references', 'min': 0, 'max': None, 'class': 'ReferenceType'},
            {'tag_name': 'metadata', 'append': 'metadata', 'min': 0, 'max': None, 'class': 'MetadataType'},
        ],
    }
