from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.photo_response import PhotoResponse
from ...models.update_album_photo_request import UpdateAlbumPhotoRequest
from ...types import Response


def _get_kwargs(
    group_id: int,
    album_id: str,
    photo_id: str,
    *,
    body: UpdateAlbumPhotoRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/groups/{group_id}/albums/{album_id}/photos/{photo_id}".format(
            group_id=quote(str(group_id), safe=""),
            album_id=quote(str(album_id), safe=""),
            photo_id=quote(str(photo_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PhotoResponse | None:
    if response.status_code == 200:
        response_200 = PhotoResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if response.status_code == 504:
        response_504 = ErrorResponse.from_dict(response.json())

        return response_504

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
) -> Response[ErrorResponse | PhotoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    album_id: str,
    photo_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAlbumPhotoRequest,
) -> Response[ErrorResponse | PhotoResponse]:
    r"""Change a group photo's description

     Sets the photo's description (at most 4096 UTF-16 units; `\"\"` clears it).
    OK sets a photo's text by the photo's id and answers no more than
    success: the answer carries the ids and the new text, and the album in the
    path is not checked against the photo. OK takes a text for a photo it
    deleted, too.

    Args:
        group_id (int):
        album_id (str):
        photo_id (str):
        body (UpdateAlbumPhotoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PhotoResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        album_id=album_id,
        photo_id=photo_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    album_id: str,
    photo_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAlbumPhotoRequest,
) -> ErrorResponse | PhotoResponse | None:
    r"""Change a group photo's description

     Sets the photo's description (at most 4096 UTF-16 units; `\"\"` clears it).
    OK sets a photo's text by the photo's id and answers no more than
    success: the answer carries the ids and the new text, and the album in the
    path is not checked against the photo. OK takes a text for a photo it
    deleted, too.

    Args:
        group_id (int):
        album_id (str):
        photo_id (str):
        body (UpdateAlbumPhotoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PhotoResponse
    """

    return sync_detailed(
        group_id=group_id,
        album_id=album_id,
        photo_id=photo_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    album_id: str,
    photo_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAlbumPhotoRequest,
) -> Response[ErrorResponse | PhotoResponse]:
    r"""Change a group photo's description

     Sets the photo's description (at most 4096 UTF-16 units; `\"\"` clears it).
    OK sets a photo's text by the photo's id and answers no more than
    success: the answer carries the ids and the new text, and the album in the
    path is not checked against the photo. OK takes a text for a photo it
    deleted, too.

    Args:
        group_id (int):
        album_id (str):
        photo_id (str):
        body (UpdateAlbumPhotoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PhotoResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        album_id=album_id,
        photo_id=photo_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    album_id: str,
    photo_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAlbumPhotoRequest,
) -> ErrorResponse | PhotoResponse | None:
    r"""Change a group photo's description

     Sets the photo's description (at most 4096 UTF-16 units; `\"\"` clears it).
    OK sets a photo's text by the photo's id and answers no more than
    success: the answer carries the ids and the new text, and the album in the
    path is not checked against the photo. OK takes a text for a photo it
    deleted, too.

    Args:
        group_id (int):
        album_id (str):
        photo_id (str):
        body (UpdateAlbumPhotoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PhotoResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            album_id=album_id,
            photo_id=photo_id,
            client=client,
            body=body,
        )
    ).parsed
