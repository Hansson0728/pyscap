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

from scap.model.xccdf_1_2.Item import Item
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class GroupRuleCommon(Item):
    def __init__(self):
        super(GroupRuleCommon, self).__init__()

        self.ignore_attributes.extend(['selected', 'weight'])
        self.ignore_sub_elements.extend([
            '{http://checklists.nist.gov/xccdf/1.2}rationale',
            '{http://checklists.nist.gov/xccdf/1.2}platform',
            '{http://checklists.nist.gov/xccdf/1.2}requires',
            '{http://checklists.nist.gov/xccdf/1.2}conflicts',
        ])
