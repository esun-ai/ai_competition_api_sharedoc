# README
## 程式架構
* 請將程式碼有依據的分類，列出2層內的檔案架構
* 以下架構為"**必需**"要有的檔案及資料夾，請自行整理程式架構成以下格式
* 層數或內容可視情況補充調整
    ```
    $ tree -L 2

    .
    ├── README.md
    ├── data_preprocess
    │ └── data_preprocess.py
    ├── inference
    │ └── inference.py
    ├── model
    │ ├── data.py
    │ ├── model.py
    │ └── training.py
    ├── api.py
    └── requirements.txt
    ```

## 程式環境
* 請說明本次比賽所使用的系統平台、程式語言、函式庫，並提供所需函式庫對應的版本
* requirments.txt範例：`套件==版號 -> torch==1.8.1`

## 執行方式及原始碼
* 請說明從資料源頭至答案產出執行過程，範例可以參考下方**執行範例** 
* 請於重點設計程式上加上註解
* 在資料處理的部分請仔細說明所使用的工具，完整處理邏輯，如果有用到額外資料也請附上資料來源以及處理邏輯
* 在推論的部分請仔細說明推論邏輯以及各個函數的作用

## 執行範例
範例執行功能為最低描述需求，參賽者可依照團隊需求增述

* 虛擬環境
    ```
    # 安裝虛擬環境
    $ python3 -m venv venv
    
    # 啟動虛擬環境 
    $ source venv/bin/activate
    
    # 安裝所需套件
    $ pip install -r requirements.txt 
    ```
* 資料前處理
    * 說明針對資料處理的方法，例如：採用的自然語言處理技術
    * 說明是否在資料上有額外擴充，或資料標註上的調整
    ```
    # 執行前處理
    $ python data_preprocess.py
    ```
* 模型訓練
    * 說明採用了什麼模型架構，例如：Transformers 架構或哪一篇開源論文
    * 說明調整的參數，例如：epoch，learning rate
    * 說明使用什麼訓練技巧，例如：warn up schedule，special activation function
    ```
    # 執行模型訓練
    $ python training.py
    ```
* 模型推論
    * 說明是否進行額外的後處理
    * 說明是否優化API執行時間
    ```
    # 執行模型推論
    $ python inference.py
    ```