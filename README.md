# finding a point in a grid layout


### build image
docker build --rm -f Dockerfile -t finding-a-point .

### run container
docker run --rm -it -p 0.0.0.0:6006:6006 finding-a-point

### clone repo in container
git checkout <branch-name>
git pull

### run script
python main.py -s window/triangle/hook

### TODOs
- [x] dynamic start
    - [x] solving substraction problem
- [x] train policy for each group of points (e.g. for each logo)
    - [?] find optimal sequence of pictures for training model (maybe new epsilon for each picture)
- [ ] change measurement to accumulated reward & reward per episode
    - [ ] print func for parameters
- [ ] concept to show learning results (strategy)
- [ ] train model with neural network
- [ ] testing other algorithms instead of q-learning
- [ ] any parallelism possible?