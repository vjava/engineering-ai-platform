
github_df=spark.table("bronze_applications")
github_df.write.mode("overwrite").saveAsTable("bronze_github")
