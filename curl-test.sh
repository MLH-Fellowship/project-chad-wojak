#!/usr/bin/bash
curl --request POST http://localhost:5000/api/timeline_post -d 'name=Carrie&email=carriekam@protonmail.com&content=Just added database to my portfolio!'

curl http://localhost:5000/api/timeline_post
