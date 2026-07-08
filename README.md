@'
# Rice-Crab Intelligent Digital Twin System
Full Industrial Open-Source Agricultural Decision Platform

## Introduction
This full-stack digital twin system targets rice-crab symbiotic farm. All datasets are real public official data from NASA POWER & FAOSTAT without simulation data.
Multi deep learning models + multi-objective optimization + UAV path planning integrated.
Standard PyTorch training pipeline with 1000 epoch full training, early stop, learning rate decay, checkpoint resume.

## Data Source
1. NASA POWER: 10-year daily meteorology data
2. FAOSTAT: Global rice & crustacean production, cost, market statistics
3. Public agricultural open data: soil nutrient, pest risk
4. Remote sensing NDVI crop growth data

## Algorithm Stack
### Deep Learning
- CNN-Transformer Hybrid Model
- LSTM-Attention Time Series Model
- Residual Regression Network
- SSA-BP Optimized Neural Network

### Traditional Optimization
- NSGA-II Four-objective planting optimization
- GA UAV patrol path planning
- ARIMA time series prediction
- Random Forest Ensemble Evaluation

## Training Pipeline
- Max epoch: 1000
- Train/Val/Test split: 0.7 / 0.15 / 0.15
- Exponential learning rate decay
- Early stopping (patience=30) anti-overfitting
- Auto save loss & metric curves
- Checkpoint breakpoint resume training

## Quick Start
```bash
# Install dependencies
pip install -r requirements.txt
# Run full pipeline
run_all.bat  # Windows
bash run_all.sh # Linux / Mac

Output Assets
Raw & processed official 10-year time series dataset
Standard tensor train/val/test dataset
Best model weight checkpoint
Training loss, R², MAE visualization figures
Pareto optimal solution diagram
UAV full coverage patrol route graph
Complete Excel analysis report
License
MIT License
'@ | Out-File README.md -Encoding utf8