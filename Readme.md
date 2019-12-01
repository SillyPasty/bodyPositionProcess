# 算法设计报告

[TOC]

## 需求

### 功能概述

- 通过对人体关键点识别算法输出数据流的处理，实现了对测试周期内体测动作（仰卧起坐、俯卧撑、引体向上）的计数和标准判断。

### 功能需求

- 处理数据流

  判断动作周期

  判断动作是否标准

## 结构

### 设计概念

- 功能主要分为动作周期判断和标准程度判断。

- 通过对特定身体关键点向量之间的夹角比较、向量与关键点的比较，实现判断。

### 详细设计

#### 总体结构

![](https://raw.githubusercontent.com/SillyPasty/CloudImg/master/data/image-20191130163347408.png)

#### 模块描述

- 数据输入：包含位置矩阵的键-值对。
- 数据处理模块：对输入的数据流进行处理，选取特定点坐标矩阵构建向量、计算夹角。
- 趋势分析模块：根据数据分析趋势
  -  趋势概念：对于参数x进行判断，每t秒（帧）为一个判断区间，记录区间内x的最大值max与最小值min，对于t秒（帧）内所有大于min且在更新max的x的数量，超过了x总数的p%，则称之为上行趋势，同理对于t秒（帧）内所有小于max且在更新min的x的数量，超过了x总数的p%，称之为下行趋势，否则称为稳定趋势。
- 周期判断：一段连续上行趋势（区间数大于X）和一段连续下行趋势（区间数大于X）为一个周期，周期区间为上行趋势开始到下行趋势结束（其间可能包括稳定趋势）。
- 计算判断：根据特定向量夹角、向量和关键点的位置比较判断动作标注程度
- 记录数据：将每周期的数据记录。
- 是否到时：如果到时，显示结束。
- 数据输出：.json格式输出总数、有效个数、百分比、速度、姿势分析。

## 实现

### 命名标准

- 其中变量采用下划线命名法（**全局变量、外来变量采用大写下划线命名**），文件名、函数采用小驼峰命名法。 **后续改为面对对象编程？**

### 文件结构

```
bodyPosit
│  analysis.py
│  bodyPositionDetect.cfg
│  getValue.py
│  jsonProcess.py
│  main.py
│  pullUp.py
│  pushUp.py
│  strProc.py
│  test.py
│  tree.txt
│  writeCfg.py
│ 
└─output
   │  push-up-front-side.avi
   │  push-up-side.avi
   │  
   ├─push-up
   │      俯卧撑－正侧_000000000000_keypoints.json
   │                                               ..
   │      俯卧撑－正侧_000000000236_keypoints.json
   │      
   └─push-up-front-side


```



### 算法模块

#### 数据输入、处理

- `jsonProcess.py`

#### 趋势分析

- `analysis.py`
  - `getTendency(tick, var)`

#### 周期判断

- `pullUp.py`
- `pushUp.py`

#### 计算判断

- `analysis.py`
  - `pushUpPeriodJudge(...)`
  - `pullUpPeriodJudge(...)`

#### 数据输出

- `pullUp.py`
- `pushUp.py`

### 算法文件及接口说明

- `bodyPositionDetect.cfg`: 各种判断参数

- `writeCfg.py`: 对.cfg文件的修改

- `jsonProcess.py`: 对openpose输出的.json文件进行处理，返回一个储存坐标的字典。

- `getValue.py`: 各种求值函数，可以根据坐标获得关键点的距离、角度等参数
- `getAngle(d1, d2, d3)`: 获得$ ∠d_1d_2d_3 $
  
     - `getDistance(d1, d2, d3)`: 获得点$d_1$和过两点直线$d_2d_3$之间的距离的绝对值
    - 求值参数`(coor, side)`: coor为包含身体关键点位置的字典，side为身体方向
      - `getElbowAngle(coor, side)`: 肘关节角度
    
      - `getHipAngle(coor, side)`: 臀部角度
    
      - `getKneeAngle(coor, side)`: 膝盖角度
    
      - `getHipDistance(coor, side)`: 臀部高度（目前以手腕和大脚趾为地面判断依据）
    
      - `getHeadDistance(coor, side)`: 脖子与单杠绝对距离（目前以两手腕连线为单杠判断依据）
    
      - `getEyeWristDistance(coor, side)`:眼部与单杠距离（目前以两手腕连线为单杠判断依据）***\*此函数对特定情况进行了优化，视频水平传入时（针对x轴），若眼睛over单杠，距离为负\****

---

- `pullUp.py`: 引体向上判断模块
- `pullUpAnalyis(folder_path)`:输入openpose返回的`.json`文件夹路径，读取文件并进行判断，返回一个字典列表，其中包含了数量、标准信息、周期之间的tick（debug用）。

---

- `pushUp.py`: 俯卧撑判断模块
- `pushUpAnalyis(folder_path)`:输入openpose返回的`.json`文件夹路径，读取文件并进行判断，返回一个字典列表，其中包含了数量、标准信息、周期之间的tick（debug用）。

---

- `analysis.py`: 趋势、标准判断模块
- `getTendency(tick, var)`: 对每个tick的趋势判断，输入一个tick的待判断值列表和判断方差（消抖用），返回`'down'/'upper'/None`。
  
- `pullUpPeriodJudje(r_elbow_angle_list, l_elbow_angle_list, eye_distance_list)`: 输入一个周期中的两肘关节、眼部与单杠距离的列表，对其中数值变化进行判断，返回一个布尔元组，为两肘关节（L，R）和眼部高度是否达标。
  
- `pushUpPeriodJudge(r_elbow_angle_list, hip_angle_list, r_knee_angle_list)`: 输入一个周期中的肘关节、臀部角度与膝盖角度的列表，对其中数值变化进行判断，返回一个布尔元组，为肘关节、臀部角度、膝盖角度是否达标。

---

- `test.py`: 对数据的分析与可视化，同时对结果进行测试。

- `main.py`: 主函数。