import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from nilearn import plotting
from nilearn import image
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D
import scipy.ndimage as ndi
########### CARGAR (LEER) IMAGEN #########################################################################################################
#Guardar dirección
img_path="I:/UNIVERSIDAD 4/ANALISIS Y METODOS NUMERICOS/MRIsamples/1_24.hdr"
#Cargar imagen con Nibabel
t1=nib.load(img_path)

############# MOSTRAR IMAGEN - 3 ejes orientación de corte del volumen espacial ####################################################
""""
OrthoSlicer3D(t1.dataobj).show()
plt.show()

"""
############ MOSTRAR HEADER - ver metadatos ##########################################################################################################################

t1_hdr = t1.header

"""
print(t1_hdr)

"""
############ ACCEDER A DATOS DEL OBJETO ######################################################################################################################################################

t1_data = t1.get_fdata()
""""
######### tipo de dato #########################################################################################################
print(t1_data.dtype)

"""
#############SHAPE - forma ################################################################################################################################################
"""
height, width, depth, channels=t1_data.shape



print(f"El objeto de imagen tiene las siguientes dimensiones: height: {height}, width:{width}, depth:{depth}, channels:{channels}")
"""

########### MOSTRAR UNA IMAGEN DEL CONJUNTO DE IMAGENES ##########################################################################################
"""
mxval = 255
i = np.random.randint(0, mxval)
channel = 0
print(f"Plotting Layer {i} Channel {channel} of Image")
#plt.imshow(t1_data[:, :, i, channel], cmap='gray')
#plt.axis('on');
#plt.show()
"""
######## MOSAICO DE 4x4 ########################################################################################################################
"""
fig_rows = 4
fig_cols = 4
n_subplots = fig_rows * fig_cols
n_slice = t1_data.shape[0]
step_size = n_slice // n_subplots
plot_range = n_subplots * step_size
start_stop = int((n_slice - plot_range) / 2)

fig, axs = plt.subplots(fig_rows, fig_cols, figsize=[10, 10])

for idx, img in enumerate(range(start_stop, plot_range, step_size)):
    axs.flat[idx].imshow(ndi.rotate(t1_data[img, :, :], 90), cmap='gray')
    axs.flat[idx].axis('on')
        
plt.tight_layout()
plt.show()
"""

fig, ax = plt.subplots(figsize=[8, 3])
plotting.plot_img(t1, cmap='gray', axes=ax)
plt.show()

#plotting.plot_img(t1, display_mode='mosaic', cmap='gray')
#plt.show()

fwhm = 1

#brain_vol_smth = image.smooth_img(t1, fwhm)
#plotting.plot_img(brain_vol_smth, cmap='gray', cut_coords=(-45, 40, 0))
#plt.show()

######################### CONVERSIÓN DE HDR A NIFTI ######################################


t1_affine= t1.affine

print(t1_affine)

t1_nifti = nib.Nifti1Image(t1_data, t1_affine)

#nib.save(t1_nifti, 'I:/UNIVERSIDAD 4/ANALISIS Y METODOS NUMERICOS/Archivos_nifti/1_24.nii')
#print("--------------------saved---------------------------")
##################Comprobación de conversión de HDR a archivo Nifti#####################

#img_path2="I:/UNIVERSIDAD 4/ANALISIS Y METODOS NUMERICOS/Archivos_nifti/1_24.nii"
#t1_nii = nib.load(img_path2)
#t1_data_nii = t1_nii.get_fdata()
#OrthoSlicer3D(t1_nii.dataobj).show()





    

