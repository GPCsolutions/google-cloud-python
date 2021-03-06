# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest


class TestEntity(unittest.TestCase):

    def _getTargetClass(self):
        from google.cloud.language.entity import Entity
        return Entity

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_constructor_defaults(self):
        name = 'Italian'
        entity_type = 'LOCATION'
        wiki_url = 'http://en.wikipedia.org/wiki/Italy'
        metadata = {'wikipedia_url': wiki_url}
        base_metadata = {'foo': 'bar'}
        metadata.update(base_metadata)
        salience = 0.19960518
        mentions = ['Italian']
        entity = self._makeOne(name, entity_type, metadata,
                               salience, mentions)
        self.assertEqual(entity.name, name)
        self.assertEqual(entity.entity_type, entity_type)
        self.assertEqual(entity.wikipedia_url, wiki_url)
        self.assertEqual(entity.metadata, base_metadata)
        self.assertEqual(entity.salience, salience)
        self.assertEqual(entity.mentions, mentions)

    def test_from_api_repr(self):
        klass = self._getTargetClass()
        name = 'Italy'
        entity_type = 'LOCATION'
        salience = 0.223
        wiki_url = 'http://en.wikipedia.org/wiki/Italy'
        mention1 = 'Italy'
        mention2 = 'To Italy'
        mention3 = 'From Italy'
        payload = {
            'name': name,
            'type': entity_type,
            'salience': salience,
            'metadata': {'wikipedia_url': wiki_url},
            'mentions': [
                {'text': {'content': mention1}},
                {'text': {'content': mention2}},
                {'text': {'content': mention3}},
            ],
        }
        entity = klass.from_api_repr(payload)
        self.assertEqual(entity.name, name)
        self.assertEqual(entity.entity_type, entity_type)
        self.assertEqual(entity.salience, salience)
        self.assertEqual(entity.wikipedia_url, wiki_url)
        self.assertEqual(entity.metadata, {})
        self.assertEqual(entity.mentions, [mention1, mention2, mention3])
