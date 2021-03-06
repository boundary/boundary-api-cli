#!/usr/bin/env python
#
# Copyright 2015 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from unittest import TestCase
import json
from cli_test import CLITest
from cli_runner import CLIRunner
from boundary import MetricCreate
from boundary import MetricDelete
from boundary import MetricUpdate


class MetricUpdateTest(TestCase):

    def setUp(self):
        self.cli = MetricUpdate()

    def test_get_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_delete_metric(self):
        runner_create = CLIRunner(MetricCreate())
        metric_name = 'METRIC' + CLITest.random_string(6)
        display_name = 'Display Name ' + CLITest.random_string(20)
        display_name_short = 'Short Display Name' + CLITest.random_string(5)
        description = CLITest.random_string(30)
        aggregate = 'avg'
        unit = 'number'
        resolution = 60000
        disabled = False

        create = runner_create.get_output(['-n', metric_name,
                                           '-d', display_name,
                                           '-s', display_name_short,
                                           '-i', description,
                                           '-g', aggregate,
                                           '-r', str(resolution),
                                           '-u', unit,
                                           '-x', str(disabled).lower()])
        metric_create = json.loads(create)
        metric = metric_create['result']


        display_name = 'Display Name ' + CLITest.random_string(20)
        display_name_short = 'Short Display Name' + CLITest.random_string(5)
        description = CLITest.random_string(30)
        aggregate = 'max'
        unit = 'percent'
        resolution = 30000
        disabled = True

        runner_update = CLIRunner(MetricUpdate())
        update = runner_update.get_output(['-n', metric_name,
                                           '-d', display_name,
                                           '-s', display_name_short,
                                           '-i', description,
                                           '-g', aggregate,
                                           '-r', str(resolution),
                                           '-u', unit,
                                           '-x', str(disabled).lower()])

        metric_update = json.loads(update)
        metric = metric_update['result']

        self.assertEqual(metric_name, metric['name'])
        self.assertEqual(display_name, metric['displayName'])
        self.assertEqual(display_name_short, metric['displayNameShort'])
        self.assertEqual(description, metric['description'])
        self.assertFalse(metric['isDisabled'])
        self.assertEqual(unit, metric['unit'])
        self.assertEqual(aggregate, metric['defaultAggregate'].lower())
        self.assertEqual(resolution, int(metric['defaultResolutionMS']))
        self.assertEqual(description, metric['description'])


        runner_delete = CLIRunner(MetricDelete())
        delete = runner_delete.get_output(['-n', metric_name])
        result = json.loads(delete)
        self.assertTrue(result['result']['success'])
