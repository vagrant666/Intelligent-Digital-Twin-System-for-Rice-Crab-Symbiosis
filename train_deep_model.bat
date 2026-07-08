@echo off
chcp 65001
echo 仅执行深度学习模型训练流程
python -c "from src.train.trainer import DeepTrainer; print('训练模块就绪，请先完成数据采集')"
pause
