# Description of Steps
## Data ingestion - gathering data and loading into a queryable format
1. Created EC2 instance on AWS.
2. Logged into to this EC2 instance and installed all the necessary python libraries.
3. A python script (using Boto3) is written to the download data from the SQS queue to the EC2 instance. See [link](https://github.com/gkrampah/inter_project/blob/main/download_script.py)
4. The data was further downloaded to my local computer for offline analysis and visualiation. See [link](https://nbviewer.org/github/gkrampah/inter_project/blob/main/DataAnalysis.ipynb) 
5. I created a continuous integration pipeline using github action using some dummy scripts for testing (this is just to demonstrate how the CI work in practice). This reposition has all the information needed to reproduce the analysis

### Data type
The data is a json formatted data with dictionary. In the jupyter notebook, I showed the observation metadata and values. The data was issued by a government instition with a stationary detector in Belgium

### Map visualization of measurement
Using matplotlib and folium, I made plots of daily variation of NO$_2$ in West-Vlaanderen and displayed this on the map. 

![dataM_fig](https://user-images.githubusercontent.com/65491585/234057617-9dd8c013-ac0a-468f-b398-ca0b2b98650e.png)

It can be view properly using the [link](https://nbviewer.org/github/gkrampah/inter_project/blob/main/DataAnalysis.ipynb) 

### Creating and writing data to MySql database
Scrren shot of the data in the database

![dataMinded_img](https://user-images.githubusercontent.com/65491585/235886531-6962dc33-142b-42a5-a150-43ba6bf33ec2.png)



### Dashboard made with Dash and Plotly to visualize data from MySql database

![dash_img](https://user-images.githubusercontent.com/65491585/235962331-01b492fd-e3a1-420e-b778-f98eac4576f0.png)

# Further steps:
* Automate the process of data ingestion using a batch-based method on the cloud platform and populate the database - naively use cronjob
* create a better dashboard to query the database 

