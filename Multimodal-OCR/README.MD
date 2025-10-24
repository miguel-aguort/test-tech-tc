### Quick guidelines RAG GUI PoC

The code comes from **https://docling-project.github.io/docling/examples/export_multimodal/**

First you need to install conda environment using: 
```console
$cd OCR/
$conda env create -f test-env-multimodal-ocr.yml
```

Then, execute the code with:
```console
$conda avtivate test_env_multimodal_ocr
$python app.py
```

The output parquet file will be written in ../data/scratch