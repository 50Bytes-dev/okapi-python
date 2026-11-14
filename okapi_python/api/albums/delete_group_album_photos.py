from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_album_photos_request import DeleteAlbumPhotosRequest
from ...models.delete_album_photos_response import DeleteAlbumPhotosResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    group_id: int,
    album_id: str,
    *,
    body: DeleteAlbumPhotosRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/groups/{group_id}/albums/{album_id}/photos/delete".format(
            group_id=quote(str(group_id), safe=""),
            album_id=quote(str(album_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteAlbumPhotosResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DeleteAlbumPhotosResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if response.status_code >= 400:
        # okapi-python: every error of the gateway is the ErrorResponse envelope, also on a status the schema does
        # not list for this call.
        try:
            error_body = response.json()
        except ValueError:
            error_body = None
        if (
            isinstance(error_body, dict)
            and error_body.get("success") is False
            and isinstance(error_body.get("code"), str)
        ):
            return ErrorResponse.from_dict(error_body)

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteAlbumPhotosResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    album_id: str,
    *,
    client: AuthenticatedClient,
    body: DeleteAlbumPhotosRequest,
) -> Response[DeleteAlbumPhotosResponse | ErrorResponse]:
    """Delete photos of a group's album

     Deletes up to 100 photos, one call to OK each (OK deletes a photo by its id: the album in the path
    is not checked against it), and answers each: `deleted`, `not_found`, `forbidden`, or `failed` with
    the `code` its own delete would have answered. A failure that stops every later call (`paused`,
    `not_logged_in`, `not_connected`) and the request's time running out (120 s at most) leave the rest
    `skipped` with that `code`; a stop signal pauses the OK user and the answer carries the `pause`.
    Nothing is retried.

    Args:
        group_id (int):
        album_id (str):
        body (DeleteAlbumPhotosRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAlbumPhotosResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        album_id=album_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    album_id: str,
    *,
    client: AuthenticatedClient,
    body: DeleteAlbumPhotosRequest,
) -> DeleteAlbumPhotosResponse | ErrorResponse | None:
    """Delete photos of a group's album

     Deletes up to 100 photos, one call to OK each (OK deletes a photo by its id: the album in the path
    is not checked against it), and answers each: `deleted`, `not_found`, `forbidden`, or `failed` with
    the `code` its own delete would have answered. A failure that stops every later call (`paused`,
    `not_logged_in`, `not_connected`) and the request's time running out (120 s at most) leave the rest
    `skipped` with that `code`; a stop signal pauses the OK user and the answer carries the `pause`.
    Nothing is retried.

    Args:
        group_id (int):
        album_id (str):
        body (DeleteAlbumPhotosRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAlbumPhotosResponse | ErrorResponse
    """

    return sync_detailed(
        group_id=group_id,
        album_id=album_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    album_id: str,
    *,
    client: AuthenticatedClient,
    body: DeleteAlbumPhotosRequest,
) -> Response[DeleteAlbumPhotosResponse | ErrorResponse]:
    """Delete photos of a group's album

     Deletes up to 100 photos, one call to OK each (OK deletes a photo by its id: the album in the path
    is not checked against it), and answers each: `deleted`, `not_found`, `forbidden`, or `failed` with
    the `code` its own delete would have answered. A failure that stops every later call (`paused`,
    `not_logged_in`, `not_connected`) and the request's time running out (120 s at most) leave the rest
    `skipped` with that `code`; a stop signal pauses the OK user and the answer carries the `pause`.
    Nothing is retried.

    Args:
        group_id (int):
        album_id (str):
        body (DeleteAlbumPhotosRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAlbumPhotosResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        album_id=album_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    album_id: str,
    *,
    client: AuthenticatedClient,
    body: DeleteAlbumPhotosRequest,
) -> DeleteAlbumPhotosResponse | ErrorResponse | None:
    """Delete photos of a group's album

     Deletes up to 100 photos, one call to OK each (OK deletes a photo by its id: the album in the path
    is not checked against it), and answers each: `deleted`, `not_found`, `forbidden`, or `failed` with
    the `code` its own delete would have answered. A failure that stops every later call (`paused`,
    `not_logged_in`, `not_connected`) and the request's time running out (120 s at most) leave the rest
    `skipped` with that `code`; a stop signal pauses the OK user and the answer carries the `pause`.
    Nothing is retried.

    Args:
        group_id (int):
        album_id (str):
        body (DeleteAlbumPhotosRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAlbumPhotosResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            album_id=album_id,
            client=client,
            body=body,
        )
    ).parsed
