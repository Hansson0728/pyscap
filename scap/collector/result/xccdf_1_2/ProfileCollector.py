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

from scap.collector.ResultCollector import ResultCollector
from scap.Engine import Engine
import logging

logger = logging.getLogger(__name__)
class ProfileCollector(ResultCollector):
    def collect_results(self):
        # expand values
        values = {}
        for value_id, value in self.content.parent.values.items():
            values[value_id] = {}
            if value_id in self.content.value_selections:
                values[value_id]['value'] = value.selectors[self.content.value_selections[value_id]]
            else:
                if None in value.selectors:
                    values[value_id]['value'] = value.selectors[None]
                elif len(value.selectors.values()) > 0:
                    values[value_id]['value'] = value.selectors.values()[0]
            if 'value' not in values[value_id] or values[value_id]['value'] is None:
                logger.critical('Valid value not selected for ' + value_id + ': ' + str(value.selectors))
                import sys
                sys.exit()
            values[value_id]['operator'] = value.operator
            values[value_id]['type'] = value.type

            logger.debug('Using value ' + values[value_id]['operator'] + ' ' + values[value_id]['value'] + ' for ' + values[value_id]['type'] + ' value ' + value_id)

        for rule_id in self.content.selected_rules:
            from scap.collector.result.xccdf_1_2.RuleCollector import RuleCollector
            rule = self.content.parent.rules[rule_id]
            self.host.add_result_collector(RuleCollector(self.host, rule, values, self.content.rule_check_selections[rule_id]))