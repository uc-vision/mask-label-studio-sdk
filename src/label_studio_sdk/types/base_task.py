# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .base_task_updated_by import BaseTaskUpdatedBy
from .base_task_file_upload import BaseTaskFileUpload
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BaseTask(UniversalBaseModel):
    id: typing.Optional[int] = None
    data: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    User imported or uploaded data for a task. Data is formatted according to the project label config. You can find examples of data for your project on the Import page in the Label Studio Data Manager UI.
    """

    meta: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Meta is user imported (uploaded) data and can be useful as input for an ML Backend for embeddings, advanced vectors, and other info. It is passed to ML during training/predicting steps.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Time a task was created
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Last time a task was updated
    """

    is_labeled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the number of annotations for this task is greater than or equal to the number of maximum_completions for the project
    """

    overlap: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of distinct annotators that processed the current task
    """

    inner_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Internal task ID in the project, starts with 1
    """

    total_annotations: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of total annotations for the current task except cancelled annotations
    """

    cancelled_annotations: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of total cancelled annotations for the current task
    """

    total_predictions: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of total predictions for the current task
    """

    comment_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of comments in the task including all annotations
    """

    unresolved_comment_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of unresolved comments in the task including all annotations
    """

    last_comment_updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the last comment was updated
    """

    project: typing.Optional[int] = pydantic.Field(default=None)
    """
    Project ID for this task
    """

    updated_by: typing.Optional[BaseTaskUpdatedBy] = pydantic.Field(default=None)
    """
    Last annotator or reviewer who updated this task
    """

    file_upload: typing.Optional[BaseTaskFileUpload] = pydantic.Field(default=None)
    """
    Uploaded file used as data source for this task
    """

    comment_authors: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Users who wrote comments
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
