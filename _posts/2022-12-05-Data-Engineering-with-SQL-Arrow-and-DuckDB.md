---
title: "Tip of the Week: Data Engineering with SQL, Arrow and DuckDB"
author: dave-bunten
tags:
  - tip-of-the-week
  - software
  - data
  - sql
  - dataframes
  - arrow
  - duckdb
---

# Tip of the Week: Data Engineering with SQL, Arrow and DuckDB

{% include tip-of-the-week-intro.html %}

<!-- excerpt start -->

[Apache Arrow](https://arrow.apache.org/) is a language-independent and high performance data format useful in many scenarios. [DuckDB](https://duckdb.org/) is an in-process [SQL](https://en.wikipedia.org/wiki/SQL)-based data management system which is Arrow-compatible. In addition to providing a [SQLite](https://sqlite.org/index.html)-like database format, DuckDB also provides a standardized and high performance way to work with Arrow data where otherwise one may be forced to language-specific data structures or transforms.

<!-- excerpt end -->

__TLDR (too long, didn't read);__
DuckDB may be used to access and transform Arrow-based data from multiple data formats through SQL. Using Arrow and DuckDB provides a cross-language way to access and manage data. Data development with these tools may also enable improvements in performance, understandability, or long term maintainability of your code.

## Reduce Wasted Conversion Effort with Arrow

<pre class="mermaid">
flowchart TB
    Python:::outlined <--> Arrow
    R:::outlined <--> Arrow
    C++:::outlined <--> Arrow
    Java:::outlined <--> Arrow
    others...:::outlined <--> Arrow

    classDef outlined fill:#fff,stroke:#333
</pre>
<script type="module">
  import mermaid from 'https://unpkg.com/mermaid@9/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

Arrow provides a [multi-language](https://arrow.apache.org/docs/) data format which prevents you from needing to convert to other formats when dealing with multiple in-memory or serialized data formats. For example, this means that a Python and an R package may use the same in-memory or file-based data without conversion (where normally a Python Pandas dataframe and R data frame may require a conversion step in between).

<pre class="mermaid">
flowchart TB
    subgraph Python
      Pandas:::outlined
      Polars:::outlined
      dict[Python dict]:::outlined
      list[Python list]:::outlined
    end

    Pandas <--> Arrow
    Polars <--> Arrow
    dict <--> Arrow
    list <--> Arrow

  classDef outlined fill:#fff,stroke:#333
</pre>

The same stands for various libraries within one language - Arrow enables interchange between various language library formats (for example, a Python Pandas dataframe and Python dictionary are two distinct in-memory formats which may require conversions). Conversions to or from these formats can involve data type or other inferences which are costly to productivity. You can save time and effort by avoiding conversions using Arrow.

## Using SQL to Join or Transform Arrow Data via DuckDB

<pre class="mermaid">
flowchart LR
    subgraph duckdb["DuckDB Processing"]
        direction BT
        SQL[SQL] --> DuckDB[DuckDB Client]
    end
    parquet1[example.parquet] --> duckdb
    sqlite[example.sqlite] --> duckdb
    csv[example.csv] --> duckdb
    arrow["in-memory Arrow"] --> duckdb
    pandas["in-memory Pandas"] --> duckdb
    duckdb --> Arrow
    Arrow --> Other[Other work...]
</pre>

DuckDB provides a management client and relational database format (similar to SQLite databases) which may be handled with Arrow. SQL may be used with the DuckDB client to filter, join, or change various data types. Due to Arrow's cross-language properties, there is no additional cost to using SQL through DuckDB to return data for implementation within other purpose-built data formats. [DuckDB provides client API's in many languages](https://duckdb.org/docs/api/overview) (for example, Python, R, and C++), making it possible to write DuckDB client code with SQL to manage data without having to use manually written sub-procedures.

<pre class="mermaid">
flowchart TB
  subgraph duckdb["DuckDB Processing"]
        direction BT
        SQL[SQL] --> DuckDB[DuckDB Client]
    end
    Python:::outlined <--> duckdb
    R:::outlined <--> duckdb
    C++:::outlined <--> duckdb
    Java:::outlined <--> duckdb
    others...:::outlined <--> duckdb
    duckdb <--> Arrow

    classDef outlined fill:#fff,stroke:#333
</pre>

Using SQL to perform these operations with Arrow provides an opportunity for your data code to be used (or understood) within other languages without additional rewrites. SQL also provides you access to roughly 48 years worth of data management improvements without being constrained by imperative language data models or schema (reference: [SQL Wikipedia: _First appeared: 1974_](https://en.wikipedia.org/wiki/SQL)).

## Example with SQL to Join Arrow Data with DuckDB in Python

{% include figure.html image="images/duckdb_arrow_query_example.png" caption="Jupyter notebook example screenshot with DuckDB and Arrow data handling" width="500px" %}

The following example notebook shows how to use SQL to join data from multiple sources using the DuckDB client API within Python. The example includes DuckDB querying a remote CSV, local Parquet file, and Arrow in-memory tables.

[Linked Example](https://github.com/CU-DBMI/notebooks/blob/main/content/arrow_and_duckdb_example.ipynb)

## Additional Resources

Please see the following the additional resources.

- [Apache Arrow Documentation](https://arrow.apache.org/docs/index.html)
- [DuckDB Documentation](https://duckdb.org/docs/)
