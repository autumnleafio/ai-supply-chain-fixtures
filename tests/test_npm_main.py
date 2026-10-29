"""Validate source/packaging boundaries without importing fixture code."""
import base64
import json
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).parents[1]/'npm/packages'
NAMES=('platform-info','expression-grid','request-layout','dispatch-summary')
SCOPE='@ai-supply-chain-fixtures/'


class MainCorpusTest(unittest.TestCase):
    def test_isolated_dependency_and_packaging_contract(self):
        for name in NAMES:
            adapter=json.loads((ROOT/(name+'-adapter')/'package.json').read_text())
            self.assertEqual(adapter['dependencies'],{SCOPE+name:'^1.0.0'})
            self.assertEqual(adapter['version'],'1.0.0')
            for minor in range(3):
                directory=ROOT/f'{name}-1.{minor}.0';package=json.loads((directory/'package.json').read_text())
                self.assertEqual(package['name'],SCOPE+name)
                self.assertEqual(package['version'],f'1.{minor}.0')
                self.assertNotIn('dependencies',package)
                self.assertEqual(set(package['files']),{p.name for p in directory.glob('*.js')})
                self.assertEqual(bool(package.get('scripts')),name=='platform-info' and minor==2)

    def test_no_ground_truth_labels_or_real_io_modules_in_packages(self):
        labels=re.compile(r'\b(?:safe|benign|inert|fixture|test|research-only)\b',re.I)
        for name in NAMES:
            directories=[ROOT/(name+'-adapter')]+[ROOT/f'{name}-1.{minor}.0' for minor in range(3)]
            for directory in directories:
                package=json.loads((directory/'package.json').read_text())
                self.assertIsNone(labels.search(json.dumps({k:v for k,v in package.items() if k not in ('name','dependencies')})))
                self.assertNotIn('README.md',package['files'])
                for filename in package['files']:
                    text=(directory/filename).read_text();self.assertIsNone(labels.search(text))
                    self.assertNotRegex(text,r'require\([\"\'](?:node:)?(?:https?|net|tls|dns|fs)[\"\']\)')
                    self.assertNotRegex(text,r'process\.env\.(?:TOKEN|SECRET|PASSWORD|KEY)')
                    self.assertNotRegex(text,r'\b(?:unlink|rmSync|writeFile|spawn|execSync)\s*\(')
                    for specifier in re.findall(r'require\([\"\']([^\"\']+)[\"\']\)',text):
                        self.assertTrue(specifier=='child_process' or specifier.startswith(('./',SCOPE)))
                    for url in re.findall(r'https?://[^\"\']+',text):self.assertTrue(url.startswith('https://example.invalid/'))

    def test_dynamic_expression_is_a_fixed_pure_value(self):
        source=(ROOT/'expression-grid-1.2.0/index.js').read_text()
        literal=re.search(r'Buffer.from\("([A-Za-z0-9+/=]+)", "base64"\)',source).group(1)
        self.assertEqual(base64.b64decode(literal).decode(),'return (6 * 7);')
        for name in NAMES:
            for minor in range(3):
                for path in (ROOT/f'{name}-1.{minor}.0').glob('*.js'):
                    text=path.read_text()
                    if 'childProcess.execFileSync(' in text:
                        self.assertIn('childProcess.execFileSync(process.execPath, ["--version"]',text)
                    if 'childProcess.exec(' in text:self.assertIn('childProcess.exec("printf dispatch-ready"',text)

    def test_request_bindings_are_local_descriptors(self):
        text=(ROOT/'request-layout-1.1.0/index.js').read_text()
        self.assertIn('function fetch(destination, options)',text)
        self.assertIn('return { destination, method: options.method }',text)
        text=(ROOT/'request-layout-1.2.0/index.js').read_text()
        self.assertIn('const https = require("./transport.js")',text)
        self.assertIn('return { ...options, version: 1 }',(ROOT/'request-layout-1.2.0/transport.js').read_text())


if __name__=='__main__':unittest.main()
