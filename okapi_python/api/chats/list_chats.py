from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_list_response import ChatListResponse
from ...models.chat_type import ChatType
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: list[ChatType] | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item = type_item_data.value
            json_type_.append(type_item)

    params["type"] = json_type_

    params["q"] = q

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChatListResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = ChatListResponse.from_dict(response.json())

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
) -> Response[ChatListResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    type_: list[ChatType] | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ChatListResponse | ErrorResponse]:
    """List or search the chats

     The account's chats, newest event first, one page at a time;
    `nextCursor` gives the next page and only its absence means the end.
    With `q`, the chats whose title matches, as OK's search finds them.
    `type` keeps only the given chat types. OK filters by neither, so
    the gateway reads OK's pages and keeps the wanted chats, at most 10
    of OK's pages per request: a page may hold fewer than `limit` chats,
    even none, and still have a `nextCursor`. A dialog OK gives no title
    is titled with the other person's name.

    Args:
        type_ (list[ChatType] | Unset):
        q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatListResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        q=q,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    type_: list[ChatType] | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ChatListResponse | ErrorResponse | None:
    """List or search the chats

     The account's chats, newest event first, one page at a time;
    `nextCursor` gives the next page and only its absence means the end.
    With `q`, the chats whose title matches, as OK's search finds them.
    `type` keeps only the given chat types. OK filters by neither, so
    the gateway reads OK's pages and keeps the wanted chats, at most 10
    of OK's pages per request: a page may hold fewer than `limit` chats,
    even none, and still have a `nextCursor`. A dialog OK gives no title
    is titled with the other person's name.

    Args:
        type_ (list[ChatType] | Unset):
        q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatListResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        type_=type_,
        q=q,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_: list[ChatType] | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[ChatListResponse | ErrorResponse]:
    """List or search the chats

     The account's chats, newest event first, one page at a time;
    `nextCursor` gives the next page and only its absence means the end.
    With `q`, the chats whose title matches, as OK's search finds them.
    `type` keeps only the given chat types. OK filters by neither, so
    the gateway reads OK's pages and keeps the wanted chats, at most 10
    of OK's pages per request: a page may hold fewer than `limit` chats,
    even none, and still have a `nextCursor`. A dialog OK gives no title
    is titled with the other person's name.

    Args:
        type_ (list[ChatType] | Unset):
        q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatListResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        q=q,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    type_: list[ChatType] | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> ChatListResponse | ErrorResponse | None:
    """List or search the chats

     The account's chats, newest event first, one page at a time;
    `nextCursor` gives the next page and only its absence means the end.
    With `q`, the chats whose title matches, as OK's search finds them.
    `type` keeps only the given chat types. OK filters by neither, so
    the gateway reads OK's pages and keeps the wanted chats, at most 10
    of OK's pages per request: a page may hold fewer than `limit` chats,
    even none, and still have a `nextCursor`. A dialog OK gives no title
    is titled with the other person's name.

    Args:
        type_ (list[ChatType] | Unset):
        q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatListResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            q=q,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
