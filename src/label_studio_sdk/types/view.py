# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .filter_group import FilterGroup
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class View(UniversalBaseModel):
    id: typing.Optional[int] = None
    filter_group: typing.Optional[FilterGroup] = None
    data: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Custom view data
    """

    ordering: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Ordering parameters
    """

    selected_items: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Selected items
    """

    user: typing.Optional[int] = pydantic.Field(default=None)
    """
    User who made this view
    """

    project: int = pydantic.Field()
    """
    Project ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
