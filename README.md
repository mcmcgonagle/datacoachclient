# datacoachclient
Python scripts for API Gateway - > Lambda -> S3


1. Log into AWS Management Console.
2. From the Services menu, select AWS Lambda.
3. Click Create Function -> Author from Scratch. Type a name for the function. Select Python 3.8 for the Runtime. 
4. Click Create Function.
5. From the Services menu, select API Gateway. 
6. Click Create API.
7. Under REST API click Build. 
8. Name the API and click Create API. 
9. From the Actions menu, click Create Resource and name it response.
10. Select the response Resource. From the Actions menu, click Create Method. 
11. Select GET. 
12. For Integration type select Lambda Function then select your Lambda function from the dropdown menu in step 3-4.
13. Click Method Request and then click URL Query String Parameters.
14. Click Add query string. 
15. For name, type "company_id" (no quotes). Select Requried.
16. Repeat Step 14 for the "person_id" and "rating" (no quotes for both).
17. Go back to the GET - Method Execution area and select Integration Request.
18. Go to Maaping Templates and select "When there are no templates defined (recommended)".
19. For Content-Type, type "application/json".
20. For the mapping template, type this in: 

{
     "company_id": "$input.params('company_id')",
     "person_id": "$input.params('person_id')",
     "rating": "$input.params('rating')"
}

21. From the Services menu, select S3.
22. Click Create bucket.
23. Name the bucket and click Create bucket.
24. Select the bucket you just created and then click Upload. Upload the file name onefile.csv.
25. From the Services menu, select Lambda. 
26. Open up the Lambda function you created. 
27. In the Function code section, paste in the contents of the onefilecsv.py. Some of the information in this file might need to be customized. 
