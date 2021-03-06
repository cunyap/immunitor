[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/cunyap/codevscovid19_app/blob/master/LICENSE)



![](app/static/img/immonitor-ch-bright.png) 

# Immunitor



The COVID19 crisis is posing an unprecedented challenge to the healthcare system as well as society. While great effort is being put in increasing the testing capacity, systematically collecting data regarding the outcome is still challenging. This will be especially impelling as soon as home testing becomes a viable option. While there are currently many self-report tools, data validation is still a critical, un-met, need.
We plan to collaborate with the test-kit manufacturers to gather the kits serial numbers and thus validate entries of tests performed also in the clinics.
Using kits serial numbers will allow combining entries from different cantons, manufacturers and healthcare providers.
During the CodeVsCOVID19 Hackathon, we prototyped a platform where patients who got tested can submit the result. The platform allows the user to fully control how much additional information they want to provide (e.g. gender, age, location, profession etc.). The collected data will be anonymous and stored to an openBIS database, to be accessible to anyone interested. The platform is currently designed to support single entries from the patients but has the potential to accept bulk entries from hospitals or laboratories, those entries would then be cross-validated, using the test serial number, to avoid duplicates.
Moreover, we plan to allow users to submit subsequent entries by generating a code that the users can store if desired. This would be of great value to track the evolution of a single case and avoid overcounting while maintaining anonymity.
This platform has the potential to be a powerful tool for researchers to obtain and previewing data concerning the Covid19 crisis. While it guarantees a completely anonymized submission from the user, it also allows subsetting for validated data, or additional tags (e.g. gender, age etc.).



[![IMAGE ALT TEXT](http://img.youtube.com/vi/PbIC1CnMSFY/0.jpg)](http://www.youtube.com/watch?v=PbIC1CnMSFY "Immunitor")



## Immunitor could be useful for:

- __citizens__ to visualize data concerning the pandemic

- __researchers__ for having a fast, reliable and safe platform to aggregate validated data in an anonymized form. Additionally, an automated data analysis pipeline can be setup to display information in real time.

- __authorities__ and __organisations__ to track the development of the crisis and the increasing number of people becoming immune in real time

- __media__ for having a central source of data which can be retrieved automatically.

  



### Design proposal for COVID19 POC test manafacturer

We want to _facilitate an automated readout_ of upcoming SARS COVID19 Point Of Care Tests (POCT). Therefore we propose to encode details of the test kit in a machine readable format (i.e datamatrix)  as well as highlighting the read out zone with colored frame and Quick Response (QR) codes to better detects its location once a picture is taken from the test.

The main advantages would be:

* __Low additional costs__ for the test while changing the package printings slightly as brand names and similar anyway gets printed onto the package.
* __Everyone__ with a smartphone can take a picture of the test and __quantify the result automatically__ using our website or with an app.
* Tests used in research i.e for broad studies can be batch quantified quickly without any sophisitcated and expensive device or equipment
* __Results are directly available in digital format__ and can be combined with results from other tests.

![POC test proposal](app/static/img/POCT_Package_Porposal.jpg)





## Technical requirements

* Server i.e. a VServer or VM running CentOS, docker with openBIS and miniconda.



# We would like to thank:

- the CodeVsCovid19 organization people for the opportunity. 

- Vincenco Spanò for the technical support with the VM.

- Swen Vermeul and Grehard Bräunlich for helping out with docker.

- Nicolas Uffer for providing example datasets.

- Mr. Robert Scott and Prof. Dr. Sebastian Bonhoeffer for critical revision of the idea.

  

# Main contributors:
Bieberich Florian, Cuny Andreas P., Garulli Elisa L.