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

#### EE

| 编号 | 课程名称 | 类别 | 备注 |
| ---- | ---- | ---- | ---- |
| 16A | Designing Information Devices And Systems I | required | |
| 16B | Designing Information Devices And Systems II | required | |
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
| 118 | Introduction To Optical Engineering | optics | |

#### CS
| 编号 | 课程名称 | 类别 | 备注 |
| ---- | ---- | ---- | ---- |
| 61A | The Structure And Interpretation Of Computer Programs | core | |
| 61B | Data Structures | core | |
| 61C | Machine Structures | core | |
| 70 | Discrete Mathematics And Probability Theory | core | |
| 186 | Introduction To Database Systems | applications | |
| 184 | Foundations Of Computer Graphics | applications | |
| 188 | Introduction To Artificial Intelligence | applications | |
| 189 | Introduction To Machine Learning | applications | |
| 160 | User Interface Design And Development | software | |
| 161 | Computer Security | software | |
| 162 | Operating Systems And System Programming | software | |
| 164 | Programming Languages And Compilers | software | |
| 168 | Introduction To The Internet: Architecture And Protocols | software | |
| 169 | Software Engineering | software | |
| 170 | Efficient Algorithms And Intractable Problems | theory | |
| 172 | Computability And Complexity | theory | |
| 174 | Combinatorics And Discrete Probability | theory | |
| 176 | Algorithms For Computational Biology | theory | |
| 191 | Quantum Information Science And Technology | theory | |
| 152 | Computer Architecture And Engineering | hardware | |


### UC Berkeley体系EECS课程路线图

#### EE
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

#### CS
```graphviz
digraph {
    rankdir=LR;

    # core nodes
    c61A [label="61A"];
    c61B [label="61B"];
    c61C [label="61C"];
    c70 [label="70"];

    # core cluster
    subgraph cluster_core {
        c61A; c61B; c61C; c70;
        label="core";
    }

    # applications nodes
    c186 [label="186"];
    c184 [label="184"];
    c188 [label="188"];
    c189 [label="189"];

    # applications cluster
    subgraph cluster_applications {
        c186; c184; c188; c189;
        label="applications";
    }

    # software nodes
    c160 [label="160"];
    c161 [label="161"];
    c162 [label="162"];
    c164 [label="164"];
    c168 [label="168"];
    c169 [label="169"];

    # software cluster
    subgraph cluster_software {
        c160; c161; c162; c164; c168; c169;
        label="software";
    }

    # theory nodes
    c170 [label="170"];
    c172 [label="172"];
    c174 [label="174"];
    c176 [label="176"];
    c191 [label="191"];

    # theory cluster
    subgraph cluster_theory {
        c170; c172; c174; c176; c191;
        label="theory";
    }

    # hardware nodes
    c152 [label="152"];

    # hardware cluster
    subgraph cluster_hardware {
        c152;
        label="hardware";
    }

    ##### core dependency #####
    # 61B
    c61A->c61B;

    # 61C
    c61B->c61C;

    ##### applications dependency #####
    # 184
    c61B->c184;

    # 186
    c61C->c186;

    # 188
    c70->c188;
    c170->c188

    # 189
    c188->c189

    ##### software dependency #####
    # 160
    c61B->c160;

    # 161
    c61C->c161;
    c70->c161;

    # 162
    c70->c162;
    c61C->c162;

    # 164
    c61C->c164;

    # 168
    c61B->c168;

    # 169
    c61C->c169;

    ##### theory dependency #####
    # 170
    c61B->c170;
    c70->c170;

    # 172
    c170->c172;

    # 174
    c170->c174;

    # 176
    c170->c176;

    # 191
    c170->c191;

    ##### hardware dependency #####
    # 152
    c61C->c152;
}
```