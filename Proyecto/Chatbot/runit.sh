docker build -t chatbot .
 docker run --rm -it --name chatbot -p 5000:5000 -v ${PWD}:/usr/src/app  chatbot bash