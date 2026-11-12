from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.health_response import HealthResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/health",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HealthResponse | None:
    if response.status_code == 200:
        response_200 = HealthResponse.from_dict(response.json())

        return response_200

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 503:
        response_503 = HealthResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HealthResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | HealthResponse]:
    """Gateway health

     Answers 200 when the database answers a ping, 503 otherwise. OK is not checked.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HealthResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | HealthResponse | None:
    """Gateway health

     Answers 200 when the database answers a ping, 503 otherwise. OK is not checked.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HealthResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | HealthResponse]:
    """Gateway health

     Answers 200 when the database answers a ping, 503 otherwise. OK is not checked.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HealthResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | HealthResponse | None:
    """Gateway health

     Answers 200 when the database answers a ping, 503 otherwise. OK is not checked.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HealthResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
