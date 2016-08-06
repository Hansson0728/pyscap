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
class Catalog(Model):
    ATTRIBUTE_MAP = {
        'id': {'ignore': True, 'type': 'ID'},
        'prefer': {'ignore': True, 'enum': ['system', 'public']},
        '*': {'ignore': True}
    }
    TAG_MAP = {
        '{urn:oasis:names:tc:entity:xmlns:xml:catalog}uri': {'map': 'entries', 'key': 'name', 'value': 'uri'},
        '*': {'ignore': True},
    }
    # def __init__(self):
    #     super(Catalog, self).__init__()
    #
    #     self.entries = {}
    #
    # def parse_element(self, sub_el):
    #     if sub_el.tag == '{urn:oasis:names:tc:entity:xmlns:xml:catalog}uri':
    #         self.entries[sub_el.attrib['name']] = sub_el.attrib['uri']
    #     else:
    #         return super(SubClass, self).parse_element(sub_el)
    #     return True
    #
    def to_dict(self):
        logger.debug('Catalog entries: ' + str(self.entries))
        return self.entries