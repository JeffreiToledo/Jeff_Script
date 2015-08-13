# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from clothing_app.model import Clothing

class ClothingPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Clothing
    _include = [Clothing.date, 
                Clothing.price, 
                Clothing.name]


class ClothingForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Clothing
    _include = [Clothing.date, 
                Clothing.price, 
                Clothing.name]


class ClothingDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Clothing
    _include = [Clothing.date, 
                Clothing.price, 
                Clothing.creation, 
                Clothing.name]


class ClothingShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Clothing
    _include = [Clothing.date, 
                Clothing.price, 
                Clothing.creation, 
                Clothing.name]


class SaveClothingCommand(SaveCommand):
    _model_form_class = ClothingForm


class UpdateClothingCommand(UpdateNode):
    _model_form_class = ClothingForm


class ListClothingCommand(ModelSearchCommand):
    def __init__(self):
        super(ListClothingCommand, self).__init__(Clothing.query_by_creation())

