
import zxing
import cv2
import numpy as np

reader = zxing.BarCodeReader()

image_path = "06_image.png"  
image = cv2.imread(image_path)

decoded = reader.decode(image_path)

if decoded:
    print(f"Decoded Data: {decoded.parsed}")
    print(f"Barcode Format: {decoded.format}")

    if decoded.points:
        points = [(int(p.x), int(p.y)) for p in decoded.points]
        cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)

        x, y = points[0]  
        cv2.putText(image, decoded.parsed, (x, y-50 ), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("MaxiCode", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    output_file = "maxicode_decoded.png"
    cv2.imwrite(output_file, image)
    print(f"Annotated image saved as {output_file}")
else:
    print("Failed while decoding the MaxiCode.")