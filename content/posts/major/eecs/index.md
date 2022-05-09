---
title: "EECS"
date: 2022-05-09T14:30:35+08:00
draft: false
---

## 学科编码
| 学科体系 | 编码 | 备注 |
| ---- | ---- | ---- |
| UC Berkeley | EECS | https://hkn.eecs.berkeley.edu/courseguides |

## 课程列表与路线图

### UC Berkeley体系EECS课程列表

| 编号 | 课程名称 | 类别 | 备注 |
| ---- | ---- | ---- | ---- |
| 16A | Designing Information Devices And Systems I | required | |
| 16B | DESIGNING INFORMATION DEVICES AND SYSTEMS II | required | |
| 144 | Fundamental Algorithms For Systems Modeling, Analysis, And Optimization | robotics | |
| 145L | Introductory Electronic Transducers Laboratory | robotics | |
| C106A | Introduction To Robotics | robotics | |
| C106B | Robotic Manipulation And Interaction | robotics | |
| 149 | Introduction To Embedded Systems | robotics | |
| 192 | Mechatronic Design Laboratory | robotics | |
| 128 | Feedback Control Systems | robotics | |
| 120 | Signals And Systems | signals | |
| 123 | Digital Signal Processing | signals | |
| 126 | Probability And Random Processes | signals | |
| 122 | Introduction To Communication Networks | signals | |
| 127 | Optimization Models In Engineering | signals | |
| 145B | Medical Imaging Signals And Systems | signals | |
| 117 | Electromagnetic Fields And Waves | power | |
| 113 | Power Electronics | power | |
| 137A | Introduction To Electric Power Systems | power | |
| 137B | Introduction To Electric Power Systems | power | |
| 105 | Microelectronic Devices And Circuits | circuits | |
| 140 | Linear Integrated Circuits | circuits | |
| 142 | Integrated Circuits For Communications | circuits | |
| 130 | Integrated-Circuit Devices | devices | |
| 134 | Fundamentals Of Photovoltaic Devices | devices | |
| 143 | Microfabrication Technology | devices | |
| 147 | Introduction To Microelectromechanical Systems(MEMS) | devices | |
| 118 | INTRODUCTION TO OPTICAL ENGINEERING | optics | |

### UC Berkeley体系EECS课程路线图
```graphviz
digraph {
    rankdir=LR;

    # required nodes
    c16A [label="16A"];
    c16B [label="16B"];

    # robotics nodes
    c144 [label="144"];
    c145L [label="145L"];
    c106A [label="C106A"];
    c106B [label="C106B"];
    c149 [label="149"];
    c192 [label="192"];
    c128 [label="128"];

    # signals nodes
    c120 [label="120"];
    c123 [label="123"];
    c126 [label="126"];
    c145B [label="145B"];
    c127 [label="127"];
    c122 [label="122"];

    # power nodes
    c117 [label="117"];
    c113 [label="113"];
    c137A [label="137A"];
    c137B [label="137B"];

    # circuits nodes
    c105 [label="105"];
    c140 [label="140"];
    c142 [label="142"];

    # devices nodes
    c130 [label="130"];
    c143 [label="143"];
    c134 [label="134"];
    c147 [label="147"];

    # optics nodes
    c118 [label="118"];

    # required cluster
    subgraph cluster_required {
        c16A; c16B;
        label="required";
    }

    # robotics cluster
    subgraph cluster_robotics {
        c144; c145L; c149;
        c106A; c106B;
        c192; c128;
        label="robotics";
    }

    # signal cluster
    subgraph cluster_signal {
        c120; c123; c126;
        c145B; c127; c122;
        label="signal";
    }

    # power cluster
    subgraph cluster_power {
        c117; c113; c137A; c137B;
        label="power";
    }

    # circuits cluster
    subgraph cluster_circuits {
        c105; c140; c142;
        label="circuits";
    }

    # devices cluster
    subgraph cluster_devices {
        c130; c134; c143; c147;
        label="devices";
    }

    # optics cluster
    subgraph cluster_optics {
        c118;
        label="optics";
    }

    ##### required dependency #####
    c16A->c16B;

    ##### robotics dependency #####
    # 144
    c16B->c144;

    # 145L
    c145L;

    # 149
    c16B->c149;

    # C106A
    c120->c106A;

    # C106B
    c106A->c106B

    # 192
    c120->c192;

    ##### signal dependency #####
    # 120
    c16B->c120;

    # 123
    c120->c123;

    # 126
    c16B->c126;

    # 145B
    c16B->c145B;

    ##### power dependency #####
    # 117
    c16B->c117;

    # 137A
    c16B->c137A;

    # 137B
    c137A->c137B;

    # 113
    c105->c113;

    ##### circuits dependency #####
    # 105
    c16B->c105;

    # 140
    c105->c140;

    # 142
    c117->c142;
    c140->c142;

    ##### devices dependency #####
    # 130
    c105->c130;

    # 143
    c16B->c143;

    # 134
    c16B->c134;

    # 147
    c16B->c147;
}
```
