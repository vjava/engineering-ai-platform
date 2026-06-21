
dbutils.notebook.run("/01_generate_sample_data",3600)
dbutils.notebook.run("/02_github_ingestion",3600)
dbutils.notebook.run("/03_jira_ingestion",3600)
