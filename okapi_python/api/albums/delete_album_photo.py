from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.success_response import SuccessResponse
from ...types import Response


def _get_kwargs(
    album_id: str,
    photo_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/albums/{album_id}/photos/{photo_id}".format(
            album_id=quote(str(album_id), safe=""),
            photo_id=quote(str(photo_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SuccessResponse | None:
    if response.status_code == 200:
        response_200 = SuccessResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | SuccessResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    album_id: str,
    photo_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | SuccessResponse]:
    """Delete a photo

     Deletes the photo. OK deletes a photo by its id: the album in the path is not checked against it.
    The deletion is soft on OK (it can restore the photo), which the API does not expose.

    Args:
        album_id (str):
        photo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SuccessResponse]
    """

    kwargs = _get_kwargs(
        album_id=album_id,
        photo_id=photo_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    album_id: str,
    photo_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | SuccessResponse | None:
    """Delete a photo

     Deletes the photo. OK deletes a photo by its id: the album in the path is not checked against it.
    The deletion is soft on OK (it can restore the photo), which the API does not expose.

    Args:
        album_id (str):
        photo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SuccessResponse
    """

    return sync_detailed(
        album_id=album_id,
        photo_id=photo_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    album_id: str,
    photo_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | SuccessResponse]:
    """Delete a photo

     Deletes the photo. OK deletes a photo by its id: the album in the path is not checked against it.
    The deletion is soft on OK (it can restore the photo), which the API does not expose.

    Args:
        album_id (str):
        photo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SuccessResponse]
    """

    kwargs = _get_kwargs(
        album_id=album_id,
        photo_id=photo_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    album_id: str,
    photo_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | SuccessResponse | None:
    """Delete a photo

     Deletes the photo. OK deletes a photo by its id: the album in the path is not checked against it.
    The deletion is soft on OK (it can restore the photo), which the API does not expose.

    Args:
        album_id (str):
        photo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SuccessResponse
    """

    return (
        await asyncio_detailed(
            album_id=album_id,
            photo_id=photo_id,
            client=client,
        )
    ).parsed
