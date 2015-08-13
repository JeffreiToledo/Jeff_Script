# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Clothing(Node):
    price = property.SimpleCurrency(required=True)
    name = ndb.StringProperty(required=True)
    date = ndb.DateProperty(required=True)

