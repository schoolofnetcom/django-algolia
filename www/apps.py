from __future__ import unicode_literals
from django.contrib import algoliasearch
from django.contrib.algoliasearch import AlgoliaIndex
from django.apps import AppConfig


class WwwConfig(AppConfig):
    name = 'www'

    def ready(self):
        Post = self.get_model('Post')
        algoliasearch.register(Post, PostIndex)

class PostIndex(AlgoliaIndex):
    fields = ('id', 'title', 'content', 'createt_at')
    settings = {'attributesToIndex': ['title', 'content']}
    index_name = 'blog_posts'
    tags = 'category'