bl_info = {
    "name": "Image Finder in Materials",
   "blender": (4, 0, 0),  
    "category": "Object",
    "author": "Alvaro Rosati",
    "description": "Search for a selected image in all materials' textures.",
    "version": (1, 0),
    "support": "COMMUNITY",
}

import bpy

def execute_script(self, context):
    image_name = context.id.name
    found = False
    for mat in bpy.data.materials:
        if mat.use_nodes:
            for node in mat.node_tree.nodes:
                if node.type == 'TEX_IMAGE' and node.image and node.image.name == image_name:
                    self.report({'INFO'}, f"Image {image_name} found in material {mat.name}")
                    found = True

    if not found:
        self.report({'INFO'}, f"No match found for image {image_name} in materials.")

class OUTLINER_OT_execute_script(bpy.types.Operator):
    bl_idname = "outliner.execute_script"
    bl_label = "Find Image in Materials"
    bl_description = "Search for the selected image in all materials' textures"

    def execute(self, context):
        execute_script(self, context)
        return {'FINISHED'}

def menu_func(self, context):
    layout = self.layout
    if context.id and isinstance(context.id, bpy.types.Image):
        layout.operator(OUTLINER_OT_execute_script.bl_idname, text="Find Image in Materials")

def register():
    bpy.utils.register_class(OUTLINER_OT_execute_script)
    bpy.types.OUTLINER_MT_context_menu.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OUTLINER_OT_execute_script)
    bpy.types.OUTLINER_MT_context_menu.remove(menu_func)

if __name__ == "__main__":
    register()
