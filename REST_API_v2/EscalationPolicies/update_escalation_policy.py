#!/usr/bin/env python
#
# Copyright (c) 2016, PagerDuty, Inc. <info@pagerduty.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of PagerDuty Inc nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL PAGERDUTY INC BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import requests
import json

# Update to match your API key
API_KEY = '3c3gRvzx7uGfMYEnWKvF'

# Update to match ID of resource you want to update
ID = 'PVHNG0S'

# Update to match your chosen parameters
TYPE = 'escalation_policy'
NAME = 'Insert resource name here'
SUMMARY = 'Insert resource description here'
REPEAT_ENABLED = True
NUM_LOOPS = 3
ESCALATION_RULES = [
    {
        'escalation_delay_in_minutes': 30,
        'targets': [
            {
                'type': 'schedule',
                'id': 'PTC959G'
            }
        ]
    }
]
SERVICES = []


def update_escalation_policy():
    url = 'https://api.pagerduty.com/escalation_policies/{id}'.format(id=ID)
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY),
        'Content-type': 'application/json'
    }
    payload = {
        'escalation_policy': {
            'name': NAME,
            'type': TYPE,
            'summary': SUMMARY,
            'repeat_enabled': REPEAT_ENABLED,
            'num_loops': NUM_LOOPS,
            'escalation_rules': ESCALATION_RULES,
            'services': SERVICES
        }
    }
    r = requests.put(url, headers=headers, data=json.dumps(payload))
    print('Status Code: {code}'.format(code=r.status_code))
    print(r.json())

if __name__ == '__main__':
    update_escalation_policy()
