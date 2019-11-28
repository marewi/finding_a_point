# finding a point in a grid layout


### build image
docker build --rm -f Dockerfile -t finding-a-point .

### run container
docker run --rm -it -p 0.0.0.0:6006:6006 finding-a-point

### run script
python main.py -s window/triangle/hook

### TODOs
- [x] dynamic start
    - [x] solving substraction problem
- [ ] train policy for each group of points (e.g. for each logo)
    - [ ] find optimal sequence of pictures for training model (maybe new epsilon for each picture)
- [ ] train model with neural network
- [ ] testing other algorithms instead of q-learning