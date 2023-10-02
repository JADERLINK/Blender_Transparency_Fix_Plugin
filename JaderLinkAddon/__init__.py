#by JADERLINK
#GitHub: https://github.com/JADERLINK
#reference: https://blender.stackexchange.com/questions/220490/changing-default-blend-mode-settings-for-materials
#https://github.com/JADERLINK/Blender_Transparency_Fix_Plugin

bl_info = {
	"name": "JADERLINK TextureFix",
	"author": "JADERLINK",
	"version": (1, 0, 0),
	"blender": (3, 6, 0)
}

import bpy
 
class ADDONNAME_PT_main_panel(bpy.types.Panel):
    
    bl_label = "Change Transparency Material Panel"
    bl_idname = "MYADDON_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Change All Material'
 
    def draw(self, context):
        layout = self.layout
        layout.operator("addonname.hashed_operator")
        layout.operator("addonname.clip_operator")    
        layout.operator("addonname.opaque_operator")    
        layout.operator("addonname.set_texture_alfa_operator")    
 
 
 
class ADDONNAME_OT_Change_to_HASHED(bpy.types.Operator):
    bl_label = "Change Materials to HASHED"
    bl_idname = "addonname.hashed_operator"
    
    
    def execute(self, context):
               
        for x in bpy.data.materials:
            x.blend_method = "HASHED"
            x.shadow_method = "HASHED"
    
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
 
 
class ADDONNAME_OT_Change_to_CLIP(bpy.types.Operator):
    bl_label = "Change Materials to CLIP"
    bl_idname = "addonname.clip_operator"
    
    
    def execute(self, context):
        
        for x in bpy.data.materials:
            x.blend_method = "CLIP"
            x.shadow_method = "CLIP"
    
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
 
 
class ADDONNAME_OT_Change_to_OPAQUE(bpy.types.Operator):
    bl_label = "Change Materials to OPAQUE"
    bl_idname = "addonname.opaque_operator"
    
    
    def execute(self, context):
        
        for x in bpy.data.materials:
            x.blend_method = "OPAQUE"
            x.shadow_method = "OPAQUE"
    
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
 
class ADDONNAME_OT_set_texture_alfa(bpy.types.Operator):
    bl_label = "Set Texture Alfa For Principled BSDF"
    bl_idname = "addonname.set_texture_alfa_operator"
    
    
    def execute(self, context):
        
        for x in bpy.data.materials:
        
            try:       
                node_1 = x.node_tree.nodes.get('Principled BSDF')
                node_2 = x.node_tree.nodes.get('Image Texture')
                x.node_tree.links.new(node_2.outputs["Alpha"], node_1.inputs["Alpha"])  
            except:
                print("Error!")
    
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
 
classes = [ADDONNAME_PT_main_panel, ADDONNAME_OT_Change_to_CLIP, ADDONNAME_OT_Change_to_HASHED, ADDONNAME_OT_Change_to_OPAQUE, ADDONNAME_OT_set_texture_alfa]
 
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
 
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
 
 
if __name__ == "__main__":
    register()