import bpy

# Add-On metadata for Blender
bl_info = {"name": "Gear Creator", "category": "Mesh", "author": "github.com/aalajoki"}

class CreateGearHeader(bpy.types.Header):
    # Create a header into the 3D view
    bl_idname = "OBJECT_HT_create_gear"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        # Create a button that calls CreateCogOperator.invoke on a click
        row.operator("object.create_gear_operator", text="Create Gear", icon="SCRIPTWIN")

class CreateGearOperator(bpy.types.Operator):
    # Operator identifier
    bl_idname = "object.create_gear_operator"

    # Dialog pop-up content
    bl_label = "Create Gear"
    test_int = bpy.props.IntProperty(name="Test integer")

    def execute(self, context):
        # Close the dialog pop-up
        message = "Test int is " + str(self.test_int)
        self.report({'INFO'}, message)
        return {'FINISHED'}

    def invoke(self, context, event):
        # Open a dialog pop-up
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

# Register the classes into Blender, allowing Blender to instantiate them and call their functions
def register():
    bpy.utils.register_class(CreateGearOperator)
    bpy.utils.register_class(CreateGearHeader)

def unregister():
    bpy.utils.unregister_class(CreateGearOperator)
    bpy.utils.unregister_class(CreateGearHeader)


if __name__ == "__main__":
    register()
