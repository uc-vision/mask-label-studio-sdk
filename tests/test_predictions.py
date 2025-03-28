# This file was auto-generated by Fern from our API Definition.

from label_studio_sdk import LabelStudio
from label_studio_sdk import AsyncLabelStudio
import typing
from .utilities import validate_response


async def test_list_(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = [
        {
            "id": 1,
            "result": [
                {
                    "original_width": 1920,
                    "original_height": 1080,
                    "image_rotation": 0,
                    "from_name": "bboxes",
                    "to_name": "image",
                    "type": "rectanglelabels",
                    "value": {
                        "x": 20,
                        "y": 30,
                        "width": 50,
                        "height": 60,
                        "rotation": 0,
                        "values": {"rectanglelabels": ["Person"]},
                    },
                }
            ],
            "model_version": "yolo-v8",
            "created_ago": "created_ago",
            "score": 0.95,
            "cluster": 1,
            "neighbors": {"key": "value"},
            "mislabeling": 1.1,
            "created_at": "2024-01-15T09:30:00Z",
            "updated_at": "2024-01-15T09:30:00Z",
            "model": 1,
            "model_run": 1,
            "task": 1,
            "project": 1,
        }
    ]
    expected_types: typing.Tuple[typing.Any, typing.Any] = (
        "list",
        {
            0: {
                "id": "integer",
                "result": (
                    "list",
                    {
                        0: (
                            "dict",
                            {
                                0: (None, None),
                                1: (None, None),
                                2: (None, None),
                                3: (None, None),
                                4: (None, None),
                                5: (None, None),
                                6: (None, None),
                            },
                        )
                    },
                ),
                "model_version": None,
                "created_ago": None,
                "score": None,
                "cluster": "integer",
                "neighbors": ("dict", {0: (None, None)}),
                "mislabeling": None,
                "created_at": "datetime",
                "updated_at": "datetime",
                "model": "integer",
                "model_run": "integer",
                "task": "integer",
                "project": "integer",
            }
        },
    )
    response = client.predictions.list()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.predictions.list()
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "result": [
            {
                "original_width": 1920,
                "original_height": 1080,
                "image_rotation": 0,
                "from_name": "bboxes",
                "to_name": "image",
                "type": "rectanglelabels",
                "value": {
                    "x": 20,
                    "y": 30,
                    "width": 50,
                    "height": 60,
                    "rotation": 0,
                    "values": {"rectanglelabels": ["Person"]},
                },
            }
        ],
        "model_version": "yolo-v8",
        "created_ago": "created_ago",
        "score": 0.95,
        "cluster": 1,
        "neighbors": {"key": "value"},
        "mislabeling": 1.1,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "model": 1,
        "model_run": 1,
        "task": 1,
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "result": (
            "list",
            {
                0: (
                    "dict",
                    {
                        0: (None, None),
                        1: (None, None),
                        2: (None, None),
                        3: (None, None),
                        4: (None, None),
                        5: (None, None),
                        6: (None, None),
                    },
                )
            },
        ),
        "model_version": None,
        "created_ago": None,
        "score": None,
        "cluster": "integer",
        "neighbors": ("dict", {0: (None, None)}),
        "mislabeling": None,
        "created_at": "datetime",
        "updated_at": "datetime",
        "model": "integer",
        "model_run": "integer",
        "task": "integer",
        "project": "integer",
    }
    response = client.predictions.create(
        result=[
            {
                "original_width": 1920,
                "original_height": 1080,
                "image_rotation": 0,
                "from_name": "bboxes",
                "to_name": "image",
                "type": "rectanglelabels",
                "value": {
                    "x": 20,
                    "y": 30,
                    "width": 50,
                    "height": 60,
                    "rotation": 0,
                    "values": {"rectanglelabels": ["Person"]},
                },
            }
        ],
        score=0.95,
        model_version="yolo-v8",
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.predictions.create(
        result=[
            {
                "original_width": 1920,
                "original_height": 1080,
                "image_rotation": 0,
                "from_name": "bboxes",
                "to_name": "image",
                "type": "rectanglelabels",
                "value": {
                    "x": 20,
                    "y": 30,
                    "width": 50,
                    "height": 60,
                    "rotation": 0,
                    "values": {"rectanglelabels": ["Person"]},
                },
            }
        ],
        score=0.95,
        model_version="yolo-v8",
    )
    validate_response(async_response, expected_response, expected_types)


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "result": [
            {
                "original_width": 1920,
                "original_height": 1080,
                "image_rotation": 0,
                "from_name": "bboxes",
                "to_name": "image",
                "type": "rectanglelabels",
                "value": {
                    "x": 20,
                    "y": 30,
                    "width": 50,
                    "height": 60,
                    "rotation": 0,
                    "values": {"rectanglelabels": ["Person"]},
                },
            }
        ],
        "model_version": "yolo-v8",
        "created_ago": "created_ago",
        "score": 0.95,
        "cluster": 1,
        "neighbors": {"key": "value"},
        "mislabeling": 1.1,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "model": 1,
        "model_run": 1,
        "task": 1,
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "result": (
            "list",
            {
                0: (
                    "dict",
                    {
                        0: (None, None),
                        1: (None, None),
                        2: (None, None),
                        3: (None, None),
                        4: (None, None),
                        5: (None, None),
                        6: (None, None),
                    },
                )
            },
        ),
        "model_version": None,
        "created_ago": None,
        "score": None,
        "cluster": "integer",
        "neighbors": ("dict", {0: (None, None)}),
        "mislabeling": None,
        "created_at": "datetime",
        "updated_at": "datetime",
        "model": "integer",
        "model_run": "integer",
        "task": "integer",
        "project": "integer",
    }
    response = client.predictions.get(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.predictions.get(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert (
        client.predictions.delete(id=1)  # type: ignore[func-returns-value]
        is None
    )

    assert (
        await async_client.predictions.delete(id=1)  # type: ignore[func-returns-value]
        is None
    )


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "result": [
            {
                "original_width": 1920,
                "original_height": 1080,
                "image_rotation": 0,
                "from_name": "bboxes",
                "to_name": "image",
                "type": "rectanglelabels",
                "value": {
                    "x": 20,
                    "y": 30,
                    "width": 50,
                    "height": 60,
                    "rotation": 0,
                    "values": {"rectanglelabels": ["Person"]},
                },
            }
        ],
        "model_version": "yolo-v8",
        "created_ago": "created_ago",
        "score": 0.95,
        "cluster": 1,
        "neighbors": {"key": "value"},
        "mislabeling": 1.1,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "model": 1,
        "model_run": 1,
        "task": 1,
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "result": (
            "list",
            {
                0: (
                    "dict",
                    {
                        0: (None, None),
                        1: (None, None),
                        2: (None, None),
                        3: (None, None),
                        4: (None, None),
                        5: (None, None),
                        6: (None, None),
                    },
                )
            },
        ),
        "model_version": None,
        "created_ago": None,
        "score": None,
        "cluster": "integer",
        "neighbors": ("dict", {0: (None, None)}),
        "mislabeling": None,
        "created_at": "datetime",
        "updated_at": "datetime",
        "model": "integer",
        "model_run": "integer",
        "task": "integer",
        "project": "integer",
    }
    response = client.predictions.update(
        id=1,
        result=[
            {
                "original_width": 1920,
                "original_height": 1080,
                "image_rotation": 0,
                "from_name": "bboxes",
                "to_name": "image",
                "type": "rectanglelabels",
                "value": {
                    "x": 20,
                    "y": 30,
                    "width": 50,
                    "height": 60,
                    "rotation": 0,
                    "values": {"rectanglelabels": ["Person"]},
                },
            }
        ],
        score=0.95,
        model_version="yolo-v8",
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.predictions.update(
        id=1,
        result=[
            {
                "original_width": 1920,
                "original_height": 1080,
                "image_rotation": 0,
                "from_name": "bboxes",
                "to_name": "image",
                "type": "rectanglelabels",
                "value": {
                    "x": 20,
                    "y": 30,
                    "width": 50,
                    "height": 60,
                    "rotation": 0,
                    "values": {"rectanglelabels": ["Person"]},
                },
            }
        ],
        score=0.95,
        model_version="yolo-v8",
    )
    validate_response(async_response, expected_response, expected_types)
