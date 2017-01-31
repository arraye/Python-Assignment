#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 15:14:37 2017

@author: Lauren
"""

#### PARSE_CSV ####
#

from collections import namedtuple
import csv


    
class Error(Exception):
    pass

class IncompatibleHeadersError(Error):
    pass


headers=['rowid', 'pl_hostname', 'pl_letter', 'pl_discmethod', 'pl_pnum', 'pl_orbper', 'pl_orbsmax', 'pl_orbeccen', 'pl_orbincl', 'pl_bmassj', 'pl_bmassprov', 'pl_radj', 'pl_dens', 'pl_ttvflag', 'pl_kepflag', 'pl_k2flag', 'pl_nnotes', 'ra_str', 'ra', 'dec_str', 'dec', 'st_dist', 'st_optmag', 'st_optband', 'gaia_gmag', 'st_teff', 'st_mass', 'st_rad', 'rowupdate', 'pl_name', 'pl_tranflag', 'pl_rvflag', 'pl_imgflag', 'pl_astflag', 'pl_omflag', 'pl_cbflag', 'pl_orbtper', 'pl_orblper', 'pl_rvamp', 'pl_eqt', 'pl_insol', 'pl_massj', 'pl_msinij', 'pl_masse', 'pl_msinie', 'pl_bmasse', 'pl_rade', 'pl_rads', 'pl_trandep', 'pl_trandur', 'pl_tranmid', 'pl_tsystemref', 'pl_imppar', 'pl_occdep', 'pl_ratdor', 'pl_ratror', 'pl_def_reflink', 'pl_disc', 'pl_disc_reflink', 'pl_locale', 'pl_facility', 'pl_telescope', 'pl_instrument', 'pl_status', 'pl_mnum', 'pl_st_npar', 'pl_st_nref', 'pl_pelink', 'pl_edelink', 'pl_publ_date', 'hd_name', 'hip_name', 'st_rah', 'st_glon', 'st_glat', 'st_elon', 'st_elat', 'st_plx', 'gaia_plx', 'gaia_dist', 'st_pmra', 'st_pmdec', 'st_pm', 'gaia_pmra', 'gaia_pmdec', 'gaia_pm', 'st_radv', 'st_sp', 'st_spstr', 'st_logg', 'st_lum', 'st_dens', 'st_metfe', 'st_metratio', 'st_age', 'st_vsini', 'st_acts', 'st_actr', 'st_actlx', 'swasp_id', 'st_nts', 'st_nplc', 'st_nglc', 'st_nrvc', 'st_naxa', 'st_nimg', 'st_nspec', 'st_uj', 'st_vj', 'st_bj', 'st_rc', 'st_ic', 'st_j', 'st_h', 'st_k', 'st_wise1', 'st_wise2', 'st_wise3', 'st_wise4', 'st_irac1', 'st_irac2', 'st_irac3', 'st_irac4', 'st_mips1', 'st_mips2', 'st_mips3', 'st_iras1', 'st_iras2', 'st_iras3', 'st_iras4', 'st_photn', 'st_umbj', 'st_bmvj', 'st_vjmic', 'st_vjmrc', 'st_jmh2', 'st_hmk2', 'st_jmk2', 'st_bmy', 'st_m1', 'st_c1', 'st_colorn']
data_nt = namedtuple('data_np',headers)


def file_is_csv(filename):
    allowed_extensions = (".csv")
    if filename.lower().endswith(allowed_extensions): return True
    return False
        

def check_headers(imported_headers):
        if not imported_headers == headers:
            print("ERROR: Incompatible headers in csv file!")
            print("Expected headers: " + str(headers))
            raise IncompatibleHeadersError
        return(imported_headers)
    
def import_csv_as_ntuple(path):
            
    data=[]
    imported_headers=[]
    exoplanets=[]
    
    with open(path) as csv_file:
        csvreader = csv.reader(csv_file)
        for line in csvreader:
            if not line[0].startswith('#'):     #Ignore all comments in csv
                if not line[0].isdigit():
                    if not imported_headers:    #If 
                        #print("Detected headers: " + str(line))
                        imported_headers = check_headers(line)
                else:
                    #data.append(line)
                    exoplanets.append(data_nt._make(line))
    return(imported_headers,exoplanets)

def as_list(path):
    
    data=[]
    imported_headers=[]
    headers_dict={}
    exoplanets=[]

    if not file_is_csv(path):
        raise ValueError("Incorrect filetype. Please run with a CSV file.")

    
    with open(path) as csv_file:
        csvreader = csv.reader(csv_file)
        for line in csvreader:
            if not line[0].startswith('#'):
                if not line[0].isdigit():
                    if not headers_dict:    
                        # Assume headers appear once at the top of the file, 
                        # and are the first non-comment non-digit rows.
                        # If further header-like rows appear, treat as data.
                        headers_dict={line[i]: i for i in range(len(line))}
                    else:
                        data.append(line)
                else:
                    data.append(line)

    return(data,headers_dict)  