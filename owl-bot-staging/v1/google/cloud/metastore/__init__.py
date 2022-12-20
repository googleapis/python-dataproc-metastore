# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from google.cloud.metastore import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.metastore_v1.services.dataproc_metastore.client import DataprocMetastoreClient
from google.cloud.metastore_v1.services.dataproc_metastore.async_client import DataprocMetastoreAsyncClient
from google.cloud.metastore_v1.services.dataproc_metastore_federation.client import DataprocMetastoreFederationClient
from google.cloud.metastore_v1.services.dataproc_metastore_federation.async_client import DataprocMetastoreFederationAsyncClient

from google.cloud.metastore_v1.types.metastore import Backup
from google.cloud.metastore_v1.types.metastore import CreateBackupRequest
from google.cloud.metastore_v1.types.metastore import CreateMetadataImportRequest
from google.cloud.metastore_v1.types.metastore import CreateServiceRequest
from google.cloud.metastore_v1.types.metastore import DatabaseDumpSpec
from google.cloud.metastore_v1.types.metastore import DeleteBackupRequest
from google.cloud.metastore_v1.types.metastore import DeleteServiceRequest
from google.cloud.metastore_v1.types.metastore import EncryptionConfig
from google.cloud.metastore_v1.types.metastore import ExportMetadataRequest
from google.cloud.metastore_v1.types.metastore import GetBackupRequest
from google.cloud.metastore_v1.types.metastore import GetMetadataImportRequest
from google.cloud.metastore_v1.types.metastore import GetServiceRequest
from google.cloud.metastore_v1.types.metastore import HiveMetastoreConfig
from google.cloud.metastore_v1.types.metastore import KerberosConfig
from google.cloud.metastore_v1.types.metastore import ListBackupsRequest
from google.cloud.metastore_v1.types.metastore import ListBackupsResponse
from google.cloud.metastore_v1.types.metastore import ListMetadataImportsRequest
from google.cloud.metastore_v1.types.metastore import ListMetadataImportsResponse
from google.cloud.metastore_v1.types.metastore import ListServicesRequest
from google.cloud.metastore_v1.types.metastore import ListServicesResponse
from google.cloud.metastore_v1.types.metastore import LocationMetadata
from google.cloud.metastore_v1.types.metastore import MaintenanceWindow
from google.cloud.metastore_v1.types.metastore import MetadataExport
from google.cloud.metastore_v1.types.metastore import MetadataImport
from google.cloud.metastore_v1.types.metastore import MetadataManagementActivity
from google.cloud.metastore_v1.types.metastore import NetworkConfig
from google.cloud.metastore_v1.types.metastore import OperationMetadata
from google.cloud.metastore_v1.types.metastore import Restore
from google.cloud.metastore_v1.types.metastore import RestoreServiceRequest
from google.cloud.metastore_v1.types.metastore import Secret
from google.cloud.metastore_v1.types.metastore import Service
from google.cloud.metastore_v1.types.metastore import TelemetryConfig
from google.cloud.metastore_v1.types.metastore import UpdateMetadataImportRequest
from google.cloud.metastore_v1.types.metastore import UpdateServiceRequest
from google.cloud.metastore_v1.types.metastore_federation import BackendMetastore
from google.cloud.metastore_v1.types.metastore_federation import CreateFederationRequest
from google.cloud.metastore_v1.types.metastore_federation import DeleteFederationRequest
from google.cloud.metastore_v1.types.metastore_federation import Federation
from google.cloud.metastore_v1.types.metastore_federation import GetFederationRequest
from google.cloud.metastore_v1.types.metastore_federation import ListFederationsRequest
from google.cloud.metastore_v1.types.metastore_federation import ListFederationsResponse
from google.cloud.metastore_v1.types.metastore_federation import UpdateFederationRequest

__all__ = ('DataprocMetastoreClient',
    'DataprocMetastoreAsyncClient',
    'DataprocMetastoreFederationClient',
    'DataprocMetastoreFederationAsyncClient',
    'Backup',
    'CreateBackupRequest',
    'CreateMetadataImportRequest',
    'CreateServiceRequest',
    'DatabaseDumpSpec',
    'DeleteBackupRequest',
    'DeleteServiceRequest',
    'EncryptionConfig',
    'ExportMetadataRequest',
    'GetBackupRequest',
    'GetMetadataImportRequest',
    'GetServiceRequest',
    'HiveMetastoreConfig',
    'KerberosConfig',
    'ListBackupsRequest',
    'ListBackupsResponse',
    'ListMetadataImportsRequest',
    'ListMetadataImportsResponse',
    'ListServicesRequest',
    'ListServicesResponse',
    'LocationMetadata',
    'MaintenanceWindow',
    'MetadataExport',
    'MetadataImport',
    'MetadataManagementActivity',
    'NetworkConfig',
    'OperationMetadata',
    'Restore',
    'RestoreServiceRequest',
    'Secret',
    'Service',
    'TelemetryConfig',
    'UpdateMetadataImportRequest',
    'UpdateServiceRequest',
    'BackendMetastore',
    'CreateFederationRequest',
    'DeleteFederationRequest',
    'Federation',
    'GetFederationRequest',
    'ListFederationsRequest',
    'ListFederationsResponse',
    'UpdateFederationRequest',
)