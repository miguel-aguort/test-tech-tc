### Quick guidelines pre-MVP Assistant with pdf-RAG

The code has been developed from scratch based on PoC's tools. In this document you will find guidelines to execute the pre-MVP.

#### Guidelines

1. First, add pdf file that will be process and included in the database to be used in the RAG system. The path is **data/**

2. Add .env file with corresponding environmental variables. Use .env-template file as template.

3. Open a terminal and install conda environment and activate it:
    1. ```console
        $cd Assistant/
        $conda env create -f test-env.yml
        ```
    2. ```console
        $conda activate test_env
        ```

4. In the same terminal, execute the app.py file:
    1. ```console
        $python app.py
        ``` 

At this point, the selected PDF will be processed and the database will start.

Then, all data extracted from the PDF will be loaded into the database, and the LangGraph App will be initialized.

Finally, the Gradio App will start, and a URL will appear in the terminal. Open it and enjoy!