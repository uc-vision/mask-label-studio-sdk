# This file was auto-generated by Fern from our API Definition.

from label_studio_sdk import LabelStudio
from label_studio_sdk import AsyncLabelStudio
import typing
from .utilities import validate_response


async def test_list_(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = [
        {
            "id": 1,
            "text": "text",
            "project": 1,
            "task": 1,
            "annotation": 1,
            "created_by": 1,
            "created_at": "2024-01-15T09:30:00Z",
            "updated_at": "2024-01-15T09:30:00Z",
            "is_resolved": True,
            "resolved_at": "2024-01-15T09:30:00Z",
        }
    ]
    expected_types: typing.Tuple[typing.Any, typing.Any] = (
        "list",
        {
            0: {
                "id": "integer",
                "text": None,
                "project": "integer",
                "task": "integer",
                "annotation": "integer",
                "created_by": "integer",
                "created_at": "datetime",
                "updated_at": "datetime",
                "is_resolved": None,
                "resolved_at": "datetime",
            }
        },
    )
    response = client.comments.list()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.comments.list()
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "text": "text",
        "project": 1,
        "task": 1,
        "annotation": 1,
        "created_by": 1,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "is_resolved": True,
        "resolved_at": "2024-01-15T09:30:00Z",
    }
    expected_types: typing.Any = {
        "id": "integer",
        "text": None,
        "project": "integer",
        "task": "integer",
        "annotation": "integer",
        "created_by": "integer",
        "created_at": "datetime",
        "updated_at": "datetime",
        "is_resolved": None,
        "resolved_at": "datetime",
    }
    response = client.comments.create()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.comments.create()
    validate_response(async_response, expected_response, expected_types)


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "text": "text",
        "project": 1,
        "task": 1,
        "annotation": 1,
        "created_by": 1,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "is_resolved": True,
        "resolved_at": "2024-01-15T09:30:00Z",
    }
    expected_types: typing.Any = {
        "id": "integer",
        "text": None,
        "project": "integer",
        "task": "integer",
        "annotation": "integer",
        "created_by": "integer",
        "created_at": "datetime",
        "updated_at": "datetime",
        "is_resolved": None,
        "resolved_at": "datetime",
    }
    response = client.comments.get(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.comments.get(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert (
        client.comments.delete(id=1)  # type: ignore[func-returns-value]
        is None
    )

    assert (
        await async_client.comments.delete(id=1)  # type: ignore[func-returns-value]
        is None
    )


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "text": "text",
        "project": 1,
        "task": 1,
        "annotation": 1,
        "created_by": 1,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "is_resolved": True,
        "resolved_at": "2024-01-15T09:30:00Z",
    }
    expected_types: typing.Any = {
        "id": "integer",
        "text": None,
        "project": "integer",
        "task": "integer",
        "annotation": "integer",
        "created_by": "integer",
        "created_at": "datetime",
        "updated_at": "datetime",
        "is_resolved": None,
        "resolved_at": "datetime",
    }
    response = client.comments.update(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.comments.update(id=1)
    validate_response(async_response, expected_response, expected_types)
