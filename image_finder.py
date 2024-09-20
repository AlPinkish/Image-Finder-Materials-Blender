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
        self.report({'WARNING'}, f"No match found for image {image_name} in materials.")

def delete_image_if_unused(self, context):
    image_name = context.id.name
    found = False
    for mat in bpy.data.materials:
        if mat.use_nodes:
            for node in mat.node_tree.nodes:
                if node.type == 'TEX_IMAGE' and node.image and node.image.name == image_name:
                    self.report({'ERROR'}, f"Cannot delete: Image {image_name} is used in material {mat.name}")
                    found = True
                    break

    if not found:
        image = context.id
        bpy.data.images.remove(image)
        self.report({'INFO'}, f"Deleted! {image_name} is not used in any materials.")

def delete_all_unused_images(self, context):
    unused_images = []

    for image in bpy.data.images:
        found = False
        for mat in bpy.data.materials:
            if mat.use_nodes:
                for node in mat.node_tree.nodes:
                    if node.type == 'TEX_IMAGE' and node.image and node.image.name == image.name:
                        found = True
                        break
            if found:
                break
        if not found:
            unused_images.append(image.name)

    for image_name in unused_images:
        image = bpy.data.images.get(image_name)
        if image:
            bpy.data.images.remove(image)
            self.report({'INFO'}, f"Deleted! {image_name} is not used in any materials.")

class OUTLINER_OT_execute_script(bpy.types.Operator):
    bl_idname = "outliner.execute_script"
    bl_label = "Find Image in Materials"
    bl_description = "Search for the selected image in all materials' textures"

    def execute(self, context):
        execute_script(self, context)
        return {'FINISHED'}

class OUTLINER_OT_delete_image(bpy.types.Operator):
    bl_idname = "outliner.delete_unused_image"
    bl_label = "Delete Image if Unused"
    bl_description = "Delete the selected image if it is not used in any materials"

    def execute(self, context):
        delete_image_if_unused(self, context)
        return {'FINISHED'}

class OUTLINER_OT_delete_all_unused_images(bpy.types.Operator):
    bl_idname = "outliner.delete_all_unused_images"
    bl_label = "Delete All Unused Images"
    bl_description = "Delete all images that are not used in any materials"

    def execute(self, context):
        delete_all_unused_images(self, context)
        return {'FINISHED'}

def menu_func(self, context):
    layout = self.layout
    if context.id and isinstance(context.id, bpy.types.Image):
        layout.operator(OUTLINER_OT_execute_script.bl_idname, text="Find Image in Materials", icon='VIEWZOOM')
        layout.operator(OUTLINER_OT_delete_image.bl_idname, text="Delete Image if Unused", icon='TRASH')
    layout.operator(OUTLINER_OT_delete_all_unused_images.bl_idname, text="Delete All Unused Images", icon='TRASH')

def register():
    bpy.utils.register_class(OUTLINER_OT_execute_script)
    bpy.utils.register_class(OUTLINER_OT_delete_image)
    bpy.utils.register_class(OUTLINER_OT_delete_all_unused_images)
    bpy.types.OUTLINER_MT_context_menu.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OUTLINER_OT_execute_script)
    bpy.utils.unregister_class(OUTLINER_OT_delete_image)
    bpy.utils.unregister_class(OUTLINER_OT_delete_all_unused_images)
    bpy.types.OUTLINER_MT_context_menu.remove(menu_func)

if __name__ == "__main__":
    register()
