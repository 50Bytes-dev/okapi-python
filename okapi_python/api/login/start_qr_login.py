from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.login_response import LoginResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/session/login/qr",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | LoginResponse | None:
    if response.status_code == 200:
        response_200 = LoginResponse.from_dict(response.json())

        return response_200

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
) -> Response[ErrorResponse | LoginResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | LoginResponse]:
    """Start a login by QR code

     Asks ok.ru for a login QR code and answers once it exists. A running
    login is cancelled first. The owner scans the QR with the OK app
    (or opens `link` on the phone where the app is) and confirms the
    login there. **Check that the 4-digit code the app shows is `code`**
    before confirming: it ties the scan to this QR. The login then
    becomes `done` and the session connects (`Connected`); unconfirmed
    within `OKAPI_LOGIN_TIMEOUT` it fails `expired`. A profile with OK's
    two-factor protection goes to step `code` after the confirmation:
    OK sends a code by SMS, given with `POST /session/login/code`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | LoginResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | LoginResponse | None:
    """Start a login by QR code

     Asks ok.ru for a login QR code and answers once it exists. A running
    login is cancelled first. The owner scans the QR with the OK app
    (or opens `link` on the phone where the app is) and confirms the
    login there. **Check that the 4-digit code the app shows is `code`**
    before confirming: it ties the scan to this QR. The login then
    becomes `done` and the session connects (`Connected`); unconfirmed
    within `OKAPI_LOGIN_TIMEOUT` it fails `expired`. A profile with OK's
    two-factor protection goes to step `code` after the confirmation:
    OK sends a code by SMS, given with `POST /session/login/code`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | LoginResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | LoginResponse]:
    """Start a login by QR code

     Asks ok.ru for a login QR code and answers once it exists. A running
    login is cancelled first. The owner scans the QR with the OK app
    (or opens `link` on the phone where the app is) and confirms the
    login there. **Check that the 4-digit code the app shows is `code`**
    before confirming: it ties the scan to this QR. The login then
    becomes `done` and the session connects (`Connected`); unconfirmed
    within `OKAPI_LOGIN_TIMEOUT` it fails `expired`. A profile with OK's
    two-factor protection goes to step `code` after the confirmation:
    OK sends a code by SMS, given with `POST /session/login/code`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | LoginResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | LoginResponse | None:
    """Start a login by QR code

     Asks ok.ru for a login QR code and answers once it exists. A running
    login is cancelled first. The owner scans the QR with the OK app
    (or opens `link` on the phone where the app is) and confirms the
    login there. **Check that the 4-digit code the app shows is `code`**
    before confirming: it ties the scan to this QR. The login then
    becomes `done` and the session connects (`Connected`); unconfirmed
    within `OKAPI_LOGIN_TIMEOUT` it fails `expired`. A profile with OK's
    two-factor protection goes to step `code` after the confirmation:
    OK sends a code by SMS, given with `POST /session/login/code`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | LoginResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
