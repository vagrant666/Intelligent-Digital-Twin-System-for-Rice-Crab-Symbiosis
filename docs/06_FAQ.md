# 项目常见问题FAQ
## 一、环境安装
Q1：ModuleNotFoundError
A：pip install -r requirements.txt，严格使用Python3.10，版本不兼容会报错。
Q2：CUDA显存不足
A：自动切换CPU训练；可修改global_config降低BATCH_SIZE。

## 二、数据采集报错
Q3：API连续3次请求失败
A：1.检查外网能否访问NASA/FAO官网；2.调大API_INTERVAL；3.等待服务器限流解除。
Q4：提示不支持离线仿真
A：项目无模拟数据生成代码，必须联网拉取官方数据，非BUG。

## 三、模型训练
Q5：提前触发早停
A：正常防过拟合机制，自动保存最优权重，不影响最终效果。
Q6：模型R²过低
A：删除data/raw所有csv，重新采集完整多源数据。

## 四、输出文件缺失
Q7：output无图表/Excel
A：程序中途异常中断，查看logs/system_run.log定位报错。
Q8：帕累托解集太少
A：修改global_config的NSGA_POP、NSGA_GEN增大种群与迭代数。

## 五、参数自定义
Q9：修改农场经纬度、数据年份
A：调整config/global_config内LAT、LON、DATA_START_YEAR、DATA_END_YEAR。
Q10：调整时序窗口、模型隐藏层
A：data_config控制时序；model_config单独管理各模型超参，无需修改源码。

## 六、开源规范
Q11：是否可商用
A：MIT协议，允许商用修改分发，保留原始版权声明即可。
Q12：代码提交PR流程
A：按CONTRIBUTING.md规范，从dev新建feature分支，完成单元测试后提交审核。
