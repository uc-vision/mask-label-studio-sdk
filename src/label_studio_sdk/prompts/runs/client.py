# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from .types.runs_list_request_project_subset import RunsListRequestProjectSubset
from ...core.request_options import RequestOptions
from ...types.inference_run import InferenceRun
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...types.inference_run_project_subset import InferenceRunProjectSubset
from ...types.inference_run_organization import InferenceRunOrganization
from ...types.inference_run_created_by import InferenceRunCreatedBy
from ...types.inference_run_status import InferenceRunStatus
import datetime as dt
from ...core.serialization import convert_and_respect_annotation_metadata
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        id: int,
        version_id: int,
        *,
        project: int,
        project_subset: RunsListRequestProjectSubset,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InferenceRun:
        """
        Get information (status, etadata, etc) about an existing inference run

        Parameters
        ----------
        id : int
            Prompt ID

        version_id : int
            Prompt Version ID

        project : int
            The ID of the project that this Interence Run makes predictions on

        project_subset : RunsListRequestProjectSubset
            Defines which tasks are operated on (e.g. HasGT will only operate on tasks with a ground truth annotation, but All will operate on all records)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferenceRun
            Success

        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.prompts.runs.list(
            id=1,
            version_id=1,
            project=1,
            project_subset="All",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions/{jsonable_encoder(version_id)}/inference-runs",
            method="GET",
            params={
                "project": project,
                "project_subset": project_subset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    InferenceRun,
                    parse_obj_as(
                        type_=InferenceRun,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        id: int,
        version_id: int,
        *,
        project: int,
        project_subset: InferenceRunProjectSubset,
        organization: typing.Optional[InferenceRunOrganization] = OMIT,
        model_version: typing.Optional[int] = OMIT,
        created_by: typing.Optional[InferenceRunCreatedBy] = OMIT,
        status: typing.Optional[InferenceRunStatus] = OMIT,
        job_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        triggered_at: typing.Optional[dt.datetime] = OMIT,
        predictions_updated_at: typing.Optional[dt.datetime] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InferenceRun:
        """
        Run a prompt inference.

        Parameters
        ----------
        id : int
            Prompt ID

        version_id : int
            Prompt Version ID

        project : int

        project_subset : InferenceRunProjectSubset

        organization : typing.Optional[InferenceRunOrganization]

        model_version : typing.Optional[int]

        created_by : typing.Optional[InferenceRunCreatedBy]

        status : typing.Optional[InferenceRunStatus]

        job_id : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        triggered_at : typing.Optional[dt.datetime]

        predictions_updated_at : typing.Optional[dt.datetime]

        completed_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferenceRun


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.prompts.runs.create(
            id=1,
            version_id=1,
            project=1,
            project_subset="All",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions/{jsonable_encoder(version_id)}/inference-runs",
            method="POST",
            json={
                "organization": convert_and_respect_annotation_metadata(
                    object_=organization, annotation=InferenceRunOrganization, direction="write"
                ),
                "project": project,
                "model_version": model_version,
                "created_by": convert_and_respect_annotation_metadata(
                    object_=created_by, annotation=InferenceRunCreatedBy, direction="write"
                ),
                "project_subset": project_subset,
                "status": status,
                "job_id": job_id,
                "created_at": created_at,
                "triggered_at": triggered_at,
                "predictions_updated_at": predictions_updated_at,
                "completed_at": completed_at,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    InferenceRun,
                    parse_obj_as(
                        type_=InferenceRun,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        id: int,
        version_id: int,
        *,
        project: int,
        project_subset: RunsListRequestProjectSubset,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InferenceRun:
        """
        Get information (status, etadata, etc) about an existing inference run

        Parameters
        ----------
        id : int
            Prompt ID

        version_id : int
            Prompt Version ID

        project : int
            The ID of the project that this Interence Run makes predictions on

        project_subset : RunsListRequestProjectSubset
            Defines which tasks are operated on (e.g. HasGT will only operate on tasks with a ground truth annotation, but All will operate on all records)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferenceRun
            Success

        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.prompts.runs.list(
                id=1,
                version_id=1,
                project=1,
                project_subset="All",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions/{jsonable_encoder(version_id)}/inference-runs",
            method="GET",
            params={
                "project": project,
                "project_subset": project_subset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    InferenceRun,
                    parse_obj_as(
                        type_=InferenceRun,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        id: int,
        version_id: int,
        *,
        project: int,
        project_subset: InferenceRunProjectSubset,
        organization: typing.Optional[InferenceRunOrganization] = OMIT,
        model_version: typing.Optional[int] = OMIT,
        created_by: typing.Optional[InferenceRunCreatedBy] = OMIT,
        status: typing.Optional[InferenceRunStatus] = OMIT,
        job_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        triggered_at: typing.Optional[dt.datetime] = OMIT,
        predictions_updated_at: typing.Optional[dt.datetime] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InferenceRun:
        """
        Run a prompt inference.

        Parameters
        ----------
        id : int
            Prompt ID

        version_id : int
            Prompt Version ID

        project : int

        project_subset : InferenceRunProjectSubset

        organization : typing.Optional[InferenceRunOrganization]

        model_version : typing.Optional[int]

        created_by : typing.Optional[InferenceRunCreatedBy]

        status : typing.Optional[InferenceRunStatus]

        job_id : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        triggered_at : typing.Optional[dt.datetime]

        predictions_updated_at : typing.Optional[dt.datetime]

        completed_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InferenceRun


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.prompts.runs.create(
                id=1,
                version_id=1,
                project=1,
                project_subset="All",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/prompts/{jsonable_encoder(id)}/versions/{jsonable_encoder(version_id)}/inference-runs",
            method="POST",
            json={
                "organization": convert_and_respect_annotation_metadata(
                    object_=organization, annotation=InferenceRunOrganization, direction="write"
                ),
                "project": project,
                "model_version": model_version,
                "created_by": convert_and_respect_annotation_metadata(
                    object_=created_by, annotation=InferenceRunCreatedBy, direction="write"
                ),
                "project_subset": project_subset,
                "status": status,
                "job_id": job_id,
                "created_at": created_at,
                "triggered_at": triggered_at,
                "predictions_updated_at": predictions_updated_at,
                "completed_at": completed_at,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    InferenceRun,
                    parse_obj_as(
                        type_=InferenceRun,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
