# webScrapping

This is a simple web scrapping script which get information from different job position from Indeed with Beautiful Soup. 

Steps to implement web scrapping: 
1. We need to use `requests` lib to request for the URL, 
  * When we analyize the URL link, where `q=job_title` and `l=location`, by knowing this two feature,we are able to do the search
2. We can parse our result into an HTML parse with the help of Beautiful Soup 
3. We can use `find` or `find_all` function to find the tag or information we need 
4. Lastly, we can save the information into a CSV file 


 
