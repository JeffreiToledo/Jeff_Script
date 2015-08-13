# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Modelo(Node):
    preco = property.SimpleCurrency(required=True)
    titulo = ndb.StringProperty(required=True)
    data = ndb.DateProperty(required=True)

