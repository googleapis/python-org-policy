# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Mapping, MutableMapping, MutableSequence, Optional, Sequence, Tuple, Type, Union

from google.cloud.orgpolicy_v2 import gapic_version as package_version

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials   # type: ignore
from google.oauth2 import service_account              # type: ignore

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object]  # type: ignore

from google.cloud.orgpolicy_v2.services.org_policy import pagers
from google.cloud.orgpolicy_v2.types import constraint
from google.cloud.orgpolicy_v2.types import orgpolicy
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import OrgPolicyTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import OrgPolicyGrpcAsyncIOTransport
from .client import OrgPolicyClient


class OrgPolicyAsyncClient:
    """An interface for managing organization policies.

    The Organization Policy Service provides a simple mechanism for
    organizations to restrict the allowed configurations across
    their entire resource hierarchy.

    You can use a policy to configure restrictions on resources. For
    example, you can enforce a policy that restricts which Google
    Cloud APIs can be activated in a certain part of your resource
    hierarchy, or prevents serial port access to VM instances in a
    particular folder.

    Policies are inherited down through the resource hierarchy. A
    policy applied to a parent resource automatically applies to all
    its child resources unless overridden with a policy lower in the
    hierarchy.

    A constraint defines an aspect of a resource's configuration
    that can be controlled by an organization's policy
    administrator. Policies are a collection of constraints that
    defines their allowable configuration on a particular resource
    and its child resources.
    """

    _client: OrgPolicyClient

    DEFAULT_ENDPOINT = OrgPolicyClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = OrgPolicyClient.DEFAULT_MTLS_ENDPOINT

    constraint_path = staticmethod(OrgPolicyClient.constraint_path)
    parse_constraint_path = staticmethod(OrgPolicyClient.parse_constraint_path)
    custom_constraint_path = staticmethod(OrgPolicyClient.custom_constraint_path)
    parse_custom_constraint_path = staticmethod(OrgPolicyClient.parse_custom_constraint_path)
    policy_path = staticmethod(OrgPolicyClient.policy_path)
    parse_policy_path = staticmethod(OrgPolicyClient.parse_policy_path)
    common_billing_account_path = staticmethod(OrgPolicyClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(OrgPolicyClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(OrgPolicyClient.common_folder_path)
    parse_common_folder_path = staticmethod(OrgPolicyClient.parse_common_folder_path)
    common_organization_path = staticmethod(OrgPolicyClient.common_organization_path)
    parse_common_organization_path = staticmethod(OrgPolicyClient.parse_common_organization_path)
    common_project_path = staticmethod(OrgPolicyClient.common_project_path)
    parse_common_project_path = staticmethod(OrgPolicyClient.parse_common_project_path)
    common_location_path = staticmethod(OrgPolicyClient.common_location_path)
    parse_common_location_path = staticmethod(OrgPolicyClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            OrgPolicyAsyncClient: The constructed client.
        """
        return OrgPolicyClient.from_service_account_info.__func__(OrgPolicyAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            OrgPolicyAsyncClient: The constructed client.
        """
        return OrgPolicyClient.from_service_account_file.__func__(OrgPolicyAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: Optional[ClientOptions] = None):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return OrgPolicyClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> OrgPolicyTransport:
        """Returns the transport used by the client instance.

        Returns:
            OrgPolicyTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(OrgPolicyClient).get_transport_class, type(OrgPolicyClient))

    def __init__(self, *,
            credentials: Optional[ga_credentials.Credentials] = None,
            transport: Union[str, OrgPolicyTransport] = "grpc_asyncio",
            client_options: Optional[ClientOptions] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the org policy client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.OrgPolicyTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = OrgPolicyClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def list_constraints(self,
            request: Optional[Union[orgpolicy.ListConstraintsRequest, dict]] = None,
            *,
            parent: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListConstraintsAsyncPager:
        r"""Lists constraints that could be applied on the
        specified resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import orgpolicy_v2

            async def sample_list_constraints():
                # Create a client
                client = orgpolicy_v2.OrgPolicyAsyncClient()

                # Initialize request argument(s)
                request = orgpolicy_v2.ListConstraintsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_constraints(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.orgpolicy_v2.types.ListConstraintsRequest, dict]]):
                The request object. The request sent to the [ListConstraints]
                [google.cloud.orgpolicy.v2.OrgPolicy.ListConstraints]
                method.
            parent (:class:`str`):
                Required. The Google Cloud resource that parents the
                constraint. Must be in one of the following forms:

                -  ``projects/{project_number}``
                -  ``projects/{project_id}``
                -  ``folders/{folder_id}``
                -  ``organizations/{organization_id}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.orgpolicy_v2.services.org_policy.pagers.ListConstraintsAsyncPager:
                The response returned from the [ListConstraints]
                   [google.cloud.orgpolicy.v2.OrgPolicy.ListConstraints]
                   method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = orgpolicy.ListConstraintsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_constraints,
            default_retry=retries.AsyncRetry(
initial=1.0,maximum=10.0,multiplier=1.3,                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListConstraintsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_policies(self,
            request: Optional[Union[orgpolicy.ListPoliciesRequest, dict]] = None,
            *,
            parent: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListPoliciesAsyncPager:
        r"""Retrieves all of the policies that exist on a
        particular resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import orgpolicy_v2

            async def sample_list_policies():
                # Create a client
                client = orgpolicy_v2.OrgPolicyAsyncClient()

                # Initialize request argument(s)
                request = orgpolicy_v2.ListPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_policies(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.orgpolicy_v2.types.ListPoliciesRequest, dict]]):
                The request object. The request sent to the [ListPolicies]
                [google.cloud.orgpolicy.v2.OrgPolicy.ListPolicies]
                method.
            parent (:class:`str`):
                Required. The target Google Cloud resource that parents
                the set of constraints and policies that will be
                returned from this call. Must be in one of the following
                forms:

                -  ``projects/{project_number}``
                -  ``projects/{project_id}``
                -  ``folders/{folder_id}``
                -  ``organizations/{organization_id}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.orgpolicy_v2.services.org_policy.pagers.ListPoliciesAsyncPager:
                The response returned from the [ListPolicies]
                   [google.cloud.orgpolicy.v2.OrgPolicy.ListPolicies]
                   method. It will be empty if no policies are set on
                   the resource.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = orgpolicy.ListPoliciesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_policies,
            default_retry=retries.AsyncRetry(
initial=1.0,maximum=10.0,multiplier=1.3,                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListPoliciesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_policy(self,
            request: Optional[Union[orgpolicy.GetPolicyRequest, dict]] = None,
            *,
            name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> orgpolicy.Policy:
        r"""Gets a policy on a resource.

        If no policy is set on the resource, ``NOT_FOUND`` is returned.
        The ``etag`` value can be used with ``UpdatePolicy()`` to update
        a policy during read-modify-write.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import orgpolicy_v2

            async def sample_get_policy():
                # Create a client
                client = orgpolicy_v2.OrgPolicyAsyncClient()

                # Initialize request argument(s)
                request = orgpolicy_v2.GetPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orgpolicy_v2.types.GetPolicyRequest, dict]]):
                The request object. The request sent to the [GetPolicy]
                [google.cloud.orgpolicy.v2.OrgPolicy.GetPolicy] method.
            name (:class:`str`):
                Required. Resource name of the policy. See
                [Policy][google.cloud.orgpolicy.v2.Policy] for naming
                requirements.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.orgpolicy_v2.types.Policy:
                Defines an organization policy which
                is used to specify constraints for
                configurations of Google Cloud
                resources.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = orgpolicy.GetPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_policy,
            default_retry=retries.AsyncRetry(
initial=1.0,maximum=10.0,multiplier=1.3,                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_effective_policy(self,
            request: Optional[Union[orgpolicy.GetEffectivePolicyRequest, dict]] = None,
            *,
            name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> orgpolicy.Policy:
        r"""Gets the effective policy on a resource. This is the result of
        merging policies in the resource hierarchy and evaluating
        conditions. The returned policy will not have an ``etag`` or
        ``condition`` set because it is an evaluated policy across
        multiple resources. Subtrees of Resource Manager resource
        hierarchy with 'under:' prefix will not be expanded.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import orgpolicy_v2

            async def sample_get_effective_policy():
                # Create a client
                client = orgpolicy_v2.OrgPolicyAsyncClient()

                # Initialize request argument(s)
                request = orgpolicy_v2.GetEffectivePolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_effective_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orgpolicy_v2.types.GetEffectivePolicyRequest, dict]]):
                The request object. The request sent to the [GetEffectivePolicy]
                [google.cloud.orgpolicy.v2.OrgPolicy.GetEffectivePolicy]
                method.
            name (:class:`str`):
                Required. The effective policy to compute. See
                [Policy][google.cloud.orgpolicy.v2.Policy] for naming
                requirements.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.orgpolicy_v2.types.Policy:
                Defines an organization policy which
                is used to specify constraints for
                configurations of Google Cloud
                resources.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = orgpolicy.GetEffectivePolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_effective_policy,
            default_retry=retries.AsyncRetry(
initial=1.0,maximum=10.0,multiplier=1.3,                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_policy(self,
            request: Optional[Union[orgpolicy.CreatePolicyRequest, dict]] = None,
            *,
            parent: Optional[str] = None,
            policy: Optional[orgpolicy.Policy] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> orgpolicy.Policy:
        r"""Creates a policy.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the constraint does not exist.
        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.ALREADY_EXISTS`` if the policy already exists
        on the given Google Cloud resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import orgpolicy_v2

            async def sample_create_policy():
                # Create a client
                client = orgpolicy_v2.OrgPolicyAsyncClient()

                # Initialize request argument(s)
                request = orgpolicy_v2.CreatePolicyRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orgpolicy_v2.types.CreatePolicyRequest, dict]]):
                The request object. The request sent to the [CreatePolicyRequest]
                [google.cloud.orgpolicy.v2.OrgPolicy.CreatePolicy]
                method.
            parent (:class:`str`):
                Required. The Google Cloud resource that will parent the
                new policy. Must be in one of the following forms:

                -  ``projects/{project_number}``
                -  ``projects/{project_id}``
                -  ``folders/{folder_id}``
                -  ``organizations/{organization_id}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            policy (:class:`google.cloud.orgpolicy_v2.types.Policy`):
                Required. Policy to create.
                This corresponds to the ``policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.orgpolicy_v2.types.Policy:
                Defines an organization policy which
                is used to specify constraints for
                configurations of Google Cloud
                resources.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, policy])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = orgpolicy.CreatePolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if policy is not None:
            request.policy = policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_policy,
            default_retry=retries.AsyncRetry(
initial=1.0,maximum=10.0,multiplier=1.3,                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_policy(self,
            request: Optional[Union[orgpolicy.UpdatePolicyRequest, dict]] = None,
            *,
            policy: Optional[orgpolicy.Policy] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> orgpolicy.Policy:
        r"""Updates a policy.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the constraint or the policy do
        not exist. Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.ABORTED`` if the etag supplied in the request
        does not match the persisted etag of the policy

        Note: the supplied policy will perform a full overwrite of all
        fields.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import orgpolicy_v2

            async def sample_update_policy():
                # Create a client
                client = orgpolicy_v2.OrgPolicyAsyncClient()

                # Initialize request argument(s)
                request = orgpolicy_v2.UpdatePolicyRequest(
                )

                # Make the request
                response = await client.update_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orgpolicy_v2.types.UpdatePolicyRequest, dict]]):
                The request object. The request sent to the [UpdatePolicyRequest]
                [google.cloud.orgpolicy.v2.OrgPolicy.UpdatePolicy]
                method.
            policy (:class:`google.cloud.orgpolicy_v2.types.Policy`):
                Required. Policy to update.
                This corresponds to the ``policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.orgpolicy_v2.types.Policy:
                Defines an organization policy which
                is used to specify constraints for
                configurations of Google Cloud
                resources.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([policy])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = orgpolicy.UpdatePolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if policy is not None:
            request.policy = policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_policy,
            default_retry=retries.AsyncRetry(
initial=1.0,maximum=10.0,multiplier=1.3,                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("policy.name", request.policy.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_policy(self,
            request: Optional[Union[orgpolicy.DeletePolicyRequest, dict]] = None,
            *,
            name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> None:
        r"""Deletes a policy.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the constraint or organization
        policy does not exist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import orgpolicy_v2

            async def sample_delete_policy():
                # Create a client
                client = orgpolicy_v2.OrgPolicyAsyncClient()

                # Initialize request argument(s)
                request = orgpolicy_v2.DeletePolicyRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_policy(request=request)

        Args:
            request (Optional[Union[google.cloud.orgpolicy_v2.types.DeletePolicyRequest, dict]]):
                The request object. The request sent to the [DeletePolicy]
                [google.cloud.orgpolicy.v2.OrgPolicy.DeletePolicy]
                method.
            name (:class:`str`):
                Required. Name of the policy to
                delete. See the policy entry for naming
                rules.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = orgpolicy.DeletePolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_policy,
            default_retry=retries.AsyncRetry(
initial=1.0,maximum=10.0,multiplier=1.3,                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def create_custom_constraint(self,
            request: Optional[Union[orgpolicy.CreateCustomConstraintRequest, dict]] = None,
            *,
            parent: Optional[str] = None,
            custom_constraint: Optional[constraint.CustomConstraint] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> constraint.CustomConstraint:
        r"""Creates a custom constraint.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the organization does not
        exist. Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.ALREADY_EXISTS`` if the constraint already
        exists on the given organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import orgpolicy_v2

            async def sample_create_custom_constraint():
                # Create a client
                client = orgpolicy_v2.OrgPolicyAsyncClient()

                # Initialize request argument(s)
                request = orgpolicy_v2.CreateCustomConstraintRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_custom_constraint(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orgpolicy_v2.types.CreateCustomConstraintRequest, dict]]):
                The request object. The request sent to the [CreateCustomConstraintRequest]
                [google.cloud.orgpolicy.v2.OrgPolicy.CreateCustomConstraint]
                method.
            parent (:class:`str`):
                Required. Must be in the following form:

                -  ``organizations/{organization_id}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            custom_constraint (:class:`google.cloud.orgpolicy_v2.types.CustomConstraint`):
                Required. Custom constraint to
                create.

                This corresponds to the ``custom_constraint`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.orgpolicy_v2.types.CustomConstraint:
                A custom constraint defined by customers which can *only* be applied to the
                   given resource types and organization.

                   By creating a custom constraint, customers can apply
                   policies of this custom constraint. *Creating a
                   custom constraint itself does NOT apply any policy
                   enforcement*.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, custom_constraint])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = orgpolicy.CreateCustomConstraintRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if custom_constraint is not None:
            request.custom_constraint = custom_constraint

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_custom_constraint,
            default_retry=retries.AsyncRetry(
initial=1.0,maximum=10.0,multiplier=1.3,                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_custom_constraint(self,
            request: Optional[Union[orgpolicy.UpdateCustomConstraintRequest, dict]] = None,
            *,
            custom_constraint: Optional[constraint.CustomConstraint] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> constraint.CustomConstraint:
        r"""Updates a custom constraint.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the constraint does not exist.

        Note: the supplied policy will perform a full overwrite of all
        fields.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import orgpolicy_v2

            async def sample_update_custom_constraint():
                # Create a client
                client = orgpolicy_v2.OrgPolicyAsyncClient()

                # Initialize request argument(s)
                request = orgpolicy_v2.UpdateCustomConstraintRequest(
                )

                # Make the request
                response = await client.update_custom_constraint(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orgpolicy_v2.types.UpdateCustomConstraintRequest, dict]]):
                The request object. The request sent to the [UpdateCustomConstraintRequest]
                [google.cloud.orgpolicy.v2.OrgPolicy.UpdateCustomConstraint]
                method.
            custom_constraint (:class:`google.cloud.orgpolicy_v2.types.CustomConstraint`):
                Required. ``CustomConstraint`` to update.
                This corresponds to the ``custom_constraint`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.orgpolicy_v2.types.CustomConstraint:
                A custom constraint defined by customers which can *only* be applied to the
                   given resource types and organization.

                   By creating a custom constraint, customers can apply
                   policies of this custom constraint. *Creating a
                   custom constraint itself does NOT apply any policy
                   enforcement*.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([custom_constraint])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = orgpolicy.UpdateCustomConstraintRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if custom_constraint is not None:
            request.custom_constraint = custom_constraint

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_custom_constraint,
            default_retry=retries.AsyncRetry(
initial=1.0,maximum=10.0,multiplier=1.3,                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("custom_constraint.name", request.custom_constraint.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_custom_constraint(self,
            request: Optional[Union[orgpolicy.GetCustomConstraintRequest, dict]] = None,
            *,
            name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> constraint.CustomConstraint:
        r"""Gets a custom constraint.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the custom constraint does not
        exist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import orgpolicy_v2

            async def sample_get_custom_constraint():
                # Create a client
                client = orgpolicy_v2.OrgPolicyAsyncClient()

                # Initialize request argument(s)
                request = orgpolicy_v2.GetCustomConstraintRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_custom_constraint(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.orgpolicy_v2.types.GetCustomConstraintRequest, dict]]):
                The request object. The request sent to the [GetCustomConstraint]
                [google.cloud.orgpolicy.v2.OrgPolicy.GetCustomConstraint]
                method.
            name (:class:`str`):
                Required. Resource name of the custom
                constraint. See the custom constraint
                entry for naming requirements.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.orgpolicy_v2.types.CustomConstraint:
                A custom constraint defined by customers which can *only* be applied to the
                   given resource types and organization.

                   By creating a custom constraint, customers can apply
                   policies of this custom constraint. *Creating a
                   custom constraint itself does NOT apply any policy
                   enforcement*.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = orgpolicy.GetCustomConstraintRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_custom_constraint,
            default_retry=retries.AsyncRetry(
initial=1.0,maximum=10.0,multiplier=1.3,                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_custom_constraints(self,
            request: Optional[Union[orgpolicy.ListCustomConstraintsRequest, dict]] = None,
            *,
            parent: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListCustomConstraintsAsyncPager:
        r"""Retrieves all of the custom constraints that exist on
        a particular organization resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import orgpolicy_v2

            async def sample_list_custom_constraints():
                # Create a client
                client = orgpolicy_v2.OrgPolicyAsyncClient()

                # Initialize request argument(s)
                request = orgpolicy_v2.ListCustomConstraintsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_custom_constraints(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.orgpolicy_v2.types.ListCustomConstraintsRequest, dict]]):
                The request object. The request sent to the [ListCustomConstraints]
                [google.cloud.orgpolicy.v2.OrgPolicy.ListCustomConstraints]
                method.
            parent (:class:`str`):
                Required. The target Google Cloud resource that parents
                the set of custom constraints that will be returned from
                this call. Must be in one of the following forms:

                -  ``organizations/{organization_id}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.orgpolicy_v2.services.org_policy.pagers.ListCustomConstraintsAsyncPager:
                The response returned from the [ListCustomConstraints]
                   [google.cloud.orgpolicy.v2.OrgPolicy.ListCustomConstraints]
                   method. It will be empty if no custom constraints are
                   set on the organization resource.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = orgpolicy.ListCustomConstraintsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_custom_constraints,
            default_retry=retries.AsyncRetry(
initial=1.0,maximum=10.0,multiplier=1.3,                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListCustomConstraintsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_custom_constraint(self,
            request: Optional[Union[orgpolicy.DeleteCustomConstraintRequest, dict]] = None,
            *,
            name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> None:
        r"""Deletes a custom constraint.

        Returns a ``google.rpc.Status`` with
        ``google.rpc.Code.NOT_FOUND`` if the constraint does not exist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import orgpolicy_v2

            async def sample_delete_custom_constraint():
                # Create a client
                client = orgpolicy_v2.OrgPolicyAsyncClient()

                # Initialize request argument(s)
                request = orgpolicy_v2.DeleteCustomConstraintRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_custom_constraint(request=request)

        Args:
            request (Optional[Union[google.cloud.orgpolicy_v2.types.DeleteCustomConstraintRequest, dict]]):
                The request object. The request sent to the [DeleteCustomConstraint]
                [google.cloud.orgpolicy.v2.OrgPolicy.DeleteCustomConstraint]
                method.
            name (:class:`str`):
                Required. Name of the custom
                constraint to delete. See the custom
                constraint entry for naming rules.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = orgpolicy.DeleteCustomConstraintRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_custom_constraint,
            default_retry=retries.AsyncRetry(
initial=1.0,maximum=10.0,multiplier=1.3,                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def __aenter__(self) -> "OrgPolicyAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version=package_version.__version__)


__all__ = (
    "OrgPolicyAsyncClient",
)
