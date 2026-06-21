
jira_df=spark.table("bronze_applications")
jira_df.write.mode("overwrite").saveAsTable("bronze_jira")
