# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
# Generated code. DO NOT EDIT!
#
# Snippet for CreateBackup
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dataproc-metastore


# [START metastore_v1beta_generated_DataprocMetastore_CreateBackup_async]
from google.cloud import metastore_v1beta


async def sample_create_backup():
    # Create a client
    client = metastore_v1beta.DataprocMetastoreAsyncClient()

    # Initialize request argument(s)
    request = metastore_v1beta.CreateBackupRequest(
        parent="parent_value",
        backup_id="backup_id_value",
    )

    # Make the request
    operation = client.create_backup(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)

# [END metastore_v1beta_generated_DataprocMetastore_CreateBackup_async]