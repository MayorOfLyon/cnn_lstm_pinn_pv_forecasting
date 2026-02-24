# Research on Photovoltaic Power Prediction Algorithm Based on Physics-Informed Neural Networks

## Dataset

DataCastle Guoneng Rixin Photovoltaic Power Prediction Competition Dataset: https://gitcode.com/open-source-toolkit/8a397/blob/main/%E5%9B%BD%E8%83%BD%E6%97%A5%E6%96%B0%E5%85%89%E4%BC%8F%E5%8A%9F%E7%8E%87%E9%A2%84%E6%B5%8B%E5%A4%A7%E8%B5%9B%E6%95%B0%E6%8D%AE%E9%9B%86.zip

## Workflow

1. Place the downloaded dataset in the directory `./dataset/raw_dataset/`.
2. Run `./code/data_processing_pre.ipynb` and `./code/data_processing_prepare.ipynb` to process the data. The processed data will be stored in `./dataset/pre_dataset/` and `./dataset/prepare_dataset/` respectively.
3. Run `./code/formular_cell.ipynb` and `./code/formular_effi.ipynb` to implement the physical models. The results will be stored under `./dataset/final_dataset/`.
4. Run the models mentioned in the original text respectively, including the LightGBM model: `machine_learning.ipynb`, CNN-LSTM model: `cnn_lstm.ipynb`, LightGBM hybrid model: `combine_ml.ipynb`, CNN-LSTM-PINN: `cnn_lstm_pinns.ipynb`, and CNN-LSTM hybrid model: `cnn_lstm_combine.ipynb`.

## Reference

https://github.com/yyhhlancelot/DC_power_prediction_rank21

Thanks to the original author for open-sourcing their code. The data processing code in this project includes some improvements based on their work, and the corresponding updated code is located in `./tools/`.
