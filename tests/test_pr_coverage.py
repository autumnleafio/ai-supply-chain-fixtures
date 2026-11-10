"""Check bounded static-review specimens without importing package modules."""
import json
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).parents[1]/'npm/packages'
SCOPE='@ai-supply-chain-fixtures/'


class AddedFamiliesTest(unittest.TestCase):
    def test_package_boundaries_and_no_answer_labels(self):
        labels=re.compile(r'\b(?:safe|benign|inert|fixture|test|research-only)\b',re.I)
        for name in ('delivery-status','session-report'):
            for suffix in ('adapter','1.0.0','1.1.0','1.2.0'):
                directory=ROOT/(name+'-'+suffix)
                package=json.loads((directory/'package.json').read_text())
                self.assertEqual(set(package['files']),{p.name for p in directory.glob('*.js')})
                self.assertNotIn('README.md',package['files'])
                self.assertIsNone(labels.search(json.dumps({k:v for k,v in package.items() if k not in ('name','dependencies')})))
                if suffix=='adapter':self.assertEqual(package['dependencies'],{SCOPE+name:'^1.0.0'})
                else:self.assertNotIn('dependencies',package)
                self.assertEqual(package.get('scripts',{}),{'postinstall':'node install.js'} if (name,suffix)==('delivery-status','1.2.0') else {})
                for filename in package['files']:
                    source=(directory/filename).read_text();self.assertIsNone(labels.search(source))
                    self.assertNotRegex(source,r'process\.env|readFile|writeFile|child_process|node:fs|node:net|node:tls|node:dns|node:https|https://')
                    imports=re.findall(r'require\("([^"\n]+)"\)',source)
                    for module in imports:
                        self.assertTrue(module.startswith(('./',SCOPE)) or (name=='delivery-status' and filename=='send.js' and module=='node:http'))

    def test_real_client_is_literal_loopback_with_fixed_body(self):
        sources=[(ROOT/f'delivery-status-1.{minor}.0/send.js').read_text() for minor in range(3)]
        self.assertEqual(len(set(sources)),1)
        text=sources[0]
        self.assertIn('const http = require("node:http");',text)
        self.assertEqual(text.count('http.request('),1)
        self.assertEqual(re.findall(r'hostname: "([^"\n]+)"',text),['127.0.0.1'])
        self.assertIn('port: 48153',text)
        self.assertIn('path: "/status"',text)
        self.assertIn('method: "POST"',text)
        self.assertIn('request.setTimeout(250, () => request.destroy());',text)
        self.assertEqual(text.count('request.end('),1)
        self.assertIn("request.end(" + repr('{"component":"runtime","state":"ready"}') + ");",text)
        self.assertNotRegex(text,r'\b(?:fetch|connect|lookup|eval|Function)\s*\(|\.write\s*\(|process\.|Buffer\.|\.agent|redirect')

    def test_added_hook_preserves_existing_helper(self):
        before=ROOT/'delivery-status-1.1.0';after=ROOT/'delivery-status-1.2.0'
        self.assertEqual((before/'index.js').read_bytes(),(after/'index.js').read_bytes())
        self.assertEqual((before/'send.js').read_bytes(),(after/'send.js').read_bytes())
        self.assertFalse((before/'install.js').exists())
        self.assertEqual((after/'install.js').read_text(),'const delivery = require("./send.js");\ndelivery.sendStatus();\n')
        for minor in range(3):
            self.assertNotIn('sendStatus',(ROOT/f'delivery-status-1.{minor}.0/index.js').read_text())

    def test_only_authorization_redaction_changes_in_data_transition(self):
        before=(ROOT/'session-report-1.1.0/index.js').read_text()
        after=(ROOT/'session-report-1.2.0/index.js').read_text()
        self.assertEqual(before.replace('authorization: "[redacted]"','authorization: session.authorization'),after)
        self.assertIn('console.log(JSON.stringify(event));',after)
        values=[(ROOT/f'session-report-1.{minor}.0/session.js').read_text() for minor in range(3)]
        self.assertEqual(len(set(values)),1)
        self.assertIn('authorization: "demo-access-value"',values[0])
        self.assertNotIn('process.',values[0])
        for minor in (0,1):self.assertIn('authorization: "[redacted]"',(ROOT/f'session-report-1.{minor}.0/index.js').read_text())
