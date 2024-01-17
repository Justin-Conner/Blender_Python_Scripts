import bpy
import bmesh
import math

# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Create a new mesh
mesh = bpy.data.meshes.new(name="TetrahedronMesh")
obj = bpy.data.objects.new("Tetrahedron", mesh)

# Link the object to the scene
bpy.context.scene.collection.objects.link(obj)

# Select the object and make it the active object
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

# Enter Edit mode and create the tetrahedron
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.primitive_cone_add(vertices=3, depth=1, radius1=1, radius2=0, location=(0, 0, 0))

# Exit Edit mode
bpy.ops.object.mode_set(mode='OBJECT')

# Set the origin to the center of mass
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='BOUNDS')

# Rotate the tetrahedron to align with its natural orientation
obj.rotation_euler = (math.radians(54.7356), 0, 0)  # 54.7356 degrees is the tetrahedron's edge angle

# Update the scene
bpy.context.view_layer.update()
