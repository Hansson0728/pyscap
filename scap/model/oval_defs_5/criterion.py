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
class criterion(Model):
    def __init__(self):
        super(criterion, self).__init__()    # {http://oval.mitre.org/XMLSchema/oval-definitions-5}criterion

        self.negate = False
        self.applicability_check = False
        self.test_ref = None

        self.ignore_attributes.extend([
            'comment',
        ])
        self.required_attributes.append('test_ref')

    def parse_attribute(self, name, value):
        if name == 'negate':
            self.negate = self.parse_boolean(value)
        elif name == 'applicability_check':
            self.applicability_check = self.parse_boolean(value)
        elif name == 'test_ref':
            self.test_ref = value
        else:
            return super(criterion, self).parse_attribute(name, value)
        return True

    def resolve(self):
        return self.resolve_reference(self.test_ref)