# SLAM Final Project
### 40875040H KUAN-HSUN WANG
## 1. Purpose of The Final Project
Implement the UKF algorithm for both localization and mapping by simulation (In 2D and construct the map in form of an occupancy Grid map)
## 2. My Idea
I just make a model by using UKF localiztion, using the resources in the class to mapping, constructing the map.
## 3. Code Explanation
### 【First part】File reading  
I use a csv file to construct my boundaries(map), and I build a fence that can contain the whole thing.
```python
def file_read(f):
```
we read in the run_localization function below, and data will convert to angle and distance in order to calculate.
```python
ang, dist = file_read("map.csv")
```
### 【Second part】 As defined below, these function are used to deal with some problems, like model, trasition, angle and math problems.  
We model our system as a nonlinear motion model,which is made by simple bicycle model. With using this function, we can implement the state transition function. 
```python
1.  def move(x, dt, u, wheelbase):
```
We force the radius not to over 6.28. After, we optimize that if radius is for example: 4.14 radius,  we'll let it become -2.00 radius. That is to say move to [-pi, pi).  
This is to correctly compute the bearing residual.
```python
2.  def normalize_angle(x):
```
Because our state vector has two indexes, we need to have two functions to deal with each.
```python
3.  def residual_h(a, b):
    def residual_x(a, b):
```
To implement the measurement model and pass an array of landmarks. The function for the residual in the measurement will be passed an array of several measurements, one per landmark.
```python
4.  def Hx(x, landmarks):
```
Finally,there are a common problem. How do we calculate the average of 359 degree and 3 degree? Is it 181 degree? No! So we have to handle this!   
```python
5.  def state_mean(sigmas, Wm):
    def z_mean(sigmas, Wm):
```
### 【Third part】Implement the UKF  
We construct the sigma points and filter, and we use above functions to predict and update UKF. In addtion, we exhibit the map in the meanwhile.
```python
def run_localization
```
### 【Final part】
Final part is turn left or turn right, in order to  generate varying steering commands
```python
def turn(v, t0, t1, steps):
```
We can control how much curve, how long every step and turn left or turn right.  
For example :
```python
#turn right
cmds.extend(turn(v, -1, -5, 25))
cmds.extend([cmds[-1]]*80)
# turn left
cmds.extend(turn(v, 3, 6.5, 15))
cmds.extend([cmds[-1]]*80)
```
In the end, we define the location of landmarks, time interval, the set up of some parameters, and we call the run_loaclization function.
## 4. Result
This is my result for this project. If run this code, it will be an animation. The red points are our boundaries. The blue squares are landmarks. You can observe The uncertainty increase a little, because there is no landmark in the end. If I add some landmarks, the error will become smaller!!
![avatar](result.png)  

You can see if I decrease landmarks, the uncertainly is bigger!!  

![avatar](result2.png)