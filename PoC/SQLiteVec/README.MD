### Quick guidelines SQLiteVec PoC

The code comes from **https://python.langchain.com/docs/integrations/vectorstores/sqlitevec/**

First you need to install conda environment using: 
```console
$cd Multimodal-OCR/
$conda env create -f test-env-sqlitevec.yml
```

Then, execute the code with:
```console
$conda avtivate test_env_multimodal_ocr
$python app.py
```

The output parquet file will be written in ../data/scratch