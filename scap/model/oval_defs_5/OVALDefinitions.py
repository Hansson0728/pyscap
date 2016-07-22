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

from scap.model.Simple import Simple
import logging

logger = logging.getLogger(__name__)
class OVALDefinitions(Simple):
    def __init__(self):
        super(OVALDefinitions, self).__init__()

        self.definitions = {}
        self.tests = {}
        self.objects = {}
        self.states = {}
        self.variables = {}

        self.ignore_sub_elements.extend([
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}generator',
            '{http://oval.mitre.org/XMLSchema/oval-common-5}generator',
            '{http://www.w3.org/2000/09/xmldsig#}Signature',
        ])

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}definitions':
            from scap.model.oval_defs_5.Definition import Definition
            for def_el in sub_el:
                d = Definition()
                d.from_xml(self, def_el)
                self.definitions[def_el.attrib['id']] = d
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}tests':
            from scap.model.oval_defs_5.Test import Test
            for test_el in sub_el:
                t = Test()
                t.from_xml(self, test_el)
                self.tests[test_el.attrib['id']] = t
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}objects':
            from scap.model.oval_defs_5.Object import Object
            for obj_el in sub_el:
                o = Object()
                o.from_xml(self, obj_el)
                self.objects[obj_el.attrib['id']] = o
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}states':
            from scap.model.oval_defs_5.State import State
            for state_el in sub_el:
                s = State()
                s.from_xml(self, state_el)
                self.states[state_el.attrib['id']] = s
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}variables':
            from scap.model.oval_defs_5.Variable import Variable
            for var_el in sub_el:
                v = Variable()
                v.from_xml(self, var_el)
                self.variables[var_el.attrib['id']] = v
        else:
            return super(OVALDefinitions, self).parse_sub_el(sub_el)
        return True
