import cv2
import os


def convert_png_to_cascade_xml(png_file, xml_file, obj_width, obj_height):
    # Load the PNG image using OpenCV
    image = cv2.imread(png_file)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform object detection using Haar-like features
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    objects = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(obj_width, obj_height))

    # Create the XML string
    xml_str = '<opencv_storage>\n'
    xml_str += f'<cascade type_id="opencv-cascade-classifier">\n'
    xml_str += f'  <stageType>BOOST</stageType>\n'
    xml_str += f'  <featureType>HAAR</featureType>\n'
    xml_str += f'  <height>{obj_height}</height>\n'
    xml_str += f'  <width>{obj_width}</width>\n'
    xml_str += f'  <stageParams>\n'
    xml_str += f'    <maxWeakCount>0</maxWeakCount>\n'
    xml_str += f'    <stageThreshold>-1.0</stageThreshold>\n'
    xml_str += f'    <weakClassifiers>\n'

    for i, (x, y, w, h) in enumerate(objects):
        xml_str += f'      <_>\n'
        xml_str += f'        <internalNodes>{i * 9} -1 0 1 {int(x + w / 2)} {int(y + h / 2)}</internalNodes>\n'
        xml_str += f'        <leafValues>0.0 1.0</leafValues>\n'
        xml_str += f'      </_>\n'

    xml_str += f'    </weakClassifiers>\n'
    xml_str += f'  </stageParams>\n'
    xml_str += f'  <featureParams>\n'
    xml_str += f'    <maxCatCount>0</maxCatCount>\n'
    xml_str += f'    <featSize>{obj_width * obj_height}</featSize>\n'
    xml_str += f'  </featureParams>\n'
    xml_str += f'</cascade>\n'
    xml_str += f'</opencv_storage>'

    # Save the XML string to a file
    with open(xml_file, 'w') as f:
        f.write(xml_str)


# Provide the paths for the PNG and XML files
png_file = "clear.png"
xml_file = "output.xml"

# Specify the dimensions of the object to be detected
object_width = 100
object_height = 100

# Perform the conversion
convert_png_to_cascade_xml(png_file, xml_file, object_width, object_height)