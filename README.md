# Road-condition-detection
😀👏 Detect pedestrians, cars, trucks, bicycles and other vehicles on the road where the vehicle is traveling, and issue an alarm

检测感受野中的行人，轿车，自行车及障碍物，并进行播报与类别打印。（已封装好，直接使用即可）
# EN
## Use the code
### Use the trained model
- Download the project
- Use the camera: `python .\detect.py --source 0`
- Detect the fixed images or video: Change the path in detect.py and "run" it
### From the beginning
Just run the code mentioned below (you can change the path and paramenters as needed)
- Train: train.py, the result of trained model will be saved in "runs" named "expX"(e.g., exp0,exp1....)
- Test: test.py(use for images) or detect.py (maybe the test.py has some bugs in some computers)
- If you want to change the model or the images(/video/camera) used in the detect.py, you should change the path or source in detect.py
- any question please write it in "Issues", I will check and answer them when I see the comments as soon as possible.
## Result
https://www.bilibili.com/video/BV1ZW4y1a7qN?spm_id_from=333.999.0.0
