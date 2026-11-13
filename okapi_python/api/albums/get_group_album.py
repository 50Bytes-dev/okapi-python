from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_response import AlbumResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    group_id: int,
    album_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups/{group_id}/albums/{album_id}".format(
            group_id=quote(str(group_id), safe=""),
            album_id=quote(str(album_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlbumResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AlbumResponse.from_dict(response.json())

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
) -> Response[AlbumResponse | ErrorResponse]:
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
) -> Response[AlbumResponse | ErrorResponse]:
    """Get a group album

    Args:
        group_id (int):
        album_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        album_id=album_id,
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
) -> AlbumResponse | ErrorResponse | None:
    """Get a group album

    Args:
        group_id (int):
        album_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumResponse | ErrorResponse
    """

    return sync_detailed(
        group_id=group_id,
        album_id=album_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    album_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AlbumResponse | ErrorResponse]:
    """Get a group album

    Args:
        group_id (int):
        album_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlbumResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        album_id=album_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    album_id: str,
    *,
    client: AuthenticatedClient,
) -> AlbumResponse | ErrorResponse | None:
    """Get a group album

    Args:
        group_id (int):
        album_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlbumResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            album_id=album_id,
            client=client,
        )
    ).parsed
