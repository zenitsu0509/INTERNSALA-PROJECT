Setup PDF2Image, PyTesseract, and libGL in GitHub Codespaces
------------------------------------------------------------

### Prerequisites

-   GitHub Codespaces environment
## run requirements.txt
```
pip install -r requirements.txt
```
### 1\. **Update Package Lists**

Run the following commands to update the package lists:

```
sudo -i
sudo apt-get update
```

### 2\. **Install `pdf2image`**

Install the `pdf2image` library using pip:

```
pip install pdf2image
```

### 3\. **Install Poppler**

PDF2Image requires **Poppler** to convert PDF files into images. Install it with:

```
sudo apt-get install -y poppler-utils
```

### 4\. **Install `pytesseract`**

Install the Tesseract OCR library and the Python wrapper:



```
pip install pytesseract
```

### 5\. **Install Tesseract OCR**

Install Tesseract OCR on your system:


```
sudo apt-get install -y tesseract-ocr
```

### 6\. **Install `libgl1` for OpenCV Compatibility**

The OpenCV library requires `libGL` to display images. Install it with:



```
sudo apt-get install -y libgl1
```

### 7\. **Verify Installations**

Check that all installations are complete and working:

-   **PDF2Image**:


    ```
    python -c "from pdf2image import convert_from_path; print('PDF2Image is installed')"
    ```

-   **PyTesseract**:

    ```
    tesseract --version
    ```

-   **Poppler**:
   ```
    pdfinfo -v
  ```
