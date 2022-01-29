from .models import Customer_Machine,Customer_Machine_Recipe,Setting_Item



class RecipeModelComplement:
    """ビューから呼び出されて、モデルを補完する"""
    def machine_model_complement(self,object):
        #idから機種を書込み
        for recipe_i in object:
            if (recipe_i.Machine_model==None) and (recipe_i.Customer_machine_id != None):
                    for c_machine in Customer_Machine.objects.select_related('Machine_model').all():
                       if recipe_i.Customer_machine_id == c_machine.Customer_machine_id:
                            try:
                                recipe_i.Machine_model = str(c_machine.Machine_model) + ': #' +str(c_machine.Customer_machine_unit_no)                  
                                recipe_i.save()
                            except:
                                pass
    
    def recipe_model_complement(self,object):
        #品種No.から品種名を書込み
                
        for recipe_i in object:
            if (recipe_i.Recipe_name==None) and (recipe_i.Customer_recipe_no != None):
                for name_j in Setting_Item.objects.all():
                    if (recipe_i.Recipe_id == name_j.Setting_item_id) and (name_j.Setting_item_name != None):
                        try:
                            recipe_i.Recipe_name = name_j.Setting_item_name                  
                            print("test test test")
                            recipe_i.save()
                        except:
                            pass

