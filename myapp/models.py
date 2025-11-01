from django.db import models
from django.core.validators import EmailValidator,RegexValidator
import datetime,os
#from django.contrib.postgres.fields import ArrayField

# Create your models here.
def img_plant(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M::%S")
    new_file = "%s%s"%(now_time,filename)
    return os.path.join("upload/plant",new_file)

def img_chem(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M::%S")
    new_file = "%s%s"%(now_time,filename)
    return os.path.join("upload/chem",new_file)

def img_dock(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M::%S")
    new_file = "%s%s"%(now_time,filename)
    return os.path.join("upload/dock",new_file)

class Reference(models.Model):
    reference = models.CharField(max_length=255,null = True,blank=True)
    title = models.CharField(max_length = 255,null = True, blank= True)
    def __str__(self):
        return self.title

class Target_reference(models.Model):
    dock_reference = models.CharField(max_length=255,null = True,blank=True)
    dock_title = models.CharField(max_length = 255,null = True, blank= True)
    def __str__(self):
        return self.dock_title    




class Contact(models.Model):
    name = models.CharField(max_length=50,null = True,blank=True)
    email = models.CharField(max_length=254, validators=[EmailValidator(message='Enter a valid email address.')])
    phone_no = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$', message='Enter a valid phone number.')])
    message = models.TextField(null = True,blank=True)
    time_of_submit = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Target(models.Model):

    name = models.CharField(max_length=255,null=True,blank=True,default="Not available")
    score = models.CharField(max_length=255,null=True,blank=True,default="Not available")
    iupac_name = models.CharField(max_length=555,null=True,blank=True,default = "Not available")
    kegg = models.CharField(max_length = 255,null=True,blank = True,default = "Not available")
    dock_im = models.CharField(max_length =255,blank = True,null = True,default = "Not available")
    dock_image = models.ImageField(upload_to=img_dock,null = True,blank=True,default="Not available")
    dock_reference = models.ManyToManyField(Target_reference,blank= True)
    
    def __str__(self):
        return self.name


class McProp(models.Model):

    name = models.CharField(max_length=255,null=True,blank=True,default="Not available")
    molecular_formula = models.CharField(max_length=255,null=True,blank=True,default="Not available")
    iupac_name = models.CharField(max_length=555,null=True,blank=True,default = "Not available")
    kegg = models.CharField(max_length = 255,null=True,blank = True,default = "Not available")
    impaat = models.CharField(max_length =255,blank = True,null = True,default = "Not available")
    chembl = models.CharField(max_length = 255,blank = True,null = True,default = "Not available" )
    pubchem = models.CharField(max_length = 255,blank = True,null = True ,default = "Not available")
    zinc = models.CharField(max_length = 255,blank = True,null = True ,default = "Not available" )
    surecheml = models.CharField(max_length = 255,blank = True,null = True ,default = "Not available")
    Molprot = models.CharField(max_length = 255,blank = True,null = True ,default = "Not available")
    molecular_weight = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    log_p = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    topological_polar_surface_area = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    num_hydrogen_bond_acceptors = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    hydrogen_donor = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    num_carbon_atoms = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    num_heavy_atoms = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    num_heteroatoms = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    num_nitrogen_atoms = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    num_sulfur_atoms = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    num_chiral_carbon_atoms = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    stereochemical_complexity = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    num_sp_hybridized_carbon_atoms = models.CharField(null = True,max_length=255,blank=True,default="Not available")
    num_sp2_hybridized_carbon_atoms = models.CharField(null = True,max_length=255,blank=True,default="Not available")
    num_sp3_hybridized_carbon_atoms = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    shape_complexity = models.CharField(null = True,blank=True,default="Not available",max_length=255)
    num_rotatable_bonds = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    num_aliphatic_carbocycles = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    num_aliphatic_heterocycles = models.CharField(null = True,max_length=255,blank=True,default="Not available")
    num_aliphatic_rings = models.CharField(null = True,blank=True,max_length=255,default="Not available")
    num_aromatic_carbocycles = models.CharField(null = True,blank=True,max_length=255,default="Not available")
    num_aromatic_heterocycles = models.CharField(null = True,blank=True,max_length=255,default="Not available")
    num_aromatic_rings = models.CharField(null = True,blank=True,max_length=255,default="Not available")
    total_num_rings = models.CharField(null = True,blank=True,max_length=255,default="Not available")
    num_saturated_carbocycles = models.CharField(null = True,blank=True,max_length=255,default="Not available")
    num_saturated_heterocycles = models.CharField(null = True,blank=True,max_length=255,default="Not available")
    num_saturated_rings = models.CharField(null = True,blank=True,max_length=255,default="Not available")
    num_sssr = models.CharField(null = True,blank=True,max_length=255,default="Not available")

    def __str__(self):
        return str(self.name)



class ADMEProp(models.Model):

    name = models.CharField(null=True,blank=True,max_length=255,default="Not available")
    bioavailability_score = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    solubility_class_esol = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    solubility_class_silicos_it = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    blood_brain_barrier_permeation = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    gastrointestinal_absorption = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    log_kp_skin_permeation = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    num_pains_structural_alerts = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    num_brenk_structural_alerts = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    cyp1a2_inhibitor = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    cyp2c19_inhibitor = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    cyp2c9_inhibitor = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    cyp2d6_inhibitor = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    cyp3a4_inhibitor = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    p_glycoprotein_substrate = models.CharField(max_length=255,null = True,blank=True,default="Not available")

    def __str__(self):
        return str(self.name)
        
class DkProp(models.Model):

    name = models.CharField(null=True,blank=True,max_length=255,default="Not available")
    lipinski_violations = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    lipinski_rule = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    ghose_violations = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    veber_rule = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    ghose_rule = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    gsk_4_400_rule = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    pfizer_3_75_rule = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    qedw_score = models.CharField(max_length=255,null = True,blank=True,default="Not available")

    def __str__(self):
        return str(self.name)

    
class Phytochemical(models.Model):

    name = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    synonymous_names = models.TextField(null = True,blank=True,default="Not available")
    molecular_formula = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    smiles = models.TextField(null = True,blank=True,default="Not available")
    pubchem_id = models.CharField(max_length=255,null =True,blank=True,default="Not available")
    chem_image = models.ImageField(upload_to=img_chem,null = True,blank=True,default="Not available")
    inchi = models.TextField(null = True,blank=True,default="Not available")
    inchikey = models.TextField(null = True,blank=True,default="Not available")
    deepsmiles = models.TextField(null = True,blank=True,default="Not available")
    functional_groups = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    molecular_formula = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    iupac_name = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    molecular_weight = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    kegg_id = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    chembl_id = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    np_classifier_superclass = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    np_classifier_class = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    np_likeness_score = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    mkproperties = models.OneToOneField(McProp, on_delete=models.CASCADE ,blank =True,null=True )
    dkproperties = models.OneToOneField(DkProp,on_delete = models.CASCADE,blank=True,null=True)
    admeproperties = models.OneToOneField(ADMEProp,on_delete = models.CASCADE,blank=True,null =True)
    target_propper = models.ManyToManyField(Target,blank=True)
    reference_paper = models.ManyToManyField( Reference,blank=True)

    def __str__(self):
        return self.name


    
class Plant(models.Model):
    name = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    botanical_name = models.CharField(max_length = 255,null = True,blank=True,default="Not available")
    family = models.CharField(max_length = 255,null = True,blank=True,default="Not available")
    synonyms = models.CharField(max_length=255,null= True,blank=True,default="Not available")
    groups = models.CharField(max_length=255,null = True,blank=True,default="Not available")
    related_plant = models.CharField(max_length = 255,null = True,blank=True,default="Not available")
    related_diseae = models.CharField(max_length = 255,null = True,blank=True,default="Not available")
    plant_image = models.ImageField(upload_to=img_plant,null = True,blank=True,default="Not available")
    description = models.TextField(null = True,blank=True,default="Not available")
    time_of_add_plant = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    phytochemical_value = models.ManyToManyField(Phytochemical ,blank = True)
    referenceplant = models.ManyToManyField( Reference, blank = True)

    def __str__(self):
        return self.name