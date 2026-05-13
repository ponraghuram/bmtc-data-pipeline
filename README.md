# bmtc-data-pipeline
Creating this repo for project practice on live/ batch data set

Problem statement : Tracking the bmtc bus for delayed in the same route to identify where the traffic is heavy and notify the user that the bus is delay beyond thresold limit
Tech Stack : storage : Github, azure Gen 2
            : Transformation and processing : Databricks
              Visualisation : Power BI or Databricks Dashboard

Folder Structure : Raw Data : bronze , One big Data combined : silver layer , Busineess Ready data : Gold

Raw csv --> bronze(delta) --> silver (cleaned) --> gold (aggregated)