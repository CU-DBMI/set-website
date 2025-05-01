---
title: "Understanding Object Storage: A Guide for Research Software Development"
author: dave-bunten
tags:
  - data-management
  - object-storage
  - reproducibility
  - scientific-software
---

# Understanding Object Storage: A Guide for Research Software Development

{% include blog-post-intro.html %}

## Introduction

{% include figure.html image="images/object-storage-cloud.png" width="40%" caption="Object storage enables flexible, scalable, and metadata-rich access to research data in modern computing ecosystems." %}

<!-- excerpt start -->
**Managing large-scale scientific data is a defining challenge of modern research.**
With datasets regularly exceeding gigabytes—or even terabytes—in size, researchers require scalable, cost-effective, and reliable storage infrastructure.

**Object storage offers a flexible alternative to traditional filesystems.**
It supports high-throughput access, structured metadata, and distributed scaling, making it a foundational tool in research computing, reproducible science, and FAIR data practices.

In this article, we’ll trace the evolution of object storage (also sometimes referred to as "S3", "storage buckets", or "object stores"), explain its design principles, survey current platforms, and walk through a hands-on example using the open-source [MinIO](https://min.io/) tool.
<!-- excerpt end -->

## A brief history of object storage

Traditional storage systems relied on block storage (used by hard drives) and file storage (used by operating systems).
While effective for early computing, these models struggled to scale with the demands of scientific data and cloud-native applications.

Object storage originated in the research community to address these challenges.
In the late 1990s, the NASD project at Carnegie Mellon and HP Labs introduced the idea of storing data as self-contained objects with rich metadata—decoupling data access from file hierarchies ([Gibson et al., 1998](https://dl.acm.org/doi/10.1145/384265.291029)).

In the early 2000s, the open-source Ceph project (from UCSC) introduced the now-famous CRUSH algorithm to distribute data without centralized metadata bottlenecks ([Weil et al., 2006](https://dl.acm.org/doi/10.5555/1298455.1298485)).

Amazon S3 brought these ideas to a global audience in 2006, offering a scalable, HTTP-accessible object store with an API-driven model that became a standard for cloud and scientific applications ([Amazon S3 launch blog post](https://aws.amazon.com/blogs/aws/amazon_s3/)).

Unlike file systems, object stores provide:

- A flat namespace with key-based access
- Rich, customizable metadata
- Scalable, distributed architecture

These qualities make object storage essential for managing large, unstructured, and reproducible scientific datasets.

## Why use object storage for research?

Object storage is not just a buzzword.
It enables capabilities increasingly vital to modern research:

- **Scalability**: Stores billions of files with virtually no performance degradation.
- **Flexibility**: Ideal for unstructured data (images, JSON, audio, NetCDF, Parquet, etc.).
- **Metadata-rich**: Stores metadata alongside objects, useful for provenance, reproducibility, and FAIR data principles ([Wilkinson et al., 2016](https://doi.org/10.1038/sdata.2016.18)).
- **Cloud-native**: Compatible with public cloud platforms and on-premises deployments.
- **HTTP-accessible**: Allows sharing, versioning, and integration with APIs and remote workflows.

Traditionally seen as a passive place to "put files," object storage is often now being used as a primary data substrate—functioning more like a database than just a dumping ground.
This shift aligns closely with principles from the Composable Data Management System Manifesto ([Pedreira et. al, 2023](https://dl.acm.org/doi/10.14778/3603581.3603604)), which advocates for modular, interoperable, and storage-agnostic data infrastructure.

Generally, consider use cases like:

- Long-term archiving of large-scale microscopy datasets.
- Sharing reproducible analysis results using structured metadata.
- Automating pipelines that read and write from shared storage

In research, where **data integrity, sharing, and sustainability** are paramount, object storage provides a modern backbone.

## Common platforms and ecosystem

Below are some popular object storage platforms used in research and industry:

| Platform         | Description                                  | Type         |
|------------------|----------------------------------------------|--------------|
| **Amazon S3**    | The original commercial object store.        | Commercial   |
| **Google Cloud Storage** | Integrated with Google Cloud ecosystem.   | Commercial   |
| **Azure Blob Storage** | Microsoft’s cloud object store.             | Commercial   |
| **MinIO**        | High-performance, S3-compatible OSS.         | Open Source  |
| **Ceph**         | Distributed object (and block/file) system. | Open Source  |
| **Wasabi**       | Cost-effective S3-compatible storage.       | Commercial   |
| **OpenStack Swift** | Open-source cloud platform component.       | Open Source  |

In academic environments, **MinIO** and **Ceph** are frequently used for institutional deployments that must remain on-premises or comply with specific data governance needs.

## How object storage works

{% include figure.html image="images/object-storage-architecture.png" width="60%" caption="An object store maps keys to data and metadata using a flat namespace, ideal for scalable distributed systems." %}

Here are the core principles of object storage:

- **Flat Namespace**: No folder hierarchies; everything is accessed via a unique object key (similar to a URL path).
- **Objects**: Each unit of data includes the content, metadata, and a unique identifier (key).
- **Buckets**: Logical containers for grouping objects (like folders, but flat).
- **APIs**: Most object stores use HTTP REST APIs, often based on the [Amazon S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html).
- **Versioning and Lifecycle**: Objects can be versioned and automatically expired or archived.
- **Event Notification**: Some systems emit events (e.g., via webhooks or queues) when new data is written—ideal for automation pipelines.

## Demo: Using MinIO for scientific data

Let’s walk through how to use [MinIO](https://min.io) to create and interact with object storage on your local system.
MinIO is lightweight, open source, and provides an S3-compatible interface, making it perfect for development and reproducible demos.

### Step 1: Install MinIO

You can install MinIO locally via Docker:

```bash
docker run -p 9000:9000 -p 9001:9001 \
  -e "MINIO_ROOT_USER=minioadmin" \
  -e "MINIO_ROOT_PASSWORD=minioadmin" \
  quay.io/minio/minio server /data --console-address ":9001"
```

Access the web UI at [http://localhost:9001](http://localhost:9001) using the above credentials.

### Step 2: Upload a file

You can interact with MinIO using the official [`mc`](https://min.io/docs/minio/linux/reference/minio-mc.html) client:

```bash
# install client
brew install minio/stable/mc  # or use curl/wget for Linux

# configure client
mc alias set local http://localhost:9000 minioadmin minioadmin

# create a bucket
mc mb local/research-data

# create a file
echo "1,2,3" > dataset.csv

# upload a file
mc cp dataset.csv local/research-data
```

### Step 3: Access via Python

You can also use the official MinIO Python client to interact with your object storage server:

```bash
pip install minio
```

Then, use the client to connect and list objects:

```python
from minio import Minio

# Initialize client
client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False  # Use True if running over HTTPS
)

# List objects in a bucket
for obj in client.list_objects("research-data"):
    print(obj.object_name)
```

This approach is lightweight, straightforward, and ideal for working directly with MinIO in local or institutional deployments.

## Wait, what about `boto`?

You might have encountered `boto` or `boto3` in other tutorials—these are **AWS SDKs for Python** that support interaction with **Amazon S3** and any object storage system that speaks the **S3 API**, including MinIO.

- [`boto`](https://github.com/boto/boto) is the original (now deprecated) SDK.
- [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) is the modern version used for AWS and S3-compatible storage.

These libraries are powerful and widely used, but they're **heavily tied to the AWS ecosystem**, which can introduce complexity or unintended coupling—especially in research environments where:

- S3 credentials and IAM policies don't apply,
- The goal is on-premises, reproducible, or containerized setups,
- Simplicity and transparency are preferred.

### When to use `boto3`:
- You're already integrating with AWS services (e.g., EC2, SageMaker, CloudWatch).
- You need access to AWS-specific features like presigned URLs, access control policies, or Glacier storage classes.
- You're developing cloud-native tools for deployment in AWS environments.

### When to use the `minio` client:
- You're working with **MinIO**, **Ceph**, or other S3-compatible but non-AWS storage.
- You want a **lightweight, dependency-free, Pythonic API**.
- You're focused on **local development, reproducible science, or hybrid infrastructure**.

Both libraries work with MinIO, but for most research workflows where AWS integration isn't required, the official [`minio`](https://min.io/docs/minio/linux/developers/python/minio-py.html) client is easier to use and avoids unnecessary complexity.

## Best practices in scientific object storage

To maximize reproducibility and data stewardship, consider the following:

- **Use consistent naming schemes** for buckets and object keys.
- **Store rich metadata** (JSON sidecars, standardized formats) alongside data.
- **Enable versioning** for mutable datasets to preserve provenance.
- **Integrate storage into workflow systems** (e.g., [Nextflow](https://www.nextflow.io/), [Dagster](https://dagster.io/), or [Galaxy](https://galaxyproject.org/)).
- **Ensure data durability and backup** in institutional deployments.
- **Align with FAIR principles** ([GO FAIR Initiative](https://www.go-fair.org/fair-principles/)) whenever possible.

## S3-Compatible Object Storage Solutions for Research Infrastructure

Many research institutions and HPC centers rely on object storage platforms that support the **S3 API** without depending on commercial cloud providers like AWS, Google Cloud, or Azure. Below are commonly used alternatives that work well with tools like the MinIO Python SDK or `mc` CLI:

| Storage System         | Type         | S3 Compatibility | Notes |
|------------------------|--------------|------------------|-------|
| **Dell PowerScale (Isilon)** | Enterprise NAS + Object | ✅ via S3 Gateway | Offers S3 compatibility alongside traditional file/NFS access. Widely used in biomedical and university HPC clusters. |
| **MinIO**              | Open Source  | ✅ Native S3 API  | Lightweight, high-performance; ideal for development, on-prem, or hybrid deployments. |
| **Ceph (RGW)**         | Open Source  | ✅ via RADOS Gateway | Highly scalable, distributed storage system with robust community support. |
| **NetApp StorageGRID** | Enterprise   | ✅               | Designed for petabyte-scale deployments, lifecycle automation, and hybrid environments. |
| **OpenIO**             | Open Source  | ✅               | Modular, scale-out object storage for edge and HPC use cases. |
| **Scality RING**       | Enterprise   | ✅               | Proven in telecom and research data centers, designed for massive scale. |
| **Cloudian HyperStore**| Enterprise   | ✅               | S3-compatible storage designed to run on-premises with cloud-tiering options. |

### Why these matter in scientific contexts

- ✅ **S3 API support** means compatibility with existing tools and workflows.
- ✅ **On-premises deployment** supports data sovereignty, compliance (e.g., HIPAA, GDPR), and high-speed access.
- ✅ **Open-source and hybrid options** allow more transparent, vendor-neutral infrastructure planning.
- ✅ **High metadata throughput** and horizontal scalability make these systems well-suited for large scientific imaging, genomics, and simulation outputs.

Researchers can use tools like the [MinIO Python client](https://min.io/docs/minio/linux/developers/python/minio-py.html) to build portable data pipelines regardless of which backend serves the object data.

## Conclusion

Object storage is a foundational technology for modern research computing. It allows research teams to scale data access, enable metadata-rich reproducibility, and bridge the gap between local experimentation and cloud workflows.

By learning how to use tools like MinIO and understanding the object storage model, research software developers can design more robust, future-proof, and FAIR-aligned systems for handling scientific data.

> _“Data is a precious thing and will last longer than the systems themselves.” - Tim Berners-Lee_

## Further Reading

- Wilkinson, M. D., et al. (2016). [The FAIR Guiding Principles for scientific data management and stewardship](https://doi.org/10.1038/sdata.2016.18). Scientific Data.
- MinIO Documentation: [https://min.io/docs](https://min.io/docs)
- AWS S3 API Reference: [https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html)
- GO FAIR Initiative: [https://www.go-fair.org/](https://www.go-fair.org/)
