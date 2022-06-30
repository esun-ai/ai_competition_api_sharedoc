# README
* 程式架構
    * [請將程式碼有依據的分類，列出2層內的檔案架構]
    * [層數或內容可視情況簡化調整]
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

* 程式環境
    * [請說明本次比賽所使用的系統平台、程式語言、函式庫，並提供所需函式庫對應的版本]
    * requirments.txt範例：```套件==版號 -> torch==1.8.1```

* 執行方式及原始碼
    * [請說明從資料源頭至答案的產出執行過程]
    * [請於重點設計程式(尤其是資料處理的部分)上加上註解，並在每個檔案夾放入簡單的說明檔]
    * 執行步驟範例 (可以依照團隊需求調整內容)：
        ```
        #安裝虛擬環境 
        $ python3 -m venv venv

        #啟動虛擬環境 
        $ source venv/bin/activate

        #安裝所需套件
        $ pip install -r requirements.txt 

        #執行前處理
        $ python data_preprocess.py

        # 執行模型訓練
        $ python training.py

        # 執行模型推論
        $ python inference.py

        #關閉 virtual environment
        $ deactivate
        ```