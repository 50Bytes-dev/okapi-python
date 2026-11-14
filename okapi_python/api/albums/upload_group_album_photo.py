from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.upload_album_photo_form import UploadAlbumPhotoForm
from ...models.upload_album_photo_request import UploadAlbumPhotoRequest
from ...models.upload_photo_response import UploadPhotoResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    album_id: str,
    *,
    body: UploadAlbumPhotoForm | UploadAlbumPhotoRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/groups/{group_id}/albums/{album_id}/photos".format(
            group_id=quote(str(group_id), safe=""),
            album_id=quote(str(album_id), safe=""),
        ),
    }

    if isinstance(body, UploadAlbumPhotoForm):
        _kwargs["files"] = body.to_multipart()

    if isinstance(body, UploadAlbumPhotoRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | UploadPhotoResponse | None:
    if response.status_code == 200:
        response_200 = UploadPhotoResponse.from_dict(response.json())

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

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

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
) -> Response[ErrorResponse | UploadPhotoResponse]:
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
    body: UploadAlbumPhotoForm | UploadAlbumPhotoRequest | Unset = UNSET,
) -> Response[ErrorResponse | UploadPhotoResponse]:
    """Upload a photo into a group album

     Uploads a photo into the album and sets its `description` when one is
    given. Send it as multipart (`file`, and `description` as a text field
    before or after it) or as JSON with either `url` (fetched by the gateway;
    internal addresses are refused) or `data` (base64 or a base64 data URL),
    and `description`.

    The photo is prepared for OK's albums first. An upright JPEG of at most
    2560 px a side goes **as it came**, metadata included; anything else (PNG,
    WebP, GIF, BMP, a larger or EXIF-turned JPEG) is decoded, turned upright,
    fitted into 2560×2560 px and re-encoded as a JPEG at quality 0.9. OK
    stores every photo as its own JPEG.

    The description (at most 4096 UTF-16 units) is checked before anything
    is uploaded. When the photo is up and OK does not take its description,
    the answer is `502 description_failed` with the `photoId`: set the text
    again with `PATCH`, do not upload again.

    Give an upload a `ref` (your idempotency key, up to 128 bytes, a
    multipart field or a JSON field): a repeat of it never uploads a second
    photo. A repeat of an upload whose photo was added answers that photo
    as first answered, with `duplicate: true`, even when it was deleted
    since (setting its description first, when that
    failed before); one whose first ended without an answer (`504 timeout`)
    looks for the photo in the album, by the id OK allocated it before the
    image was sent, and uploads again only when it is not there. The same
    `ref` with another album is `400 invalid_input`. A ref is remembered for
    7 days. Without a ref, list the album after a `504 timeout` to see
    whether the photo came. OK's own limit on new photos (1000 in 5 min,
    10000 a day) is `429 photo_limit`; the gateway keeps no pace of its own.

    OK decides who may upload; the album's `canUpload` tells beforehand (a moderator into any album, a
    member where the album is open to members, as OK's list of the group's albums tells it).

    Args:
        group_id (int):
        album_id (str):
        body (UploadAlbumPhotoForm):
        body (UploadAlbumPhotoRequest): Exactly one of `url` and `data`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UploadPhotoResponse]
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
    body: UploadAlbumPhotoForm | UploadAlbumPhotoRequest | Unset = UNSET,
) -> ErrorResponse | UploadPhotoResponse | None:
    """Upload a photo into a group album

     Uploads a photo into the album and sets its `description` when one is
    given. Send it as multipart (`file`, and `description` as a text field
    before or after it) or as JSON with either `url` (fetched by the gateway;
    internal addresses are refused) or `data` (base64 or a base64 data URL),
    and `description`.

    The photo is prepared for OK's albums first. An upright JPEG of at most
    2560 px a side goes **as it came**, metadata included; anything else (PNG,
    WebP, GIF, BMP, a larger or EXIF-turned JPEG) is decoded, turned upright,
    fitted into 2560×2560 px and re-encoded as a JPEG at quality 0.9. OK
    stores every photo as its own JPEG.

    The description (at most 4096 UTF-16 units) is checked before anything
    is uploaded. When the photo is up and OK does not take its description,
    the answer is `502 description_failed` with the `photoId`: set the text
    again with `PATCH`, do not upload again.

    Give an upload a `ref` (your idempotency key, up to 128 bytes, a
    multipart field or a JSON field): a repeat of it never uploads a second
    photo. A repeat of an upload whose photo was added answers that photo
    as first answered, with `duplicate: true`, even when it was deleted
    since (setting its description first, when that
    failed before); one whose first ended without an answer (`504 timeout`)
    looks for the photo in the album, by the id OK allocated it before the
    image was sent, and uploads again only when it is not there. The same
    `ref` with another album is `400 invalid_input`. A ref is remembered for
    7 days. Without a ref, list the album after a `504 timeout` to see
    whether the photo came. OK's own limit on new photos (1000 in 5 min,
    10000 a day) is `429 photo_limit`; the gateway keeps no pace of its own.

    OK decides who may upload; the album's `canUpload` tells beforehand (a moderator into any album, a
    member where the album is open to members, as OK's list of the group's albums tells it).

    Args:
        group_id (int):
        album_id (str):
        body (UploadAlbumPhotoForm):
        body (UploadAlbumPhotoRequest): Exactly one of `url` and `data`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UploadPhotoResponse
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
    body: UploadAlbumPhotoForm | UploadAlbumPhotoRequest | Unset = UNSET,
) -> Response[ErrorResponse | UploadPhotoResponse]:
    """Upload a photo into a group album

     Uploads a photo into the album and sets its `description` when one is
    given. Send it as multipart (`file`, and `description` as a text field
    before or after it) or as JSON with either `url` (fetched by the gateway;
    internal addresses are refused) or `data` (base64 or a base64 data URL),
    and `description`.

    The photo is prepared for OK's albums first. An upright JPEG of at most
    2560 px a side goes **as it came**, metadata included; anything else (PNG,
    WebP, GIF, BMP, a larger or EXIF-turned JPEG) is decoded, turned upright,
    fitted into 2560×2560 px and re-encoded as a JPEG at quality 0.9. OK
    stores every photo as its own JPEG.

    The description (at most 4096 UTF-16 units) is checked before anything
    is uploaded. When the photo is up and OK does not take its description,
    the answer is `502 description_failed` with the `photoId`: set the text
    again with `PATCH`, do not upload again.

    Give an upload a `ref` (your idempotency key, up to 128 bytes, a
    multipart field or a JSON field): a repeat of it never uploads a second
    photo. A repeat of an upload whose photo was added answers that photo
    as first answered, with `duplicate: true`, even when it was deleted
    since (setting its description first, when that
    failed before); one whose first ended without an answer (`504 timeout`)
    looks for the photo in the album, by the id OK allocated it before the
    image was sent, and uploads again only when it is not there. The same
    `ref` with another album is `400 invalid_input`. A ref is remembered for
    7 days. Without a ref, list the album after a `504 timeout` to see
    whether the photo came. OK's own limit on new photos (1000 in 5 min,
    10000 a day) is `429 photo_limit`; the gateway keeps no pace of its own.

    OK decides who may upload; the album's `canUpload` tells beforehand (a moderator into any album, a
    member where the album is open to members, as OK's list of the group's albums tells it).

    Args:
        group_id (int):
        album_id (str):
        body (UploadAlbumPhotoForm):
        body (UploadAlbumPhotoRequest): Exactly one of `url` and `data`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UploadPhotoResponse]
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
    body: UploadAlbumPhotoForm | UploadAlbumPhotoRequest | Unset = UNSET,
) -> ErrorResponse | UploadPhotoResponse | None:
    """Upload a photo into a group album

     Uploads a photo into the album and sets its `description` when one is
    given. Send it as multipart (`file`, and `description` as a text field
    before or after it) or as JSON with either `url` (fetched by the gateway;
    internal addresses are refused) or `data` (base64 or a base64 data URL),
    and `description`.

    The photo is prepared for OK's albums first. An upright JPEG of at most
    2560 px a side goes **as it came**, metadata included; anything else (PNG,
    WebP, GIF, BMP, a larger or EXIF-turned JPEG) is decoded, turned upright,
    fitted into 2560×2560 px and re-encoded as a JPEG at quality 0.9. OK
    stores every photo as its own JPEG.

    The description (at most 4096 UTF-16 units) is checked before anything
    is uploaded. When the photo is up and OK does not take its description,
    the answer is `502 description_failed` with the `photoId`: set the text
    again with `PATCH`, do not upload again.

    Give an upload a `ref` (your idempotency key, up to 128 bytes, a
    multipart field or a JSON field): a repeat of it never uploads a second
    photo. A repeat of an upload whose photo was added answers that photo
    as first answered, with `duplicate: true`, even when it was deleted
    since (setting its description first, when that
    failed before); one whose first ended without an answer (`504 timeout`)
    looks for the photo in the album, by the id OK allocated it before the
    image was sent, and uploads again only when it is not there. The same
    `ref` with another album is `400 invalid_input`. A ref is remembered for
    7 days. Without a ref, list the album after a `504 timeout` to see
    whether the photo came. OK's own limit on new photos (1000 in 5 min,
    10000 a day) is `429 photo_limit`; the gateway keeps no pace of its own.

    OK decides who may upload; the album's `canUpload` tells beforehand (a moderator into any album, a
    member where the album is open to members, as OK's list of the group's albums tells it).

    Args:
        group_id (int):
        album_id (str):
        body (UploadAlbumPhotoForm):
        body (UploadAlbumPhotoRequest): Exactly one of `url` and `data`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UploadPhotoResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            album_id=album_id,
            client=client,
            body=body,
        )
    ).parsed
