# 基于物理融合神经网络的光伏发电功率预测算法研究

## Dataset
DataCastle国能日新光伏功率预测大赛数据集:https://gitcode.com/open-source-toolkit/8a397/blob/main/%E5%9B%BD%E8%83%BD%E6%97%A5%E6%96%B0%E5%85%89%E4%BC%8F%E5%8A%9F%E7%8E%87%E9%A2%84%E6%B5%8B%E5%A4%A7%E8%B5%9B%E6%95%B0%E6%8D%AE%E9%9B%86.zip

## 流程
1. 将下载好的数据集放在目录./dataset/raw_dataset/下
2. 运行 ./code/data_processing_pre.ipynb 以及 ./code/data_processing_prepare.ipynb 处理数据， 处理好的数据分别存放在./dataset/pre_dataset/ 以及./dataset/prepare_dataset/ 下
3. 运行 ./code/formular_cell.ipynb 以及 ./codeformular_effi.ipynb 实现物理模型，结果存放在./dataset/final_dataset/下面
4. 分别运行原文中的模型, 包括LightGBM模型：machine_learning.ipynb, CNN-LSTM模型：cnn_lstm.ipynb, LightGBM混合模型：combine_ml.ipynb, CNN-LSTM-PINN：cnn_lstm_pinns.ipynb,  CNN-LSTM混合模型：cnn_lstm_combine.ipynb

## Reference 
https://github.com/yyhhlancelot/DC_power_prediction_rank21

感谢原作者的开源代码，本文的数据处理操作代码在此基础上进行了一些改进，对应代码./tools/
