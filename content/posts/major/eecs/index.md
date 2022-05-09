---
title: "eecs"
date: 2022-05-09T11:29:13+08:00
draft: false
---

## 学科编码
| 学科体系 | 编码/代号 | 备注 |
| ---- | ---- | ---- |
| UC Berkeley | EECS | https://hkn.eecs.berkeley.edu/courseguides |

## 基础课程
| 课程名称 | 必修/选修 | 备注 |
| ---- | ---- | ---- |
| Design information Devices And Systems | | UC Berkeley 16A |
| Design information Devices And Systems II | | UC Berkeley 16B |

## 专业课程
| 课程名称 | 必修/选修 | 备注 |
| ---- | ---- | ---- |
| Fundamental Algorithms For Systems Modeling, Analysis, And Optimization | | UC Berkeley 144 |
| Introductory Electronic Transducers Laboratory | | UC Berkeley 145L |
| Introduction To Robotics | | UC Berkeley C106A |
| Robotic Manipulation And Interaction | | UC Berkeley C106B |
| Introduction To Embedded Systems | | UC Berkeley 149 |
| Mechatronic Design Laboratory | | UC Berkeley 192 |
| Feedback Control Systems | | UC Berkeley 128 |
| Signals And Systems | | UC Berkeley 120 |
| Digital Signal Processing | | UC Berkeley 123 |
| Probability And Random Processes | | UC Berkeley 126 |
| Introduction To Communication Networks | | UC Berkeley 122 |
| Optimization Models In Engineering | | UC Berkeley 127 |
| Medical Imaging Signals And Systems | | UC Berkeley 145B |
| Electromagnetic Fields And Waves | | UC Berkeley 117 |
| Power Electronics | | UC Berkeley 113 |
| Introduction To Electric Power Systems | | UC Berkeley 137A |
| Introduction To Electric Power Systems | | UC Berkeley 137B |
| Microelectronic Devices And Circuits | | UC Berkeley 105 |
| Linear Integrated Circuits | | UC Berkeley 140 |
| Integrated Circuits For Communications | | UC Berkeley 142 |
| Integrated-Circuit Devices | | UC Berkeley 130 |
| Fundamentals Of Photovoltaic Devices | | UC Berkeley 134 |
| Microfabrication Technology | | UC Berkeley 143 |
| Introduction To Microelectromechanical Systems(MEMS) | | UC Berkeley 147 |
| INTRODUCTION TO OPTICAL ENGINEERING | | UC Berkeley 118 |

## 课程依赖关系

### UC Berkeley体系EE课程关系图
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
