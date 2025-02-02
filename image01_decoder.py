from aspose.barcode import barcoderecognition

reader = barcoderecognition.BarCodeReader("01_image.png", barcoderecognition.DecodeType.ALL_SUPPORTED_TYPES)
recognized_results = reader.read_bar_codes()
for barcode in recognized_results:
    print(barcode.code_text)
