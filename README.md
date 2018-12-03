## DAG Driven Auto Migrations

Let a DAG drive your migrations instead of orchestrating them manually or through a CI/CD system. Why?
DAGs are often running in 'production', removing the need to setup custom hooks into production
environments. DAGs can build their own dependencies - if you have a post migration task why not
schedule it as a downstream dependency of your migration DAG?
