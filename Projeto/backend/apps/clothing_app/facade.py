# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from clothing_app.commands import ListClothingCommand, SaveClothingCommand, UpdateClothingCommand, \
    ClothingPublicForm, ClothingDetailForm, ClothingShortForm


def save_clothing_cmd(**clothing_properties):
    """
    Command to save Clothing entity
    :param clothing_properties: a dict of properties to save on model
    :return: a Command that save Clothing, validating and localizing properties received as strings
    """
    return SaveClothingCommand(**clothing_properties)


def update_clothing_cmd(clothing_id, **clothing_properties):
    """
    Command to update Clothing entity with id equals 'clothing_id'
    :param clothing_properties: a dict of properties to update model
    :return: a Command that update Clothing, validating and localizing properties received as strings
    """
    return UpdateClothingCommand(clothing_id, **clothing_properties)


def list_clothings_cmd():
    """
    Command to list Clothing entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListClothingCommand()


def clothing_detail_form(**kwargs):
    """
    Function to get Clothing's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ClothingDetailForm(**kwargs)


def clothing_short_form(**kwargs):
    """
    Function to get Clothing's short form. just a subset of clothing's properties
    :param kwargs: form properties
    :return: Form
    """
    return ClothingShortForm(**kwargs)

def clothing_public_form(**kwargs):
    """
    Function to get Clothing'spublic form. just a subset of clothing's properties
    :param kwargs: form properties
    :return: Form
    """
    return ClothingPublicForm(**kwargs)


def get_clothing_cmd(clothing_id):
    """
    Find clothing by her id
    :param clothing_id: the clothing id
    :return: Command
    """
    return NodeSearch(clothing_id)


def delete_clothing_cmd(clothing_id):
    """
    Construct a command to delete a Clothing
    :param clothing_id: clothing's id
    :return: Command
    """
    return DeleteNode(clothing_id)

