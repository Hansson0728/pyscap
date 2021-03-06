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

import getpass
import logging

from scap.model.xs.String import String

logger = logging.getLogger(__name__)
class IdentityType(String):
    MODEL_MAP = {
        'attributes': {
            'authenticated': {'type': 'Boolean', 'required': True},
            'privileged': {'type': 'Boolean', 'required': True},
        }
    }

    def __init__(self, tag_name=None):
        super(IdentityType, self).__init__(tag_name=tag_name)

        self.value = getpass.getuser()

        # TODO
        self.authenticated = False
        self.privileged = False
