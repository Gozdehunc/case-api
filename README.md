# Case Study

This case study is building an api using flask and python and it was written using VSCode.


## Docker Build

Steps to create an image& how to run the app in a container list below.


Create a docker image :```bash
			docker image build -t case-api .
			```

## Docker Run

Run docker container :```bash
			docker run -p 5000:5000 -d case-api
			```
