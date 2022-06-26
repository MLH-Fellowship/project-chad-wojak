#! /bin/bash
curl -s --request POST http://localhost:5000/api/timeline_post -d 'name=Ailun&email=ailun@nonOfYourBusiness.com&content=Testing my endpoints with curl'
if [ $? -eq 0 ]
then
	echo POST endpoint works
else
	echo POST endpoint error
fi
curl -s --request GET http://localhost:5000/api/timeline_post
if [ $? -eq 0 ]
then
	echo GET endpoint works
else
	echo GET endpoint error
fi
curl -s --request DELETE http://localhost:5000/api/timeline_post
