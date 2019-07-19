# coding: utf-8

from __future__ import absolute_import
from typing import List  # noqa: F401
from application.models.base_model_ import Model
from application.util import util


class Requirement(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, title: str=None, description: str=None, comments: List[str]=None):  # noqa: E501
        """Requirement - a model defined in Swagger

        :param id: The id of this Requirement.  # noqa: E501
        :type id: int
        :param title: The title of this Requirement.  # noqa: E501
        :type title: str
        :param description: The description of this Requirement.  # noqa: E501
        :type description: str
        :param predictions: The predicted similar requirements of this Requirement.  # noqa: E501
        :type predictions: List[int]
        :param comments: Comments added to this Requirement.  # noqa: E501
        :type comments: List[str]
        """
        self.swagger_types = {
            'id': int,
            'title': str,
            'description': str,
            'comments': list,
            'predictions': list
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'description': 'description',
            'comments': 'comments',
            'predictions': 'predictions'
        }

        self._id = id
        self._title = title
        self._description = description
        self._comments = comments
        self._predictions = []

    @classmethod
    def from_dict(cls, dikt) -> 'Requirement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Requirement of this Requirement.  # noqa: E501
        :rtype: Requirement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Requirement.


        :return: The id of this Requirement.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Requirement.


        :param id: The id of this Requirement.
        :type id: int
        """

        self._id = id

    @property
    def title(self) -> str:
        """Gets the title of this Requirement.


        :return: The title of this Requirement.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Requirement.


        :param title: The title of this Requirement.
        :type title: str
        """

        self._title = title

    @property
    def description(self) -> str:
        """Gets the description of this Requirement.


        :return: The description of this Requirement.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Requirement.


        :param description: The description of this Requirement.
        :type description: str
        """

        self._description = description

    @property
    def comments(self) -> List[str]:
        """Gets the predictions of this Requirement.


        :return: The predictions of this Requirement.
        :rtype: List[str]
        """
        return self._comments

    @comments.setter
    def comments(self, comments: []):
        """Sets the comments attribute of this Requirement.


        :param comments: The comments list attribute of this Requirement.
        :type comments: List[str]
        """

        self._comments = comments

    @property
    def predictions(self) -> []:
        """Gets the predictions of this Requirement.


        :return: The predictions of this Requirement.
        :rtype: List[Requirement]
        """
        return self._predictions

    @predictions.setter
    def predictions(self, predictions: list):
        """Sets the predict attribute of this Requirement.


        :param predictions: The predictions similar requirements list attribute of this Requirement.
        :type predictions: List[int]
        """

        self._predictions = predictions