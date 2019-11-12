# finding a point in a grid layout


### build
docker build --rm -f Dockerfile -t finding-a-point .

### run
docker run --rm -it -p 0.0.0.0:6006:6006 finding-a-point


### TODOs
- dynamic start
- train policy for each group of points (e.g. for each logo)
- testing other algorithms instead of q-learning


environment implementaion inspired by 
https://pythonprogramming.net/own-environment-q-learning-reinforcement-learning-python-tutorial/


