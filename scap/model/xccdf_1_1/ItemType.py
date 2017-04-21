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

import logging

from scap.model.xccdf_1_1.Extendable import Extendable

logger = logging.getLogger(__name__)
class ItemType(Extendable):
    MODEL_MAP = {
        # abstract
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.1}status': {'class': 'StatusType', 'append': 'statuses', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}version': {'class': 'VersionType', 'min': 0, 'max': 1},
            '{http://checklists.nist.gov/xccdf/1.1}title': {'append': 'titles', 'class': 'TextWithSubType', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}description': {'append': 'descriptions', 'min': 0, 'max': None, 'class': 'HTMLTextWithSubType'},
            '{http://checklists.nist.gov/xccdf/1.1}warning': {'class': 'WarningType', 'min': 0, 'max': None, 'type': 'String', 'append': 'warnings'},
            '{http://checklists.nist.gov/xccdf/1.1}question': {'append': 'questions', 'class': 'TextType', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}reference': {'append': 'references', 'min': 0, 'max': None, 'class': 'ReferenceType'},
        },
        'element_order': [],
        'attributes': {
            'id': {'type': 'NCName', 'required': True},
            'abstract': {'type': 'Boolean', 'default': False},
            'cluster-id': {'type': 'NCName'},
            'extends': {'type': 'NCName'},
            'hidden': {'type': 'Boolean', 'default': False},
            'prohibitChanges': {'type': 'Boolean', 'default': False},
            'Id': {'type': 'ID'},
        },
    }

    def __str__(self):
        return self.__class__.__name__ + ' # ' + self.id

    def get_extended(self, benchmark):
        try:
            extended = benchmark.item[self.extends]
        except AttributeError:
            # If any Item’s extends property identifier does not match the
            # identifier of a visible Item of the same type, then Loading fails.
            raise ValueError('Item ' + self.id + ' unable to extend unknown item id: ' + self.extends)

        if self.hidden:
            raise ValueError('Item ' + self.id + ' unable to extend hidden item id: ' + self.extends)

        return extended

    def process(self, host, benchmark, profile):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
