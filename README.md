# TINIEE: Traffic-Aware Adaptive In-Network Intelligence via Early-Exit Strategy

## Overview of TINIEE

<p align="center">
<img src="Figures/TINIEE_Overview.png" alt="TINIEE Overview" width="600">

TINIEE implements deep neural network (DNN) models with early-exit strategies in programmable data planes (PDP). By leveraging intermediate classifiers within the DNN, it dynamically evaluates confidence scores at each switch to decide whether packets should exit early or proceed to subsequent layers. This adaptive mechanism effectively balances network traffic management and inference accuracy.

# Performance Results

## BMv2 environments
### In-Network Classification Performances
<table>
  <tr>
    <td align="center"><img src="Figures/Accuracy.png" width="250"/></td>
    <td align="center"><img src="Figures/F1_score.png" width="250"/></td>
    <td align="center"><img src="Figures/Exit_tendency.png" width="180"/></td>
  </tr>
  <tr>
    <td align="center">Accuracy</td>
    <td align="center">F1-score</td>
    <td align="center">Exit Tendency</td>
  </tr>
</table>

### Network Performances
<table>
  <tr>
    <td align="center"><img src="Figures/Traffic.png" width="250"/></td>
    <td align="center"><img src="Figures/MLU.png" width="240"/></td>
    <td align="center"><img src="Figures/Flow_completion_time.png" width="250"/></td>
  </tr>
  <tr>
    <td align="center">Network Traffic</td>
    <td align="center">Maximum Link Utlization</td>
    <td align="center">Flow Completion Time</td>
  </tr>
</table>

## Tofino environments
### Topology
This is the topology used during the performance evaluation of TINIEE on the Tofino:
<img src="Figures/Tofino_topology.png" widt="800"/>
Traffic was generated and sent by host1 towards host2, with each switch running three submodels of TINIEE. Note that three submodels are actually deployed in the single Wedge100BF 32X Tofino switch, but logically separated by allocating different ports.

### Performance
<table>
  <tr>
    <td align="center"><img src="Figures/Processing_delay.png" width="350"/></td>
  </tr>
  <tr>
    <td align="center">Processing Delays</td>
  </tr>
</table>
