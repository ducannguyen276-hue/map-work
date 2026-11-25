from qgis.core import (
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsProject,
    QgsVectorLayer,
    QgsFeature,
    QgsGeometry
)
from qgis.gui import QgsMapToolEmitPoint


canvas = iface.mapCanvas()

# Create the layer that will hold the points
point_layer = QgsVectorLayer(
    "Point?crs=EPSG:4326",
    "My clicked locations",
    "memory"
)

# Add the layer to QGIS
QgsProject.instance().addMapLayer(point_layer)

# Create connection to the layer and create its attribute
provider = point_layer.dataProvider()
provider.addAttributes([
    QgsField("name", QVariant.String),
    QgsField("category", QVariant.String)
])
point_layer.updateFields()
def show_lat_lon(point, button):
    
    source_crs = canvas.mapSettings().destinationCrs()
    target_crs = QgsCoordinateReferenceSystem("EPSG:4326")

    transform = QgsCoordinateTransform(
        source_crs,
        target_crs,
        QgsProject.instance()
    )

    converted_point = transform.transform(point)

    longitude = converted_point.x()
    latitude = converted_point.y()

    print(f"Latitude: {latitude}, Longitude: {longitude}")

    # Create a feature for this clicked location
    feature = QgsFeature(point_layer.fields())

    # Give the feature its point geometry
    geometry = QgsGeometry.fromPointXY(converted_point)
    feature.setGeometry(geometry)
    feature["name"] = "Study location"
    feature["category"] = "Study"

    # Add the feature to the point layer
    provider.addFeatures([feature])

    # Update the layer and redraw it
    point_layer.updateExtents()
    point_layer.triggerRepaint()


# Create and activate a click tool
click_tool = QgsMapToolEmitPoint(canvas)
click_tool.canvasClicked.connect(show_lat_lon)
canvas.setMapTool(click_tool)