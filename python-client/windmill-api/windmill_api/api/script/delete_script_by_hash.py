from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.delete_script_by_hash_response_200 import DeleteScriptByHashResponse200
from ...types import Response


def _get_kwargs(
    workspace: str,
    hash_: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/w/{workspace}/scripts/delete/h/{hash}".format(client.base_url, workspace=workspace, hash=hash_)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[DeleteScriptByHashResponse200]:
    if response.status_code == 200:
        response_200 = DeleteScriptByHashResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[DeleteScriptByHashResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    hash_: str,
    *,
    client: Client,
) -> Response[DeleteScriptByHashResponse200]:
    """delete script by hash (erase content but keep hash)

    Args:
        workspace (str):
        hash_ (str):

    Returns:
        Response[DeleteScriptByHashResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        hash_=hash_,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    hash_: str,
    *,
    client: Client,
) -> Optional[DeleteScriptByHashResponse200]:
    """delete script by hash (erase content but keep hash)

    Args:
        workspace (str):
        hash_ (str):

    Returns:
        Response[DeleteScriptByHashResponse200]
    """

    return sync_detailed(
        workspace=workspace,
        hash_=hash_,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    hash_: str,
    *,
    client: Client,
) -> Response[DeleteScriptByHashResponse200]:
    """delete script by hash (erase content but keep hash)

    Args:
        workspace (str):
        hash_ (str):

    Returns:
        Response[DeleteScriptByHashResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        hash_=hash_,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    hash_: str,
    *,
    client: Client,
) -> Optional[DeleteScriptByHashResponse200]:
    """delete script by hash (erase content but keep hash)

    Args:
        workspace (str):
        hash_ (str):

    Returns:
        Response[DeleteScriptByHashResponse200]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            hash_=hash_,
            client=client,
        )
    ).parsed