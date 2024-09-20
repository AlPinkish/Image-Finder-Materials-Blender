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

# Funzione che cerca l'immagine nei materiali
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

# Funzione che cancella l'immagine se non è usata in nessun materiale
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

# Definisci l'operatore che esegue lo script
class OUTLINER_OT_execute_script(bpy.types.Operator):
    bl_idname = "outliner.execute_script"
    bl_label = "Find Image in Materials"
    bl_description = "Search for the selected image in all materials' textures"

    def execute(self, context):
        execute_script(self, context)
        return {'FINISHED'}

# Definisci l'operatore che cancella l'immagine se non è usata
class OUTLINER_OT_delete_image(bpy.types.Operator):
    bl_idname = "outliner.delete_unused_image"
    bl_label = "Delete Image if Unused"
    bl_description = "Delete the selected image if it is not used in any materials"

    def execute(self, context):
        delete_image_if_unused(self, context)
        return {'FINISHED'}

# Funzione per aggiungere gli operatori al menu contestuale dell'Outliner (Blender File -> Images)
def menu_func(self, context):
    layout = self.layout
    if context.id and isinstance(context.id, bpy.types.Image):
        layout.operator(OUTLINER_OT_execute_script.bl_idname, text="Find Image in Materials", icon='VIEWZOOM')
        layout.operator(OUTLINER_OT_delete_image.bl_idname, text="Delete Image if Unused", icon='TRASH')

# Registra le classi e aggiungi le voci al menu contestuale dell'Outliner
def register():
    bpy.utils.register_class(OUTLINER_OT_execute_script)
    bpy.utils.register_class(OUTLINER_OT_delete_image)
    bpy.types.OUTLINER_MT_context_menu.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OUTLINER_OT_execute_script)
    bpy.utils.unregister_class(OUTLINER_OT_delete_image)
    bpy.types.OUTLINER_MT_context_menu.remove(menu_func)

if __name__ == "__main__":
    register()
