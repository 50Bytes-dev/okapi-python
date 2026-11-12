from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.member_list_response import MemberListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chat_id: int,
    *,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chats/{chat_id}/members".format(
            chat_id=quote(str(chat_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | MemberListResponse | None:
    if response.status_code == 200:
        response_200 = MemberListResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | MemberListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chat_id: int,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | MemberListResponse]:
    """The chat's members

     The members of a chat, one page at a time; `nextCursor` gives the next page.

    Args:
        chat_id (int):
        q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MemberListResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        q=q,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chat_id: int,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | MemberListResponse | None:
    """The chat's members

     The members of a chat, one page at a time; `nextCursor` gives the next page.

    Args:
        chat_id (int):
        q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MemberListResponse
    """

    return sync_detailed(
        chat_id=chat_id,
        client=client,
        q=q,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    chat_id: int,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ErrorResponse | MemberListResponse]:
    """The chat's members

     The members of a chat, one page at a time; `nextCursor` gives the next page.

    Args:
        chat_id (int):
        q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MemberListResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        q=q,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chat_id: int,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ErrorResponse | MemberListResponse | None:
    """The chat's members

     The members of a chat, one page at a time; `nextCursor` gives the next page.

    Args:
        chat_id (int):
        q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MemberListResponse
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            client=client,
            q=q,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
