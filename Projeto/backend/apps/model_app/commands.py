# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from model_app.model import Model

class ModelPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Model
    _include = [Model.price, 
                Model.data, 
                Model.title]


class ModelForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Model
    _include = [Model.price, 
                Model.data, 
                Model.title]


class ModelDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Model
    _include = [Model.price, 
                Model.creation, 
                Model.data, 
                Model.title]


class ModelShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Model
    _include = [Model.price, 
                Model.creation, 
                Model.data, 
                Model.title]


class SaveModelCommand(SaveCommand):
    _model_form_class = ModelForm


class UpdateModelCommand(UpdateNode):
    _model_form_class = ModelForm


class ListModelCommand(ModelSearchCommand):
    def __init__(self):
        super(ListModelCommand, self).__init__(Model.query_by_creation())

